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

@then(u'show title message')
def step_impl(context):
    assert "SADDAM" in browser.html, browser.html

@then(u'show input letter')
def step_impl(context):
    assert "Ingresar letra" in browser.html, browser.html

@then(u'show word')
def step_impl(context):
    assert "Palabra" in browser.html, browser.html