from behave import given, then, when


@given("I am on the login page")
def step_page(context):
    context.page = context.browser.new_page()
    context.page.goto(f"{context.test_case.live_server_url}/admin/login")
    context.page.wait_for_selector("input[name='username']")


@when('I fill in "{field}" with "{value}"')
def step_input_fill(context, field, value):
    context.page.fill(f"input[name='{field}']", value)


@when('I press "{button}"')
def step_button_press(context, button):
    context.page.click(f"text={button}")


@then("I should see errors on the page")
def step_login_errors(context):
    context.page.wait_for_selector(".errornote")

    assert len(context.page.eval_on_selector(".errornote", "el => el.innerText")) > 0


@then('I should see "Todoum Admin" section')
def step_admin_page(context):
    assert context.page.url == f"{context.test_case.live_server_url}/admin/"
    assert context.page.get_by_text("Todoum Admin").is_visible()
