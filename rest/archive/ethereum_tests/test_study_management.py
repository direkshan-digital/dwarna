"""
Test the study management functionality in the backend.
"""

from datetime import datetime, timedelta

import json
import os
import sys

path = sys.path[0]
path = os.path.join(path, "../")
if path not in sys.path:
	sys.path.insert(1, path)

import main

from biobank.handlers.exceptions import general_exceptions, study_exceptions, user_exceptions
from server.exceptions import request_exceptions

from .environment import *

from .test import BiobankTestCase

class UserManagementTest(BiobankTestCase):
	"""
	Test the study management functionality of the biobank backend.
	"""

	def test_create_study(self):
		"""
		Test the study creation functionality.
		"""

		clear()

		token = self._get_access_token(["create_study", "create_researcher"])["access_token"]

		"""
		Test parameters.
		"""
		response = self.send_request("POST", "create_study", { "name": "nick" }, token)
		body = response.json()
		self.assertEqual(response.status_code, 400)
		self.assertEqual(body["exception"], request_exceptions.MissingArgumentException.__name__)

		"""
		Normal study creation.
		"""

		response = self.send_request("POST", "create_study", {
			"study_id": "2320",
			"name": "ALS",
			"description": "ALS Study",
			"homepage": "http://um.edu.mt",
			"researchers": [],
		}, token)
		body = response.json()
		self.assertEqual(response.status_code, 200)

		response = self.send_volatile_request("POST", "create_study", {
			"study_id": "2320",
			"name": "ALS",
			"description": "ALS Study",
			"homepage": "http://um.edu.mt",
			"researchers": [],
		}, token, 500)
		body = response.json()
		self.assertEqual(response.status_code, 500)
		self.assertEqual(body["exception"], study_exceptions.StudyExistsException.__name__)

		"""
		Studies with researchers.
		"""

		response = self.send_request("POST", "create_study", {
			"study_id": "8190",
			"name": "ALS",
			"description": "ALS Study",
			"homepage": "http://um.edu.mt",
			"researchers": ["nick", "bill"],
		}, token)
		body = response.json()
		self.assertEqual(response.status_code, 500)
		self.assertEqual(body["exception"], user_exceptions.ResearcherDoesNotExistException.__name__)

		response = self.send_request("POST", "create_researcher", { "username": "nick" }, token)
		response = self.send_request("POST", "create_researcher", { "username": "bill" }, token)

		response = self.send_request("POST", "create_study", {
			"study_id": "8190",
			"name": "ALS",
			"description": "ALS Study",
			"homepage": "http://um.edu.mt",
			"researchers": ["nick", "bill"],
		}, token)
		body = response.json()
		self.assertEqual(response.status_code, 200)

	def test_get_study(self):
		"""
		Test getting a single study.
		"""

		clear()

		token = self._get_access_token(["create_study", "view_study", "create_researcher"])["access_token"]

		"""
		Test parameters.
		"""
		response = self.send_request("GET", "get_study_by_id", { }, token)
		body = response.json()
		self.assertEqual(response.status_code, 400)
		self.assertEqual(body["exception"], request_exceptions.MissingArgumentException.__name__)

		response = self.send_request("GET", "get_study_by_id", { "study_id": 8190 }, token)
		body = response.json()
		self.assertEqual(response.status_code, 500)
		self.assertEqual(body["exception"], study_exceptions.StudyDoesNotExistException.__name__)

		"""
		Create sample data.
		"""

		response = self.send_request("POST", "create_researcher", { "username": "nick" }, token)
		response = self.send_request("POST", "create_researcher", { "username": "bill" }, token)

		response = self.send_request("POST", "create_study", {
			"study_id": "8190",
			"name": "ALS",
			"description": "ALS Study",
			"homepage": "http://um.edu.mt",
			"researchers": ["bill", "nick"],
		}, token)
		body = response.json()
		self.assertEqual(response.status_code, 200)

		response = self.send_volatile_request("GET", "get_study_by_id", { "study_id": 8190 }, token)
		body = response.json()
		self.assertEqual(response.status_code, 200)
		self.assertEqual(body["study"]["study_id"], 8190)
		self.assertEqual(len(body["researchers"]), 2)

	def test_list_study(self):
		"""
		Test study listings.
		"""

		clear()

		token = self._get_access_token(["create_study", "view_study"])["access_token"]

		"""
		Create a few studies.
		"""
		response = self.send_request("POST", "create_study", {
			"study_id": "2320",
			"name": "ALS",
			"description": "ALS study",
			"homepage": "http://um.edu.mt",
			"researchers": [],
		}, token)

		response = self.send_request("POST", "create_study", {
			"study_id": "8190",
			"name": "Diabetes",
			"description": "Diabetes study",
			"homepage": "http://um.edu.mt",
			"researchers": [],
		}, token)

		for i in range(0, 10):
			response = self.send_request("POST", "create_study", {
				"study_id": 2322 + i,
				"name": "Study %d" % i,
				"description": "Another study",
				"homepage": "http://um.edu.mt",
				"researchers": [],
			}, token)

		"""
		Get studies normally.
		First, however, wait for the creation to finish.
		"""
		for i in range(0, 10):
			response = self.send_volatile_request("GET", "get_study_by_id", { "study_id": 2322 + i }, token)

		response = self.send_request("GET", "get_studies", { }, token)
		self.assertEqual(response.status_code, 200)
		response = self.send_request("GET", "get_active_studies", { }, token)
		self.assertEqual(response.status_code, 200)

		"""
		Limit number.
		"""

		response = self.send_request("GET", "get_studies", { "number": 10 }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 10)

		response = self.send_request("GET", "get_active_studies", { "number": 10 }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 10)

		response = self.send_request("GET", "get_studies", { "number": 20 }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 12)

		response = self.send_request("GET", "get_active_studies", { "number": 1 }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 1)

		response = self.send_request("GET", "get_studies", { "number": -20 }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 12)

		response = self.send_request("GET", "get_active_studies", { "number": -20 }, token)
		body = response.json()["data"]
		total = response.json()["total"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 12)
		self.assertEqual(total, 12)

		response = self.send_request("GET", "get_active_studies", { "number": 0 }, token)
		body = response.json()["data"]
		total = response.json()["total"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 0)
		self.assertEqual(total, 12)

		"""
		Pagination control.
		"""

		response = self.send_request("GET", "get_studies", { "page": 20 }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 0)

		response = self.send_request("GET", "get_active_studies", { "number": 1, "page": 20 }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 0)

		response = self.send_request("GET", "get_studies", { "page": 1 }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 10)

		response = self.send_request("GET", "get_active_studies", { "number": 10, "page": 1 }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 10)

		response = self.send_request("GET", "get_studies", { "page": 2 }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 2)

		response = self.send_request("GET", "get_studies", { "page": -1 }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 10)

		response = self.send_request("GET", "get_studies", { "number": 5, "page": 3 }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 2)

		"""
		Search.
		"""

		response = self.send_request("GET", "get_studies", { "search": "ALS" }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 1)
		self.assertEqual(body[0]["study"]["study_id"], 2320)

		response = self.send_request("GET", "get_active_studies", { "search": "ALS" }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 1)
		self.assertEqual(body[0]["study"]["study_id"], 2320)

		response = self.send_request("GET", "get_studies", { "search": "als study", "case_sensitive": False }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 1)
		self.assertEqual(body[0]["study"]["study_id"], 2320)

		response = self.send_request("GET", "get_active_studies", { "search": "als study", "case_sensitive": False }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 1)
		self.assertEqual(body[0]["study"]["study_id"], 2320)

		response = self.send_request("GET", "get_studies", { "search": "als study", "case_sensitive": True }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 0)

		response = self.send_request("GET", "get_active_studies", { "search": "als study", "case_sensitive": True }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 0)

		response = self.send_request("GET", "get_studies", { "search": "study", "number": 5, "page": 3 }, token)
		body = response.json()["data"]
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(body), 2)
		self.assertEqual(response.json()["total"], 12)

	def test_researcher_studies(self):
		"""
		Test filtering studies by reseachers.
		"""

		clear()

		token = self._get_access_token(["create_study", "update_study", "view_study", "create_researcher"])["access_token"]

		"""
		Create a few researchers and studies.
		"""

		response = self.send_request("POST", "create_researcher", { "username": "nick" }, token)
		response = self.send_request("POST", "create_researcher", { "username": "bill" }, token)

		response = self.send_request("POST", "create_study", {
			"study_id": "2320",
			"name": "ALS",
			"description": "ALS study",
			"homepage": "http://um.edu.mt",
			"researchers": ["nick", "bill"],
		}, token)

		response = self.send_request("POST", "create_study", {
			"study_id": "8190",
			"name": "Diabetes",
			"description": "Diabetes study",
			"homepage": "http://um.edu.mt",
			"researchers": ["bill"],
		}, token)

		response = self.send_request("POST", "create_study", {
			"study_id": "4540",
			"name": "Thalassemia",
			"description": "Thalassemia study",
			"homepage": "http://um.edu.mt",
			"researchers": ["nick", "bill"],
		}, token)

		response = self.send_volatile_request("GET", "get_study_by_id", { "study_id": 2320 }, token)
		response = self.send_volatile_request("GET", "get_study_by_id", { "study_id": 8190 }, token)
		response = self.send_volatile_request("GET", "get_study_by_id", { "study_id": 4540 }, token)

		"""
		Get studies normally.
		"""

		response = self.send_request("GET", "get_studies_by_researcher", { }, token)
		self.assertEqual(response.status_code, 400)
		body = response.json()
		self.assertEqual(body["exception"], request_exceptions.MissingArgumentException.__name__)

		response = self.send_request("GET", "get_studies_by_researcher", { "researcher": "nick" }, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 2)

		response = self.send_request("GET", "get_studies_by_researcher", { "researcher": "bill" }, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 3)

		"""
		Limit number.
		"""

		response = self.send_request("GET", "get_studies_by_researcher", {
			"researcher": "nick",
			"number": 2
		}, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 2)

		response = self.send_request("GET", "get_studies_by_researcher", {
			"researcher": "nick",
			"number": 1
		}, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 1)

		response = self.send_request("GET", "get_studies_by_researcher", {
			"researcher": "nick",
			"number": 3
		}, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 2)

		"""
		Pagination control.
		"""

		response = self.send_request("GET", "get_studies_by_researcher", {
			"researcher": "nick",
			"page": 20
		}, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 0)

		response = self.send_request("GET", "get_studies_by_researcher", {
			"researcher": "nick",
			"number": 1,
			"page": 3
		}, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 0)

		response = self.send_request("GET", "get_studies_by_researcher", {
			"researcher": "nick",
			"page": 1
		}, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 2)

		response = self.send_request("GET", "get_studies_by_researcher", {
			"researcher": "nick",
			"number": 2,
			"page": 1
		}, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 2)

		response = self.send_request("GET", "get_studies_by_researcher", {
			"researcher": "nick",
			"number": 1,
			"page": 2
		}, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 1)

		response = self.send_request("GET", "get_studies_by_researcher", {
			"researcher": "nick",
			"page": -1
		}, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 2)

		"""
		Search.
		"""

		response = self.send_request("GET", "get_studies_by_researcher", {
			"researcher": "nick",
			"search": "ALS",
			"case_sensitive": False,
		}, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 1)
		self.assertEqual(body[0]["study"]["study_id"], 2320)

		response = self.send_request("GET", "get_studies_by_researcher", {
			"researcher": "nick",
			"search": "diabetes",
			"case_sensitive": False,
		}, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 0)

		response = self.send_request("GET", "get_studies_by_researcher", {
			"researcher": "bill",
			"search": "diabetes",
			"case_sensitive": False,
		}, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 1)
		self.assertEqual(body[0]["study"]["study_id"], 8190)

		response = self.send_request("GET", "get_studies_by_researcher", {
			"researcher": "bill",
			"search": "diabetes",
			"case_sensitive": True,
		}, token)
		self.assertEqual(response.status_code, 200)
		body = response.json()["data"]
		self.assertEqual(len(body), 0)

	def test_update_study(self):
		"""
		Test study updates.
		"""

		clear()

		token = self._get_access_token(["create_study", "update_study", "view_study", "create_researcher"])["access_token"]

		"""
		Create a few researchers and studies.
		"""

		response = self.send_request("POST", "create_researcher", { "username": "nick" }, token)
		response = self.send_request("POST", "create_researcher", { "username": "bill" }, token)

		response = self.send_request("POST", "create_study", {
			"study_id": "2320",
			"name": "ALS",
			"description": "ALS study",
			"homepage": "http://um.edu.mt",
			"researchers": ["nick", "bill"],
		}, token)

		response = self.send_request("POST", "create_study", {
			"study_id": "8190",
			"name": "Diabetes",
			"description": "Diabetes study",
			"homepage": "http://um.edu.mt",
			"researchers": ["bill"],
		}, token)

		response = self.send_volatile_request("GET", "get_study_by_id", { "study_id": 2320 }, token)
		response = self.send_volatile_request("GET", "get_study_by_id", { "study_id": 8190 }, token)

		"""
		Test normal updating.
		"""

		response = self.send_request("POST", "update_study", {
			"study_id": "8190",
			"name": "Diabetes Type I",
			"description": "Diabetes study",
			"homepage": "http://um.edu.mt",
			"researchers": ["bill"],
		}, token)
		self.assertEqual(response.status_code, 200)
		response = self.send_request("GET", "get_study_by_id", { "study_id": 8190 }, token)
		body = response.json()["study"]
		self.assertEqual(body["name"], "Diabetes Type I")

		"""
		Test updating researchers.
		"""

		response = self.send_request("POST", "update_study", {
			"study_id": "8190",
			"name": "Diabetes",
			"description": "Diabetes study",
			"homepage": "http://um.edu.mt",
			"researchers": ["nick"],
		}, token)
		self.assertEqual(response.status_code, 200)

		response = self.send_request("GET", "get_study_by_id", { "study_id": 8190 }, token)
		body = response.json()["researchers"]
		self.assertEqual(body[0]["user_id"], "nick")

		response = self.send_request("GET", "get_study_by_id", { "study_id": 2320 }, token)
		body = response.json()["researchers"]
		self.assertEqual(body[0]["user_id"], "nick")
		self.assertEqual(body[1]["user_id"], "bill")

	def test_remove_study(self):
		"""
		Test study removals.
		"""

		clear()

		token = self._get_access_token(["create_study", "update_study", "remove_study", "view_study", "create_researcher"])["access_token"]

		"""
		Create a few researchers and studies.
		"""

		response = self.send_request("POST", "create_researcher", { "username": "nick" }, token)
		response = self.send_request("POST", "create_researcher", { "username": "bill" }, token)

		response = self.send_request("POST", "create_study", {
			"study_id": "2320",
			"name": "ALS",
			"description": "ALS study",
			"homepage": "http://um.edu.mt",
			"researchers": ["nick", "bill"],
		}, token)

		response = self.send_request("POST", "create_study", {
			"study_id": "8190",
			"name": "Diabetes",
			"description": "Diabetes study",
			"homepage": "http://um.edu.mt",
			"researchers": ["bill"],
		}, token)

		"""
		Test normal deletion.
		"""

		response = self.send_volatile_request("GET", "get_study_by_id", { "study_id": 2320 }, token)
		response = self.send_volatile_request("GET", "get_study_by_id", { "study_id": 8190 }, token)

		response = self.send_request("GET", "get_studies", { }, token)
		body = response.json()
		self.assertEqual(len(body["data"]), 2)

		response = self.send_request("POST", "remove_study", { "study_id": 8190 }, token)
		self.assertEqual(response.status_code, 200)

		response = self.send_request("GET", "get_studies", { }, token)
		body = response.json()
		self.assertEqual(len(body["data"]), 1)

		"""
		Test getting a deleted study.
		"""
		response = self.send_request("GET", "get_study_by_id", { "study_id": 8190 }, token)
		body = response.json()
		self.assertEqual(body["exception"], study_exceptions.StudyDoesNotExistException.__name__)

		response = self.send_request("GET", "get_study_by_id", { "study_id": 2320 }, token)
		body = response.json()
		self.assertEqual(response.status_code, 200)
