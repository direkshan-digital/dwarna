"""
Test the user schema.
"""

import sys
import os

from os.path import expanduser

path = sys.path[0]
path = os.path.join(path, "../")
if path not in sys.path:
	sys.path.insert(1, path)

import os
import psycopg2
import minimal_schema
import unittest

from .environment import *
from .models import *
from .test import SchemaTestCase

class UserTests(SchemaTestCase):
	"""
	Test the user schema.
	"""

	@SchemaTestCase.isolated_test
	def test_users(self):
		"""
		Test user data.
		"""

		participant = Participant("participant", "first", "last", "address")
		biobanker = Biobanker("biobanker")
		researcher = Researcher("researcher")

		"""
		The database should be empty by now
		"""
		self.assertFalse(self._connection.execute("""
			SELECT *
			FROM
				users"""))

		"""
		Therefore biobankers, researchers and participants cannot be inserted
		Each time, an ForeignKeyViolation should be raised because the ForeignKey constraint is not respected
		"""
		self.assert_fail_sql("""
			INSERT INTO
				biobankers (user_id)
			VALUES
				('%s');
			""" % biobanker.get_username(), "ForeignKeyViolation")
		self.assert_fail_sql("""
			INSERT INTO
				researchers (user_id)
			VALUES
				('%s');
		""" % researcher.get_username(), "ForeignKeyViolation")
		self.assert_fail_sql("""
			INSERT INTO
				participants (user_id, first_name, last_name, email)
			VALUES
				(%s);
		""" % participant.get_participant_insertion_string(), "ForeignKeyViolation")

	@SchemaTestCase.isolated_test
	def test_user_type_enumeration(self):
		"""
		The user role is an enumeration, and it cannot be violated.
		This is incorrect data, hence the DataError violation.
		"""


		self.assert_fail_sql("""
			INSERT INTO
				users (user_id, role)
			VALUES
				('t_id', 'ADMIN');""", "InvalidTextRepresentation")

	@SchemaTestCase.isolated_test
	def test_inserting_duplicate_user(self):
		"""
		There may be no duplicate users.
		This forces an IntegrityError.
		"""

		participant = Participant("participant", "first", "last", "address")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % participant.get_user_insertion_string())

		self.assert_fail_sql("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % participant.get_user_insertion_string(), "UniqueViolation")

	@SchemaTestCase.isolated_test
	def test_inserting_duplicate_biobanker(self):
		"""
		Biobankers must be unique.
		Otherwise, an IntegrityError is raised.
		"""

		biobanker = Biobanker("biobanker")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % biobanker.get_user_insertion_string())
		self._connection.execute("""
			INSERT INTO
				biobankers (user_id)
			VALUES
				('%s');
		""" % biobanker.get_username())
		self.assert_fail_sql("""
			INSERT INTO
				biobankers (user_id)
			VALUES
				('%s');
		""" % biobanker.get_username(), "UniqueViolation")

	@SchemaTestCase.isolated_test
	def test_inserting_duplicate_researcher(self):
		"""
		Researchers must be unique.
		Otherwise, an IntegrityError is raised.
		"""

		researcher = Researcher("researcher")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % researcher.get_user_insertion_string())
		self._connection.execute("""
			INSERT INTO
				researchers (user_id)
			VALUES
				('%s');
		""" % researcher.get_username())
		self.assert_fail_sql("""
			INSERT INTO
				researchers (user_id)
			VALUES
				('%s');
		""" % researcher.get_username(), "UniqueViolation")

	@SchemaTestCase.isolated_test
	def test_inserting_duplicate_participant(self):
		"""
		Participants must be unique.
		Otherwise, an IntegrityError is raised.
		"""

		participant = Participant("participant", "first", "last", "address")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % participant.get_user_insertion_string())
		self._connection.execute("""
			INSERT INTO
				participants (user_id, first_name, last_name, email)
			VALUES
				(%s);
		""" % participant.get_participant_insertion_string())
		self.assert_fail_sql("""
			INSERT INTO
				participants (user_id, first_name, last_name, email)
			VALUES
				(%s);
		""" % participant.get_participant_insertion_string(), "UniqueViolation")

	@SchemaTestCase.isolated_test
	def test_insert_user(self):
		"""
		Insert a single user into the database.
		"""

		participant = Participant("participant", "first", "last", "address")

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				users"""))

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % participant.get_user_insertion_string())

		self.assertEqual(self._connection.count("""
			SELECT COUNT(*)
			FROM
				users"""), 1)

	@SchemaTestCase.isolated_test
	def test_delete_user(self):
		"""
		Delete a user from the database.
		"""

		participant = Participant("participant", "first", "last", "address")

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				users"""))

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % participant.get_user_insertion_string())

		self.assertEqual(self._connection.count("""
			SELECT COUNT(*)
			FROM
				users"""), 1)

		self._connection.execute("""
			DELETE FROM
				users
			WHERE
				user_id = '%s'
		""" % participant.get_username())

		self.assertEqual(self._connection.count("""
			SELECT COUNT(*)
			FROM
				users"""), 0)

	@SchemaTestCase.isolated_test
	def test_delete_all_users(self):
		"""
		Delete all users from the database.
		"""

		participant = Participant("participant", "first", "last", "address")

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				users"""))

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % participant.get_user_insertion_string())

		self.assertEqual(self._connection.count("""
			SELECT COUNT(*)
			FROM
				users"""), 1)

		self._connection.execute("""
			DELETE FROM
				users
			WHERE TRUE;
		""")

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				users"""))

	@SchemaTestCase.isolated_test
	def test_insert_biobanker(self):
		"""
		Insert a biobanker into the database.
		"""

		biobanker = Biobanker("biobanker")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % biobanker.get_user_insertion_string())

		self._connection.execute("""
			INSERT INTO
				biobankers (user_id)
			VALUES
				('%s');
		""" % biobanker.get_username())

		self.assertEqual(self._connection.count("""
			SELECT COUNT(*)
			FROM
				users, biobankers
			WHERE
				users.user_id = biobankers.user_id"""), 1)

	@SchemaTestCase.isolated_test
	def test_remove_biobanker_from_users(self):
		"""
		Remove a biobanker from the users table.
		The user should also be removed from the biobankers table at the same time.
		"""

		biobanker = Biobanker("biobanker")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % biobanker.get_user_insertion_string())

		self._connection.execute("""
			INSERT INTO
				biobankers (user_id)
			VALUES
				('%s');
		""" % biobanker.get_username())

		self._connection.execute("""
			DELETE FROM
				users
			WHERE
				user_id = '%s'""" % biobanker.get_username())

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				biobankers"""))

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				users"""))

	@SchemaTestCase.isolated_test
	def test_remove_biobanker_from_biobankers(self):
		"""
		Remove a biobanker from the biobankers table.
		The user should also be removed from the users table at the same time.
		"""

		biobanker = Biobanker("biobanker")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % biobanker.get_user_insertion_string())

		self._connection.execute("""
			INSERT INTO
				biobankers (user_id)
			VALUES
				('%s');
		""" % biobanker.get_username())

		self.assertEqual(self._connection.count("""
			SELECT COUNT(*)
			FROM
				users, biobankers
			WHERE
				users.user_id = biobankers.user_id"""), 1)

		self._connection.execute("""
			DELETE FROM
				biobankers
			WHERE
				user_id = '%s'
		""" % biobanker.get_username())

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				biobankers"""))

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				users"""))

	@SchemaTestCase.isolated_test
	def test_insert_researcher(self):
		"""
		Insert a researcher into the database.
		"""

		researcher = Researcher("researcher")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % researcher.get_user_insertion_string())

		self._connection.execute("""
			INSERT INTO
				researchers (user_id)
			VALUES
				('%s');
		""" % researcher.get_username())

		self.assertEqual(self._connection.count("""
			SELECT COUNT(*)
			FROM
				users, researchers
			WHERE
				users.user_id = researchers.user_id"""), 1)

	@SchemaTestCase.isolated_test
	def test_remove_researcher_from_users(self):
		"""
		Remove a researcher from the users table.
		The user should also be removed from the researchers table at the same time.
		"""

		researcher = Researcher("researcher")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % researcher.get_user_insertion_string())

		self._connection.execute("""
			INSERT INTO
				researchers (user_id)
			VALUES
				('%s');
		""" % researcher.get_username())

		self._connection.execute("""
			DELETE FROM
				users
			WHERE
				user_id = '%s'""" % researcher.get_username())

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				researchers"""))

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				users"""))

	@SchemaTestCase.isolated_test
	def test_remove_researcher_from_researchers(self):
		"""
		Remove a researcher from the researchers table.
		The user should also be removed from the users table at the same time.
		"""

		researcher = Researcher("researcher")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % researcher.get_user_insertion_string())

		self._connection.execute("""
			INSERT INTO
				researchers (user_id)
			VALUES
				('%s');
		""" % researcher.get_username())

		self.assertEqual(self._connection.count("""
			SELECT COUNT(*)
			FROM
				users, researchers
			WHERE
				users.user_id = researchers.user_id"""), 1)

		self._connection.execute("""
			DELETE FROM
				researchers
			WHERE
				user_id = '%s'
		""" % researcher.get_username())

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				researchers"""))

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				users"""))

	@SchemaTestCase.isolated_test
	def test_insert_participant(self):
		"""
		Insert a participant into the database.
		"""

		participant = Participant("participant", "first", "last", "address")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % participant.get_user_insertion_string())

		self._connection.execute("""
			INSERT INTO
				participants (user_id, first_name, last_name, email)
			VALUES
				(%s);
		""" % participant.get_participant_insertion_string())

		self.assertEqual(self._connection.count("""
			SELECT COUNT(*)
			FROM
				users, participants
			WHERE
				users.user_id = participants.user_id"""), 1)

	@SchemaTestCase.isolated_test
	def test_remove_participant_from_users(self):
		"""
		Remove a participant from the users table.
		The user should also be removed from the participants table at the same time.
		"""

		participant = Participant("participant", "first", "last", "address")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % participant.get_user_insertion_string())

		self._connection.execute("""
			INSERT INTO
				participants (user_id, first_name, last_name, email)
			VALUES
				(%s);
		""" % participant.get_participant_insertion_string())

		self._connection.execute("""
			DELETE FROM
				users
			WHERE
				user_id = '%s'""" % participant.get_username())

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				participants"""))

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				users"""))

	@SchemaTestCase.isolated_test
	def test_remove_participant_from_participants(self):
		"""
		Remove a participant from the participants table.
		The user should also be removed from the users table at the same time.
		"""

		participant = Participant("participant", "first", "last", "address")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % participant.get_user_insertion_string())

		self._connection.execute("""
			INSERT INTO
				participants (user_id, first_name, last_name, email)
			VALUES
				(%s);
		""" % participant.get_participant_insertion_string())

		self.assertEqual(self._connection.count("""
			SELECT COUNT(*)
			FROM
				users, participants
			WHERE
				users.user_id = participants.user_id"""), 1)

		self._connection.execute("""
			DELETE FROM
				participants
			WHERE
				user_id = '%s'
		""" % participant.get_username())

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				participants"""))

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				users"""))

	@SchemaTestCase.isolated_test
	def test_remove_participant_cascades_to_identities(self):
		"""
		Remove a participant from the participants table.
		The participant's identities should also be removed.
		"""

		participant = Participant("participant", "first", "last", "address")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % participant.get_user_insertion_string())

		self._connection.execute("""
			INSERT INTO
				participants (user_id, first_name, last_name, email)
			VALUES
				(%s);
		""" % participant.get_participant_insertion_string())

		self.assertEqual(self._connection.count("""
			SELECT COUNT(*)
			FROM
				users, participants
			WHERE
				users.user_id = participants.user_id"""), 1)

		self._connection.execute("""
			INSERT INTO
				participant_identities (participant_id, address)
			VALUES
				('%s', '%s');
		""" % (participant._username, 't' + participant._username))

		self.assertEqual(self._connection.count("""
			SELECT COUNT(*)
			FROM
				participant_identities
			WHERE
				participant_identities.participant_id= '%s'""" % (
				participant._username
		)), 1)

		self._connection.execute("""
			DELETE FROM
				participants
			WHERE
				user_id = '%s'
		""" % participant.get_username())

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				participant_identities
			WHERE
				participant_id = '%s'""" % (
				participant._username
		)))

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				participants"""))

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				users"""))

	@SchemaTestCase.isolated_test
	def test_remove_participant_cascades_to_subscriptions(self):
		"""
		Remove a participant from the participants table.
		The participant's subscriptions should also be removed.
		"""

		participant = Participant("participant", "first", "last", "address")

		self._connection.execute("""
			INSERT INTO
				users (user_id, role)
			VALUES
				(%s);
		""" % participant.get_user_insertion_string())

		self._connection.execute("""
			INSERT INTO
				participants (user_id, first_name, last_name, email)
			VALUES
				(%s);
		""" % participant.get_participant_insertion_string())

		self.assertEqual(self._connection.count("""
			SELECT COUNT(*)
			FROM
				users, participants
			WHERE
				users.user_id = participants.user_id"""), 1)

		self._connection.execute("""
			INSERT INTO
				participant_subscriptions (participant_id)
			VALUES
				('%s');
		""" % (participant._username))

		self.assertEqual(self._connection.count("""
			SELECT COUNT(*)
			FROM
				participant_subscriptions
			WHERE
				participant_subscriptions.participant_id= '%s'""" % (
				participant._username
		)), 1)

		self._connection.execute("""
			DELETE FROM
				participants
			WHERE
				user_id = '%s'
		""" % participant.get_username())

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				participant_subscriptions
			WHERE
				participant_id = '%s'""" % (
				participant._username
		)))

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				participants"""))

		self.assertFalse(self._connection.exists("""
			SELECT *
			FROM
				users"""))
