Feature: Basic Checkbox

    Scenario: user opens basic checkbox testing page and clicks
        on checkboxes
    Given user is on the basic checkbox testing page
    When user selects and unselects single checkbox
    Then success message appears and disappears

    Scenario: user opens basic checkbox testing page and clicks
        on checkboxes
    Given user is on the basic checkbox testing page
    When user clicks on multiple checkboxes and unchecks them all
    Then checkboxes are checked and unchecked