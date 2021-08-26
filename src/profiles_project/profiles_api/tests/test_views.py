from .test_setup import TestSetUp
from ..models import UserProfile

class TestViews(TestSetUp):

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_with_complete_data(self):
        res = self.client.post(self.register_url, self.user_data)
        self.assertEqual(res.data['email'], self.user_data['email'])
        self.assertEqual(res.data['name'], self.user_data['name'])
        self.assertEqual(res.status_code, 201)

    def test_unregistered_user_cannot_login(self):
        res = self.client.post(self.login_url, self.user_data)
        self.assertEqual(res.status_code, 400)

    def test_registered_user_can_login(self):
        self.client.post(self.register_url, self.user_data)
        login_data = {'username':self.user_data['email'], 'password':self.user_data['password']}
        res = self.client.post(self.login_url, login_data)
        self.assertEqual(res.status_code, 200)

    def test_unauthenticated_user_cannot_check_feed(self):
        res = self.client.get(self.feed_url)
        self.assertEqual(res.status_code, 401)

    def test_authenticated_user_can_check_feed(self):
        token = self.login(self.user_data)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        user = UserProfile.objects.get(email=self.user_data['email'])
        res = self.client.get(self.feed_url)
        self.assertEqual(res.status_code, 200)

    def test_unauthenticated_user_cannot_post_on_feed(self):
        res = self.client.post(self.feed_url)
        self.assertEqual(res.status_code, 401)

    def test_authenticated_user_can_post_on_feed(self):
        token = self.login(self.user_data)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        user = UserProfile.objects.get(email=self.user_data['email'])
        res = self.client.post(self.feed_url, {'user_profile': user, 'status_text': 'sample_msg'})
        self.assertEqual(res.status_code, 201)