from selenium import webdriver


URL_BASE = "https://marceloterencianiifpr.github.io/premiacao-copa/"

def test_ambiente():
    assert True


def test_deve_exibir_titulo_da_pagina():
    # Arrange
    driver = webdriver.Chrome()
    titulo_esperado = "Premiação da Copa do Mundo"


    try:
        # Act
        driver.get(URL_BASE)

        # Assert
        assert driver.title == titulo_esperado
    finally:
        driver.quit()