Feature: User login
  Scenario: User enter app
    Given User enters the authorization page
    When User enters his username and password
    And Click button submit
    Then User was logged in and redirected to the main page


# pip install pytest pytest-bdd pytest-playwright - НЕОБХОДИМЫЕ БИБЛИОТЕКИ
# pytest  --generate-missing --feature login.feature  - КОД ГЕНЕРАЦИИ СЦЕНАРИЯ
