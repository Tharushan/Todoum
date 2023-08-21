import os

from behave import use_fixture
from fixtures import create_superuser, django_test_case, django_test_runner
from playwright.sync_api import sync_playwright

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.test"
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


def before_scenario(context, scenario):
    use_fixture(django_test_case, context)


def before_all(context):
    use_fixture(django_test_runner, context)
    use_fixture(create_superuser, context)
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch()


def after_all(context):
    context.browser.close()
    context.playwright.stop()
