import os

import django
from behave import fixture
from django.core import management
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase


@fixture
def django_test_runner(context):
    django.setup()
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()
    yield

    context.test_runner.teardown_databases(context.old_db_config)
    context.test_runner.teardown_test_environment()


@fixture
def django_test_case(context):
    context.test_case = LiveServerTestCase
    context.test_case.setUpClass()
    yield
    context.test_case.tearDownClass()
    del context.test_case


@fixture
def create_superuser(context):
    os.environ["DJANGO_SUPERUSER_PASSWORD"] = "randompassword"
    os.environ["DJANGO_SUPERUSER_USERNAME"] = "randomusernameadmin"
    management.call_command("createsuperuser", interactive=False, email="a@a.com")
