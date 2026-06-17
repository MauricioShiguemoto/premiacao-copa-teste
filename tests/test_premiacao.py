import time
from selenium.webdriver.common.by import By

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

def test_deve_exibir_premiacao_para_primeiro_lugar(driver_visivel):
    # Arrange
    colocacao = "1"
    premiacao_esperada = "US$ 50 milhões"

    driver_visivel.get(URL_BASE)
    campo = driver_visivel.find_element(By.ID, "colocacao")
    botao = driver_visivel.find_element(By.ID, "btn-calcular")

    # Act
    campo.clear()
    campo.send_keys(colocacao)
    time.sleep(1)
    botao.click()
    time.sleep(1)

    # Assert
    premiacao = driver_visivel.find_element(By.ID, "premiacao")
    assert premiacao.text == premiacao_esperada