Feature: Login on SauceDemo website
    As a user
    I want to log in to the system
    In order to access the product catalog

Scenario: Successful login with valid credentials
    Given I open the login page
    When I enter username "standard_user"
    And I enter password "secret_sauce"
    And I click the "Login" button
    Then I am redirected to the inventory page

Scenario: Error message with invalid credentials
    Given I open the login page
    When I enter username "invalid_user"
    And I enter password "invalid_pass"
    And I click the "Login" button
    Then I see an error message