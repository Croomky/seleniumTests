Feature: Dynamic Data Loading

    Scenario: user opens dynamic data loading page and clicks get new user
    Given user is on the dynamic data loading testing page
    When user clicks get new user button
    Then new user is loaded
