from saddam import *
from behave import *
from splinter import Browser
browser = Browser('flask', app=app)

@given(u'load initial page')
def step_impl(context):
    browser.visit('http://localhost:5000')

@given(u'load game page')
def step_impl(context):
    browser.visit('http://localhost:5000/play')

@then(u'show text "{text}"')
def step_impl(context, text):
    assert text in browser.html, browser.html

@given(u'load win page')
def step_impl(context):
    browser.visit('http://localhost:5000/win')

@given(u'load lose page')
def step_impl(context):
    browser.visit('http://localhost:5000/lose')