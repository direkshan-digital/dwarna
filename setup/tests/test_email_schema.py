"""
Test the email schema.
The tests in this class concern not only the `emails` table, but also the `email_recipients` relation.
"""

import os
import sys

from functools import wraps

path = sys.path[0]
path = os.path.join(path, "../")
if path not in sys.path:
	sys.path.insert(1, path)

import os
import psycopg2
import minimal_schema
import unittest

from datetime import datetime

from .environment import *
from .test import SchemaTestCase

class EmailTests(SchemaTestCase):
	"""
	Test the email schema.
	"""

	@classmethod
	def setUpClass(self):
		"""
		Set up the class to create the schema.
		"""

		super(EmailTests, self).setUpClass()

	def isolated_test(test):
		"""
		Perform the test in isolation.
		In essence, this means that the data is cleared from the database.
		Then, sample data is re-introduced.

		:param test: The test to perform.
		:type test: function
		"""

		@wraps(test)

		def wrapper(*args):
			"""
			The wrapper removes all data from the database.
			"""

			clear()
			self = args[0]
			test(*args)

		return wrapper

	@isolated_test
	def test_email_subject_character_set(self):
		"""
		Test that the character set of the email subject handles Maltese characters.
		"""

		subject = 'Ġanni żar lil Ċikku il-Ħamrun'

		self._connection.execute("""
			INSERT INTO
				emails(subject, body)
			VALUES
				('%s', '%s')
		""" % (
			subject, ''
		))

		stored_subject = self._connection.select_one("""
			SELECT
				subject
			FROM
				emails
			LIMIT 1
		""")
		self.assertEqual(subject, stored_subject['subject'])

	@isolated_test
	def test_email_body_character_set(self):
		"""
		Test that the character set of the email body handles Maltese characters.
		"""

		body = 'Ġanni żar lil Ċikku il-Ħamrun'

		self._connection.execute("""
			INSERT INTO
				emails(subject, body)
			VALUES
				('%s', '%s')
		""" % (
			'', body
		))

		stored_body = self._connection.select_one("""
			SELECT
				body
			FROM
				emails
			LIMIT 1
		""")
		self.assertEqual(body, stored_body['body'])

	@isolated_test
	def test_email_created_at(self):
		"""
		Test the `created_at` attribute of emails.
		"""

		subject = 'Ġanni żar lil Ċikku il-Ħamrun'

		current_time = datetime.now()
		self._connection.execute("""
			INSERT INTO
				emails(subject, body)
			VALUES
				('%s', '%s')
		""" % (
			subject, ''
		))

		email = self._connection.select_one("""
			SELECT
				created_at
			FROM
				emails
			LIMIT 1
		""")
		self.assertEqual(current_time.year, email['created_at'].year)
		self.assertEqual(current_time.month, email['created_at'].month)
		self.assertEqual(current_time.day, email['created_at'].day)
		self.assertEqual(current_time.hour, email['created_at'].hour)
		self.assertEqual(current_time.minute, email['created_at'].minute)

	@isolated_test
	def test_email_recipients_cascade_on_deletion(self):
		"""
		Test that removing an email also removes its recipients.
		"""

		"""
		Create an email and add a recipient to it.
		"""
		cursor = self._connection.execute("""
			INSERT INTO
				emails(subject, body)
			VALUES
				('%s', '%s')
			RETURNING
				id
		""" % (
			'', ''
		), with_cursor=True)
		id = cursor.fetchone()['id']
		cursor.close()

		self._connection.execute("""
			INSERT INTO
				email_recipients(email_id, recipient)
			VALUES
				('%d', 'test@email.com')
		""" % (
			id
		))

		"""
		Delete the email and ensure that the recipient has also been removed.
		"""
		self._connection.execute("""
			DELETE FROM
				emails
			WHERE
				id = %d
		""" % (
			id
		))

		self.assertFalse(self._connection.exists("""
			SELECT
				*
			FROM
				emails
			WHERE
				id = %d
		""" % (
			id
		)))

		self.assertFalse(self._connection.exists("""
			SELECT
				*
			FROM
				email_recipients
			WHERE
				email_id = %d
		""" % (
			id
		)))

	@isolated_test
	def test_email_recipient_deletion_does_not_cascade(self):
		"""
		Test that removing an email recipient does not remove the email itself.
		"""

		"""
		Create an email and add a recipient to it.
		"""
		cursor = self._connection.execute("""
			INSERT INTO
				emails(subject, body)
			VALUES
				('%s', '%s')
			RETURNING
				id
		""" % (
			'', ''
		), with_cursor=True)
		id = cursor.fetchone()['id']
		cursor.close()

		self._connection.execute("""
			INSERT INTO
				email_recipients(email_id, recipient)
			VALUES
				('%d', 'test@email.com')
		""" % (
			id
		))

		"""
		Delete the email recipient and ensure that the email is not removed.
		"""
		self._connection.execute("""
			DELETE FROM
				email_recipients
			WHERE
				email_id = %d
		""" % (
			id
		))

		self.assertTrue(self._connection.exists("""
			SELECT
				*
			FROM
				emails
			WHERE
				id = %d
		""" % (
			id
		)))

		self.assertFalse(self._connection.exists("""
			SELECT
				*
			FROM
				email_recipients
			WHERE
				email_id = %d
		""" % (
			id
		)))

	@isolated_test
	def test_default_sent_value(self):
		"""
		Test that by default, emails are not marked as sent.
		"""

		"""
		Create an email and add a recipient to it.
		"""
		cursor = self._connection.execute("""
			INSERT INTO
				emails(subject, body)
			VALUES
				('%s', '%s')
			RETURNING
				id
		""" % (
			'', ''
		), with_cursor=True)
		id = cursor.fetchone()['id']
		cursor.close()

		self._connection.execute("""
			INSERT INTO
				email_recipients(email_id, recipient)
			VALUES
				('%d', 'test@email.com')
		""" % (
			id
		))

		"""
		Assert that the email is not marked as sent.
		"""

		row = self._connection.select_one("""
			SELECT
				sent
			FROM
				email_recipients
			WHERE
				email_id = %d
		""" % (
			id
		))
		self.assertFalse(row['sent'])

	@isolated_test
	def test_duplicate_emails(self):
		"""
		Test that adding emails with duplicate IDs does not work.
		"""

		"""
		Create an email and add a recipient to it.
		"""
		cursor = self._connection.execute("""
			INSERT INTO
				emails(subject, body)
			VALUES
				('%s', '%s')
			RETURNING
				id
		""" % (
			'', ''
		), with_cursor=True)
		id = cursor.fetchone()['id']
		cursor.close()

		"""
		Assert that trying to create a new email with the same ID fails.
		"""

		"""
		Create an email and add a recipient to it.
		"""
		self.assert_fail_sql("""
			INSERT INTO
				emails(id, subject, body)
			VALUES
				(%d, '%s', '%s')
		""" % (
			id, '', ''
		), 'UniqueViolation')

	@isolated_test
	def test_duplicate_email_recipient(self):
		"""
		Test that a recipient can appear multiple times, but not for the same email.
		"""

		recipient = 'test@email.com'

		"""
		Create two emails and add the same recipient to them.
		"""
		cursor = self._connection.execute("""
			INSERT INTO
				emails(subject, body)
			VALUES
				('%s', '%s'),
				('%s', '%s')
			RETURNING
				id
		""" % (
			'', '', '', ''
		), with_cursor=True)
		rows = cursor.fetchall()
		ids = [ row['id'] for row in rows ]
		cursor.close()

		self._connection.execute("""
			INSERT INTO
				email_recipients(email_id, recipient)
			VALUES
				('%d', '%s'),
				('%d', '%s')
		""" % (
			ids[0], recipient, ids[1], recipient
		))

		"""
		Assert that the insertion worked.
		"""

		rows = self._connection.select("""
			SELECT
				email_id
			FROM
				email_recipients
			WHERE
				recipient = '%s'
			ORDER BY
				email_id ASC
		""" % (
			recipient
		))
		self.assertEqual(ids, [ row['email_id'] for row in rows ])

		"""
		Add the same recipient to the first email and assert that it fails.
		"""

		self.assert_fail_sql("""
			INSERT INTO
				email_recipients(email_id, recipient)
			VALUES
				('%d', '%s')
		""" % (
			ids[0], recipient
		), 'UniqueViolation')
