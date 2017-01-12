from saddam import *
from behave import *
from splinter import Browser
browser = Browser('flask', app=app)

@given(u'load game')
def step_impl(context):
    browser.visit('http://localhost:5000')

@then(u'show initial message')
def step_impl(context):
    assert "SADDAM" in browser.html, browser.html