Feature: Play Saddam Game

Scenario: Load initial page
    Given load page: "http://localhost:5000"
    Then show text "SADDAM"

Scenario: Load Game Page
    Given load page: "http://localhost:5000/play"
    Then show text "SADDAM"
    Then show text "Puntaje"
    Then show text "Palabra"
    Then show text "Ingresar letra"
    

Scenario: Load Win Page
    Given load page: "http://localhost:5000/win"
    Then show text "WIN"

Scenario: Load Lose Page
    Given load page: "http://localhost:5000/lose"
    Then show text "LOSE"