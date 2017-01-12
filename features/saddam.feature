Feature: Play Saddam Game

Scenario: Load initial page
    Given load game
    Then show initial message

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
    Given load game page
    Then show title message
    Then show input letter
    Then show word