Feature: Play Saddam Game

Scenario: Load initial page
    Given load initial page
    Then show title message

Scenario: Load Game Page
    Given load game page
    Then show title message
    Then show input letter
    Then show word