Feature: Play Saddam Game

Scenario: Load initial page
    Given load initial page
    Then show text "SADDAM"

Scenario: Load Game Page
    Given load game page
    Then show text "SADDAM"
    Then show text "Ingresar letra"
    Then show text "Palabra"

Scenario: Load Win Page
    Given load win page
    Then show text "WIN"

Scenario: Load Lose Page
    Given load lose page
    Then show text "LOSE"