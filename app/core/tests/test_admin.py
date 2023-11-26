"""
Test for the Django admin modifications.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Test admin site."""

    def setUp(self):
        """Create user and client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@example.com',
            password = 'testpass123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'user@example.com',
            password = 'testpass123',
            name = 'Test user full name',
        )
    def test_users_list(self):
        """Test that users are listed on user page."""
        # Generate the URL for the list user page
        url = reverse('admin:core_user_changelist')
        # Perform an HTTP GET on the URL
        res = self.client.get(url)
        # Check that the response contains the user
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works."""
        # Generate the URL for the edit user page
        url = reverse('admin:core_user_change', args=[self.user.id])
        # Perform an HTTP GET on the URL
        res = self.client.get(url)
        # Check that the response is OK
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works."""
        # Generate the URL for the create user page
        url = reverse('admin:core_user_add')
        # Perform an HTTP GET on the URL
        res = self.client.get(url)
        # Check that the response is OK
        self.assertEqual(res.status_code, 200)
