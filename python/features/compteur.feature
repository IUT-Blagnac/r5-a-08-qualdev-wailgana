Feature: Click Counter Application

  Scenario: User clicks the "Click me!" button once
    Given I have opened the Click Counter application
    When I click the "Click me!" button
    Then the click count should be 1
    And the double click count should be 0

  Scenario: User clicks the "Click me!" button multiple times
    Given I have opened the Click Counter application
    When I click the "Click me!" button 3 times
    Then the click count should be 3
    And the double click count should be 0

  Scenario: User clicks the "Double Click here!" button once
    Given I have opened the Click Counter application
    When I click the "Double Click here!" button
    Then the click count should be 2
    And the double click count should be 1

  Scenario: User clicks both buttons once
    Given I have opened the Click Counter application
    When I click the "Click me!" button
    And I click the "Double Click here!" button
    Then the click count should be 3
    And the double click count should be 1

  Scenario: User clicks the "Double Click here!" button twice
    Given I have opened the Click Counter application
    When I click the "Double Click here!" button twice
    Then the click count should be 4
    And the double click count should be 2
