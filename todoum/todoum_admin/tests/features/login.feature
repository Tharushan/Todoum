Feature: Login

Scenario: Login with wrong credentials
    Given I am on the login page
    When I fill in "username" with "wrong"
    And I fill in "password" with "wrong"
    And I press "Log in"
    Then I should see errors on the page

Scenario: Login with correct credentials
    Given I am on the login page
    When I fill in "username" with "randomusernameadmin"
    And I fill in "password" with "randompassword"
    And I press "Log in"
    Then I should see "Todoum Admin" section
