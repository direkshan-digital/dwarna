"""
Test the general functionality of the backend.
"""

import json
import os
import sys
import time

import oauth2

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

	@BiobankTestCase.isolated_test
	def test_access_token(self):
		"""
		Perform general tests with requests.
		"""

		token = self._get_access_token(["create_participant"])["access_token"]

		"""
		Test that the access token works.
		"""
		response = self.send_request("POST", "participant", { "username": "nick" }, token)
		self.assertEqual(response.status_code, 200)

	@BiobankTestCase.isolated_test
	def test_invalid_token(self):
		"""
		Make a request with an incorrect access token.
		"""

		"""
		Get a token and invalidate it by changing a single character.
		"""
		token = self._get_access_token(["create_participant"])["access_token"]
		token = list(token)
		token[1] = "Z" if token[1] is not "Z" else "A";
		token = "".join(token)

		"""
		Test that the access token works.
		"""
		response = self.send_request("POST", "participant", { "username": "nick" }, token)
		body = response.json()
		self.assertEqual(response.status_code, 401)
		self.assertEqual(body["exception"], oauth2.error.AccessTokenNotFound.__name__)

	@BiobankTestCase.isolated_test
	def test_argument_checks(self):
		"""
		Test the argument checks.
		"""

		token = self._get_access_token(["create_participant"])["access_token"]

		response = self.send_request("POST", "participant", { "name": "nick" }, token)
		body = response.json()
		self.assertEqual(response.status_code, 400)
		self.assertEqual(body["exception"], request_exceptions.MissingArgumentException.__name__)

	@BiobankTestCase.isolated_test
	def test_method_checks(self):
		"""
		Test the method checks.
		"""

		token = self._get_access_token(["create_participant"])["access_token"]

		response = self.send_request("GET", "create_participant", { "username": "nick" }, token)
		self.assertEqual(response.status_code, 405)

	@BiobankTestCase.isolated_test
	def test_scopes(self):
		"""
		Test that the scope permissions work.
		"""
		access_token = self._get_access_token(["delete_participant"])
		self.assertEqual(access_token["scope"], "none")

		access_token = self._get_access_token(["create_participant", "remove_participant"])
		token = access_token["access_token"]
		self.assertEqual(access_token["scope"], "create_participant remove_participant")
		response = self.send_request("POST", "participant", { "username": "matt" }, token)
		self.assertEqual(response.status_code, 200)

		access_token = self._get_access_token(["remove_participant"])
		token = access_token["access_token"]
		self.assertEqual(access_token["scope"], "remove_participant")
		response = self.send_request("POST", "participant", { "username": "chri" }, token)
		self.assertEqual(response.status_code, 403)

	@BiobankTestCase.isolated_test
	def test_sanitation(self):
		"""
		Test the escaping functionality.
		"""

		token = self._get_access_token(["create_study", "view_study"])["access_token"]

		study_id = self._generate_study_name()
		response = self.send_request("POST", "study", {
			"study_id": study_id,
			"name": "ALS",
			"description": "¯\_(ツ)_/¯",
			"homepage": "http://um.edu.mt",
		}, token)
		body = response.json()
		self.assertEqual(response.status_code, 200)

		response = self.send_volatile_request("GET", "study", { "study_id": study_id }, token)
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
		# NOTE: The optional parameters are all provided since the bash script and argparse do not go well together. (See https://stackoverflow.com/questions/18325211/argparse-fails-when-called-from-unittest-test)
		main.main(TEST_DATABASE, TEST_OAUTH_DATABASE, PORT, single_card=True, token_expiry=4)
		time.sleep(2) # NOTE: Needed to give time for other test servers to shutdown, or for this one to start

	@BiobankTestCase.isolated_test
	def test_short_tokens(self):
		"""
		Test token expiry.
		"""

		access_token = self._get_access_token(["create_participant"])
		self.assertEqual(access_token["scope"], "create_participant")
		token = access_token["access_token"]
		response = self.send_request("POST", "participant", { "username": "nick" }, token)
		self.assertEqual(response.status_code, 200)

		"""
		Wait one second for the token to expire.
		"""
		time.sleep(4)
		response = self.send_request("POST", "participant", { "username": "matt" }, token)
		self.assertEqual(response.status_code, 401)
