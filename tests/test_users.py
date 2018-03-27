import unittest

from flask import request
from flask_login import current_user

from base import BaseTestCase
from project import bcrypt
from project.models import User

'''
flask-login: https://flask-login.readthedocs.io/en/latest/
unittest : https://docs.python.org/2/library/unittest.html
flask-bcrypt: https://flask-bcrypt.readthedocs.io/en/latest/
'''

class TestUser(BaseTestCase):

	# Ensure user can register
	def test_user_registeration(self):
		with self.client:
			response = self.client.post('register/', data=dict(
				username='admin', email='admin@mail.com',
				password='adminpass', confirm='adminpass'
				), follow_redirects=True)
			self.assertIn(b'Welcome to Flask Posts System!', response.data)
			self.assertTrue(current_user.name == "admin")
			self.assertTrue(current_user.is_authenticated())
			self.assertTrue(current_user.is_active())
			self.assertFalse(current_user.is_anonymous())
			user = User.query.filter_by(email= 'admin@mail.com').first()
			self.assertTrue(str(user) == '<name - admin>')

	# Ensure errors are thrown during an incorrect user registration
	def test_incorrect_user_registeration(self):
		with self.client:
			response = self.client.post('register/', data=dict(
				username='admin', email='admin',
				password='adminpass', confirm='adminpass'
			), follow_redirects=True)
			self.assertIn(b'Invalid email address.', response.data)
			self.assertIn(b'/register/', request.url)
	
	def test_get_by_id(self):
		# Ensure id is correct for the current/logged in user
		with self.client:
			self.client.post('/login', data=dict(
				username="admin", password='adminpass'
			), follow_redirects=True)
			self.assertTrue(current_user.id == 1)

	def test_check_password(self):
		# Ensure given password is correct after unhashing
		user = User.query.filter_by(email='admin@mail.com').first()
		self.assertTrue(bcrypt.check_password_hash(user.password, 'adminpass'))


class UserViewsTests(BaseTestCase):

	# Ensure that the login page loads correctly
	def test_login_page_loads(self):
		response = self.client.get('/login', content_type='html/text')
		self.assertIn(b'Please login', response.data)

	# Ensure login behaves correctly with correct credentials
	def test_correct_login(self):
		with self.client:
			response = self.client.post(
				'/login',
				data=dict(username="admin", password="adminpass"),
				follow_redirects=True
				)
			self.assertIn(b'You were just logged in!', response.data)
			self.assertTrue(current_user.name == "admin")
			self.assertTrue(current_user.is_active())

	# Ensure login behaves correctly with incorrect credentials
	def test_incorrect_login(self):
		response = self.client.post(
			'/login',
			data=dict(username="wrong", password="wrong"),
			follow_redirects=True
			)
		self.assertIn(b'Invalid credentials. Please try again.', response.data)

	# Ensure logout behaves correctly
	def test_logout(self):
		with self.client:
			self.client.post(
				'/login',
				data=dict(username="admin", password="adminpass"),
				follow_redirects=True
				)
			response = self.client.get('/logout', follow_redirects=True)
			self.assertIn(b'You were just logged out!', response.data)

	# Ensure that logout page requires user login
	def test_logout_route_requires_login(self):
		response = self.client.get('/logout', follow_redirects=True)
		self.assertIn(b'Please log in to access this page', response.data)


if __name__ == '__main__':
	unittest.main()


