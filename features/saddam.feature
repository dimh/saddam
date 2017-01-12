Feature: Play Saddam Game

Scenario: Load initial page
    Given load page: "http://localhost:5000"
    Then show text "SADDAM"

Scenario: validar letra en la palabra
    Given Juego Iniciado
        AND la palaabra SEXY
    When ingresa la letra X
    Then retorna la palabra **X*

Scenario: iniciar el juego
    Given la palabra secreta SEXY
    Then retorna la palabra ****

Scenario: validar letra en la palabra 2
    Given Juego Iniciado
        AND la palaabra SEXY
    When ingresa la letra H
    Then retorna la palabra ****

Scenario: Load Game Page
    Given load page: "http://localhost:5000/play"
    Then show text "SADDAM"
    Then show text "Ingresar letra"
    Then show text "Palabra"

Scenario: Load Win Page
    Given load page: "http://localhost:5000/win"
    Then show text "WIN"

Scenario: Load Lose Page
    Given load page: "http://localhost:5000/lose"
    Then show text "LOSE"