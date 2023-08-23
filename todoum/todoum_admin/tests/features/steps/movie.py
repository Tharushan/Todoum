from behave import then, when


@when('I press "Movies" link')
def step_movies_link(context):
    context.page.click("text=Movies")


@then('I should see "Add Movie" button')
def step_movies_page(context):
    context.page.wait_for_selector("text=Add Movie")
    assert context.page.get_by_text("Add Movie").is_visible()


@when('I press "Add Movie" button')
def step_add_movie_button(context):
    context.page.click("text=Add Movie")


@when('I press "Save" button')
def step_save_button(context):
    context.page.click("[name='_save']")


@then("I should see success message")
def step_success_message(context):
    context.page.wait_for_selector(".success")
    assert len(context.page.eval_on_selector(".success", "el => el.innerText")) > 0


@then('I should see "{movie_title}" in the list')
def step_movie_in_list(context, movie_title):
    context.page.wait_for_selector(f"text={movie_title}")
    assert context.page.get_by_text(movie_title).is_visible()
