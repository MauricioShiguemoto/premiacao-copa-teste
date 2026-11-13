import time
from selenium.webdriver.common.by import By

URL_BASE = "https://marceloterencianiifpr.github.io/calculo-combustivel/"

def test_alto_consumo_limite_inferior(driver_visivel):
    # Arrange
    titulo_esperado = "Alto consumo"
    litros = 2
    distancia = 15.99

    # Act
    driver_visivel.get(URL_BASE)

    campo_litros = driver_visivel.find_element(By.ID, "litros")
    campo_litros.send_keys(litros)
    
    campo_distancia = driver_visivel.find_element(By.ID, "distancia")
    campo_distancia.send_keys(distancia)
    
    botao_calcular = driver_visivel.find_element(By.ID, "btn-calcular")
    botao_calcular.click()
    
    # campo_consumo = driver_visivel.find_element(By.ID, "consumo")
    campo_classificacao = driver_visivel.find_element(By.ID, "classificacao")
    
    # Assert
    assert campo_classificacao.text == titulo_esperado


def test_alto_consumo_limite_superior(driver_visivel):
    # Arrange
    titulo_esperado = "Consumo normal"
    litros = 2
    distancia = 16

    # Act
    driver_visivel.get(URL_BASE)

    campo_litros = driver_visivel.find_element(By.ID, "litros")
    campo_litros.send_keys(litros)

    campo_distancia = driver_visivel.find_element(By.ID, "distancia")
    campo_distancia.send_keys(distancia)

    botao_calcular = driver_visivel.find_element(By.ID, "btn-calcular")
    botao_calcular.click()

    # campo_consumo = driver_visivel.find_element(By.ID, "consumo")
    campo_classificacao = driver_visivel.find_element(By.ID, "classificacao")

    # Assert
    assert campo_classificacao.text == titulo_esperado


def test_consumo_normal_limite_inferior(driver_visivel):
    # Arrange
    titulo_esperado = "Consumo normal"
    litros = 2
    distancia = 24

    # Act
    driver_visivel.get(URL_BASE)

    campo_litros = driver_visivel.find_element(By.ID, "litros")
    campo_litros.send_keys(litros)

    campo_distancia = driver_visivel.find_element(By.ID, "distancia")
    campo_distancia.send_keys(distancia)

    botao_calcular = driver_visivel.find_element(By.ID, "btn-calcular")
    botao_calcular.click()

    # campo_consumo = driver_visivel.find_element(By.ID, "consumo")
    campo_classificacao = driver_visivel.find_element(By.ID, "classificacao")

    # Assert
    assert campo_classificacao.text == titulo_esperado


def test_consumo_normal_limite_superior(driver_visivel):
    # Arrange
    titulo_esperado = "Econômico"
    litros = 2
    distancia = 24.01

    # Act
    driver_visivel.get(URL_BASE)

    campo_litros = driver_visivel.find_element(By.ID, "litros")
    campo_litros.send_keys(litros)

    campo_distancia = driver_visivel.find_element(By.ID, "distancia")
    campo_distancia.send_keys(distancia)

    botao_calcular = driver_visivel.find_element(By.ID, "btn-calcular")
    botao_calcular.click()

    # campo_consumo = driver_visivel.find_element(By.ID, "consumo")
    campo_classificacao = driver_visivel.find_element(By.ID, "classificacao")

    # Assert
    assert campo_classificacao.text == titulo_esperado
 

def test_consumo_consumo_zero(driver_visivel):
    # Arrange
    titulo_esperado = "Inválido!"
    litros = 0
    distancia = 24.01

    # Act
    driver_visivel.get(URL_BASE)

    campo_litros = driver_visivel.find_element(By.ID, "litros")
    campo_litros.send_keys(litros)

    campo_distancia = driver_visivel.find_element(By.ID, "distancia")
    campo_distancia.send_keys(distancia)

    botao_calcular = driver_visivel.find_element(By.ID, "btn-calcular")
    botao_calcular.click()

    campo_consumo = driver_visivel.find_element(By.ID, "consumo")
    # campo_classificacao = driver_visivel.find_element(By.ID, "classificacao")

    # Assert
    assert campo_consumo.text == titulo_esperado
    
def test_consumo_distancia_zero(driver_visivel):
    # Arrange
    titulo_esperado = "Inválido!"
    litros = 2
    distancia = 0

    # Act
    driver_visivel.get(URL_BASE)

    campo_litros = driver_visivel.find_element(By.ID, "litros")
    campo_litros.send_keys(litros)

    campo_distancia = driver_visivel.find_element(By.ID, "distancia")
    campo_distancia.send_keys(distancia)

    botao_calcular = driver_visivel.find_element(By.ID, "btn-calcular")
    botao_calcular.click()

    campo_consumo = driver_visivel.find_element(By.ID, "consumo")
    # campo_classificacao = driver_visivel.find_element(By.ID, "classificacao")

    # Assert
    assert campo_consumo.text == titulo_esperado
