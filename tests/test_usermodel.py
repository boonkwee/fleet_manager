from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):
    """Test user models"""

    def test_create_user_ok(self):
        email = 'test@example.com'
        password = 'somepass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))