from saddam import *
from behave import *
from splinter import Browser
browser = Browser('flask', app=app)

@then(u'show text "{text}"')
def step_impl(context, text):
    assert text in browser.html, browser.html

@given(u'load page: "{page}"')
def step_impl(context, page):
    browser.visit(page)    