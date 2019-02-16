Feature: Simple Form

    Scenario: user opens simple form page and enters some data
    Given user is on the simple form testing page
    When user enters data to the first form and clicks show message
    Then message is showed

    Scenario: user opens simple form page and enters some data
    Given user is on the simple form testing page
    When user enters data to the second form and clicks get total
    Then sum is showed