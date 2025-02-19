from django.conf import settings
from django.test import TestCase, override_settings

"""
This demonstrates how override_settings as a decorator is broken.
After using it once it will leak it's new settings into other tests
"""


@override_settings(FOO="bar")
class TestOverrideSettingsDecorator(TestCase):
    def test_foo_is_bar(self):
        self.assertEqual(settings.FOO, "bar")


class TestOverrideSettingsContextManager(TestCase):
    def test_foo_is_foo(self):
        self.assertEqual(settings.FOO, "bar")
