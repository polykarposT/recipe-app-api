from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelsTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test createing a new user with email is successful"""
        email = 'test@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        email = "test@POLYKARPOS.com"
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test132')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@polykarpos.com',
            'test12345'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)