Feature: Ajax form

    Scenario: user open ajax form demo page and clicks submit
    Given user is on the ajax form testing page
    When user enters nothing and clicks submit
    Then name field has red outline

    Scenario: user open ajax form demo page and enters some data
    Given user is on the ajax form testing page
    When user enters data and clicks submit
    Then ajax is processing info