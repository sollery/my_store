# from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

#
#
# class CustomUserTests(TestCase):
#     def test_create_user(self):
#         User = get_user_model()
#         user = User.objects.create_user(
#                                         username='ilya', email='ilya@mail.ru', password='test1111')
#         self.assertEqual(user.username, 'ilya')
#         self.assertEqual(user.email, 'ilya@mail.ru')
#         self.assertTrue(user.is_active)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_superuser)

    # def test_create_superuser(self):
    #     User = get_user_model()
    #     admin_user = User.objects.create_superuser(username='admin_ilya', email='admin@email.com', password='test1111')
    #     self.assertEqual(admin_user.username, 'admin_ilya')
    #     self.assertEqual(admin_user.email, 'admin@email.com')
    #     self.assertTrue(admin_user.is_active)
    #     self.assertTrue(admin_user.is_staff)
    #     self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase): # new

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response,'account/signup.html')
        self.assertContains(self.response,'Регистрация')
        self.assertNotContains(self.response,'Регистрацияяя')