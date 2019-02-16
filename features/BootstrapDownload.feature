Feature: bootstrap download bar

    Scenario: download a file
    Given we're on the bootstrap download testing page
    When we click on download button
    Then percents are incrementing