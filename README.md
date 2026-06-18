# Testes Automatizados da Premiação da Copa do Mundo

Projeto desenvolvido para demonstrar a utilização do **Selenium WebDriver**, **Pytest** e da técnica de **Análise do Valor Limite (AVL)** em testes funcionais automatizados.

## Objetivo

Automatizar testes sobre a aplicação de premiação da Copa do Mundo disponível em:

https://marceloterencianiifpr.github.io/premiacao-copa/

O projeto tem finalidade educacional e busca apresentar conceitos fundamentais de automação de testes utilizando Python.

## Tecnologias Utilizadas

* Python
* Selenium WebDriver
* Pytest
* Google Chrome

## Estrutura do Projeto

```text
premiacao-copa-selenium/
│
├── tests/
│   ├── conftest.py
│   └── test_premiacao.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Configuração do Ambiente

Criar ambiente virtual:

```bash
python -m venv venv
```

Ativar ambiente virtual:

Windows:

```bash
venv\Scripts\activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

## Executando os Testes

Executar todos os testes:

```bash
pytest
```

Executar com informações detalhadas:

```bash
pytest -v
```

## Organização dos Testes

Os testes seguem o padrão **AAA (Arrange, Act, Assert)**:

* **Arrange**: preparação dos dados e do ambiente;
* **Act**: execução da ação que será testada;
* **Assert**: validação do resultado esperado.

## Fixture Selenium

O navegador é gerenciado por meio de fixtures do Pytest, permitindo reutilização da configuração entre os testes e encerramento automático dos recursos ao final da execução.

## Objetivo Pedagógico

Este projeto pode ser utilizado em disciplinas de Teste de Software para demonstrar:

* automação de testes web;
* utilização de Selenium WebDriver;
* utilização de Pytest;
* aplicação da técnica de Análise do Valor Limite;
* organização de testes utilizando o padrão AAA;
* reutilização de recursos através de fixtures.
