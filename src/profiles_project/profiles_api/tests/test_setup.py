from rest_framework.test import APITestCase
from django.urls import reverse
# from django.views import reverse_action

class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('profile-list')
        self.login_url = reverse('login-list')
        self.feed_url = reverse('feed-list')

        self.user_data = {
            'email': 'test@mail.com',
            'name': 'testUser',
            'password': 'test123'
        }

        return super().setUp()

    def login(self, user_data):
        self.client.post(self.register_url, user_data)
        login_data = {'username':user_data['email'], 'password':user_data['password']}
        res = self.client.post(self.login_url, login_data)
        return res.data['token']

    def tearDown(self):
        return super().tearDown()
