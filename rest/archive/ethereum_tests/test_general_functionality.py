"""
Test the general functionality of the backend.
"""

import json
import os
import sys
import time

path = sys.path[0]
path = os.path.join(path, "../")
if path not in sys.path:
	sys.path.insert(1, path)

import main

from biobank.handlers.exceptions import general_exceptions, user_exceptions
from server.exceptions import request_exceptions

from .environment import *

from .test import BiobankTestCase

class GeneralFunctionalityTest(BiobankTestCase):
	"""
	Test the general functionality of the biobank backend.
	"""

	def test_general_requests(self):
		"""
		Perform general tests with requests.
		"""

		clear()

		token = self._get_access_token(["create_participant"])
		token = token["access_token"]

		"""
		Test that the access token works.
		"""
		response = self.send_request("POST", "create_participant", { "username": "nick", "password": "pwd" }, token)
		self.assertEqual(response.status_code, 200)

		"""
		Test the argument checks.
		"""
		response = self.send_request("POST", "create_participant", { "name": "nick", "password": "pwd" }, token)
		body = response.json()
		self.assertEqual(response.status_code, 400)
		self.assertEqual(body["exception"], request_exceptions.MissingArgumentException.__name__)

		"""
		Test the method checks.
		"""
		response = self.send_request("GET", "create_participant", { "username": "nick", "password": "pwd" }, token)
		self.assertEqual(response.status_code, 405)

	def test_scopes(self):
		"""
		Test that the scope permissions work.
		"""
		access_token = self._get_access_token(["delete_participant"])
		self.assertEqual(access_token["scope"], "none")

		access_token = self._get_access_token(["create_participant", "remove_participant"])
		token = access_token["access_token"]
		self.assertEqual(access_token["scope"], "create_participant remove_participant")
		response = self.send_request("POST", "create_participant", { "username": "matt", "password": "pwd" }, token)
		self.assertEqual(response.status_code, 200)

		access_token = self._get_access_token(["remove_participant"])
		token = access_token["access_token"]
		self.assertEqual(access_token["scope"], "remove_participant")
		response = self.send_request("POST", "create_participant", { "username": "chri", "password": "pwd" }, token)
		self.assertEqual(response.status_code, 403)

	def test_escaping(self):
		"""
		Test the escaping functionality.
		"""

		clear()

		token = self._get_access_token(["create_study", "view_study"])["access_token"]

		response = self.send_request("POST", "create_study", {
			"study_id": "2320",
			"name": "ALS",
			"description": "¯\_(ツ)_/¯",
			"homepage": "http://um.edu.mt",
		}, token)
		body = response.json()
		self.assertEqual(response.status_code, 200)

		response = self.send_volatile_request("GET", "get_study_by_id", { "study_id": 2320 }, token)
		body = response.json()
		study = body["study"]
		self.assertEqual(study["description"], "¯\_(ツ)_/¯")

class GeneralTimedFunctionalityTest(BiobankTestCase):
	"""
	Test the general functionality of the biobank backend.
	This test incorporates very short-lived access tokens.
	"""

	@classmethod
	def setUpClass(self):
		"""
		Connect with the database, create the schema and start the server.
		"""

		create_testing_environment()
		main.main(TEST_DATABASE, TEST_OAUTH_DATABASE, PORT, 1)
		time.sleep(2) # NOTE: Needed to give time for other test servers to shutdown, or for this one to start

	def test_short_tokens(self):
		"""
		Test token expiry.
		"""

		access_token = self._get_access_token(["create_participant"])
		self.assertEqual(access_token["scope"], "create_participant")
		token = access_token["access_token"]
		response = self.send_request("POST", "create_participant", { "username": "nick", "password": "pwd" }, token)
		self.assertEqual(response.status_code, 200)

		"""
		Wait one second for the token to expire.
		"""
		time.sleep(2)
		response = self.send_request("POST", "create_participant", { "username": "matt", "password": "pwd" }, token)
		self.assertEqual(response.status_code, 401)
