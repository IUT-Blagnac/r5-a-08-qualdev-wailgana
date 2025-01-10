from behave import given, when, then
import tkinter as tk
from maincompteur import ClickCounterApp

@given('I have opened the Click Counter application')
def step_given_open_application(context):
    context.root = tk.Tk()
    context.app = ClickCounterApp(context.root)

@when('I click the "Click me!" button')
def step_when_click_button(context):
    context.app.increment_count()

@when('I click the "Click me!" button {times:d} times')
def step_when_click_button_multiple_times(context, times):
    for _ in range(times):
        context.app.increment_count()

@when('I click the "Double Click here!" button')
def step_when_double_click_button(context):
    context.app.add_double_clicks()

@when('I click the "Double Click here!" button twice')
def step_when_double_click_button_multiple_times(context):
    for _ in range(2):
        context.app.add_double_clicks()

@when('I click the "Click me!" button and I click the "Double Click here!" button')
def step_when_click_both_buttons(context):
    context.app.increment_count()
    context.app.add_double_clicks()

@then('the click count should be {expected_count:d}')
def step_then_check_click_count(context, expected_count):
    assert context.app.click_count == expected_count, f"Expected {expected_count}, but got {context.app.click_count}"

@then('the double click count should be {expected_count:d}')
def step_then_check_double_click_count(context, expected_count):
    assert context.app.double_click_count == expected_count, f"Expected {expected_count}, but got {context.app.double_click_count}"
