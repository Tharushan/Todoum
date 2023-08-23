Feature: Movie

Scenario: Access Movie Page
    Given I am on the login page
    And I am authenticated
    When I press "Movies" link
    Then I should see "Add Movie" button

Scenario: Add Movie
    Given I am on the login page
    And I am authenticated
    When I press "Movies" link
    And I press "Add Movie" button
    And I fill in "name" with "Fight Club"
    And I press "Save" button
    Then I should see success message
    And I should see "Fight Club" in the list
