URL_BASE = "https://marceloterencianiifpr.github.io/premiacao-copa/"

def test_ambiente():
    assert True


def test_deve_exibir_titulo_da_pagina(driver_visivel):
    # Arrange
    titulo_esperado = "Premiação da Copa do Mundo"

    # Act
    driver_visivel.get(URL_BASE)

    # Assert
    assert driver_visivel.title == titulo_esperado