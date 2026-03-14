from flask import Flask
from pytest_bdd import scenario

from pytest_bdd import (
given,
when,
then,
scenarios
)

@given(u'User enters the authorization page')
def user_is_on_login_page():
    """Пользователь заходит на страницу авторизации"""
    pass

@when(u'User enters his username and password')
def user_enters_his_username_and_password():
    """Пользователь вводит свой логин и пароль"""
    pass

@when(u'User clicks submit button')
def user_clicks_submit_button():
    """Пользователь нажимает кнопку отправить"""
    pass

@then(u'User was logged in and redirected to the main page')
def user_is_logged_in():
    """Пользователь авторизовался и переходит на главную страницу"""
    pass

@scenario('../features/login.feature', "Enter in app")
def test_enter_in_app():
    """ход в приложение"""
    pass
