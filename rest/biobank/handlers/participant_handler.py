"""
The route handler to handle participant-related requests.
"""

import json
import os
import psycopg2
import subprocess
import sys
import threading
import traceback

path = sys.path[0]
path = os.path.join(path, "../../")
if path not in sys.path:
	sys.path.insert(1, path)

from oauth2.web import Response

from .exceptions import general_exceptions, study_exceptions, user_exceptions
from .handler import UserHandler

from config import erasure

class ParticipantHandler(UserHandler):
	"""
	The participant handler class receives and handles requests that are related to participants.
	"""

	def create_participant(self, username, first_name="", last_name="", email="", *args, **kwargs):
		"""
		Insert a participant into the database.

		:param username: The participant's username.
		:type username: str
		:param first_name: The participant's first name.
		:type first_name: str
		:param first_name: The participant's last name.
		:type first_name: str
		:param email: The participant's email.
		:type email: str

		:return: A response with any errors that may arise.
		:rtype: :class:`oauth2.web.Response`
		"""

		response = Response()

		try:
			username = self._sanitize(username)

			if self._participant_exists(username):
				raise user_exceptions.ParticipantExistsException()
			elif self._user_exists(username):
				raise user_exceptions.UserExistsException()

			attributes = self._encrypt_participant({
				'username': username,
				'first_name': first_name,
				'last_name': last_name,
				'email': email,
			})

			self._connector.execute([
				"""
				INSERT INTO
					users (user_id, role)
				VALUES
					('%s', '%s');
				""" % (username, "PARTICIPANT"),
				"""
				INSERT INTO
					participants (user_id, first_name, last_name, email)
				VALUES
					('%s', '%s', '%s', '%s');
				""" % (username, attributes['first_name'], attributes['last_name'], attributes['email']),
				"""
				INSERT INTO
					participant_subscriptions (participant_id)
				VALUES
					('%s');
				""" % (username),
			])

			response.status_code = 200
			response.add_header("Content-Type", "application/json")
			response.body = json.dumps({ })
		except (general_exceptions.InputException,
				user_exceptions.ParticipantExistsException,
				user_exceptions.UserExistsException) as e:
			response.status_code = 500
			response.add_header("Content-Type", "application/json")
			response.body = json.dumps({ "error": str(e), "exception": e.__class__.__name__ })
		except Exception as e:
			response.status_code = 500
			response.add_header("Content-Type", "application/json")
			response.body = json.dumps({ "error": "Internal Server Error: %s" % str(e), "exception": e.__class__.__name__ })

		return response

	def update_participant(self, username, first_name=None, last_name=None, email=None, *args, **kwargs):
		"""
		Update a participant.

		:param username: The participant's new username.
		:type username: str
		:param first_name: The participant's new first name.
						   If it is not given, then it is not updated.

		:type first_name: str or None
		:param last_name: The participant's new last name.
						   If it is not given, then it is not updated.

		:type last_name: str or None
		:param email: The participant's new email.
					  If it is not given, then it is not updated.

		:type email: str or None

		:return: A response with any errors that may arise.
		:rtype: :class:`oauth2.web.Response`
		"""

		response = Response()

		try:
			username = self._sanitize(username)

			if not self._participant_exists(username):
				raise user_exceptions.ParticipantDoesNotExistException()

			attributes = self._encrypt_participant({
				'username': username,
				'first_name': first_name,
				'last_name': last_name,
				'email': email,
			})

			sql = """
				UPDATE
					participants
				SET
					%s
				WHERE
					user_id = '%s'
			"""

			update_strings = []
			if first_name is not None:
				update_strings.append(f"first_name = '{attributes['first_name']}'")

			if last_name is not None:
				update_strings.append(f"last_name = '{attributes['last_name']}'")

			if email is not None:
				update_strings.append(f"email = '{attributes['email']}'")

			if len(update_strings):
				sql = sql % (', '.join(update_strings), username)
				self._connector.execute(sql)

			response.status_code = 200
			response.add_header("Content-Type", "application/json")
			response.body = json.dumps({ })
		except (user_exceptions.ParticipantDoesNotExistException) as e:
			response.status_code = 500
			response.add_header("Content-Type", "application/json")
			response.body = json.dumps({ "error": str(e), "exception": e.__class__.__name__ })
		except Exception as e:
			response.status_code = 500
			response.add_header("Content-Type", "application/json")
			response.body = json.dumps({ "error": "Internal Server Error: %s" % str(e), "exception": e.__class__.__name__ })

		return response

	def remove_participant_by_username(self, username, *args, **kwargs):
		"""
		Remove a participant that has the given username.

		:param username: The user's username.
		:type username: str

		:return: A response with any errors that may arise.
		:rtype: :class:`oauth2.web.Response`
		"""

		response = Response()

		try:
			username = self._sanitize(username)
			if not self._participant_exists(username):
				raise user_exceptions.ParticipantDoesNotExistException()

			self._connector.execute([
				"""
				DELETE FROM
					users
				WHERE
					user_id = '%s' AND
					role = 'PARTICIPANT';""" % (username),
			])

			"""
			Remove the participant from the backups.
			"""
			if erasure.script and erasure.backups:
				bashCommand = f"{erasure.script} -p {erasure.backups} {username}"
				print(f"Running: {bashCommand}", file=sys.stderr)
				process = subprocess.call(bashCommand, shell=True, stdout=subprocess.PIPE)

			response.status_code = 200
			response.add_header("Content-Type", "application/json")
			response.body = json.dumps({ })
		except (general_exceptions.InputException,
				user_exceptions.ParticipantDoesNotExistException) as e:
			response.status_code = 500
			response.add_header("Content-Type", "application/json")
			response.body = json.dumps({ "error": str(e), "exception": e.__class__.__name__ })
		except Exception as e:
			response.status_code = 500
			response.add_header("Content-Type", "application/json")
			response.body = json.dumps({ "error": "Internal Server Error: %s" % str(e), "exception": e.__class__.__name__ })

		return response

	def get_participant(self, username=None, *args, **kwargs):
		"""
		Filter participants using the given arguments.
		If no arguments are given, all participants are returned.

		:param username: The user's username.
		:type username: str

		:return: A response with any errors that may arise.
		:rtype: :class:`oauth2.web.Response`
		"""

		username = self._sanitize(username) if username is not None else username

		if username is None:
			rows = self._connector.select("""
				SELECT
					*
				FROM
					participants
			""")

			total = self._connector.count("""
				SELECT
					COUNT(*)
				FROM
					participants
			""")
		else:
			rows = self._connector.select("""
				SELECT
					*
				FROM
					participants
				WHERE
					user_id = '%s'
			""" % username)

			total = self._connector.count("""
				SELECT
					COUNT(*)
				FROM
					participants
				WHERE
					user_id = '%s'
			""")

		decrypted_data = [ self._decrypt_participant(row) for row in rows ]

		response = Response()
		response.status_code = 200
		response.add_header("Content-Type", "application/json")
		response.body = json.dumps({ "data": decrypted_data, "total": total })
		return response
