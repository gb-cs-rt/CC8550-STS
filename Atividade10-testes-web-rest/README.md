# Aula 10 - Testes de Aplicações Web e Serviços REST

Material didático sobre testes automatizados de aplicações web e APIs REST.

## Conteúdo

- **exemplos/**: Código-fonte dos exemplos práticos
- **exercicios/**: Exercícios propostos para os alunos

## Tópicos Abordados

### Testes de Aplicações Web
- Definição e tipos de testes
- Ferramentas: Selenium, Playwright, Cypress
- Exemplos práticos com Selenium em Python
- Page Object Model
- Testes responsivos e cross-browser

### Testes de Serviços REST
- Definição e tipos de testes  
- Testes de status code, schema, validação
- Autenticação e autorização
- Testes CRUD completos
- Testes de performance com Locust

## Como Usar

### Pré-requisitos

- Python 3.8+
- pip

### Instalação

    cd aula10-testes-web-rest/exemplos
    
    # Criar ambiente virtual
    python -m venv venv
    
    # Ativar ambiente virtual
    source venv/bin/activate  # Linux/Mac
    # ou
    venv\Scripts\activate     # Windows
    
    # Instalar dependências
    pip install -r requirements.txt

Ou use os scripts de setup:

    # Linux/Mac
    ./setup.sh
    
    # Windows
    setup.bat

### Executar Testes

    # Todos os testes
    pytest tests/ -v
    
    # Apenas testes de API (não precisa Chrome)
    pytest tests/test_api.py tests/test_integration.py -v
    
    # Apenas testes web (requer Chrome instalado)
    pytest tests/test_web.py -v
    
    # Com relatório HTML
    pytest tests/ --html=report.html --self-contained-html
    
    # Com cobertura
    pytest tests/ --cov=. --cov-report=html

### Usar Markers

    # Apenas testes de API
    pytest tests/ -v -m api
    
    # Apenas testes de integração
    pytest tests/ -v -m integration
    
    # Excluir testes web (útil em ambientes sem navegador)
    pytest tests/ -v -m "not web"

## Nota sobre Ambientes

### Testes de API REST
Funcionam em qualquer ambiente (GitHub Codespaces, containers, local)

### Testes Web (Selenium)
Requerem Google Chrome instalado

- Em ambientes como GitHub Codespaces ou containers sem Chrome, os testes web serão automaticamente pulados (skipped)
- Para executar apenas testes que funcionam sem navegador: `pytest tests/ -v -m "not web"`
- Para instalar Chrome localmente:
  - Ubuntu/Debian: `sudo apt-get install google-chrome-stable`
  - Windows/Mac: https://www.google.com/chrome/

## Estrutura dos Testes

    exemplos/
    ├── tests/
    │   ├── test_api.py          # 14 testes de API REST
    │   ├── test_integration.py  # 2 testes de integração
    │   └── test_web.py          # 7 testes de interface web
    ├── pages/                   # Page Object Model
    │   ├── base_page.py        # Classe base
    │   └── google_page.py      # Exemplo de Page Object
    ├── api/                     # Clientes de API
    │   └── users_api.py        # Cliente para API de usuários
    └── locustfile.py           # Testes de carga/performance

## APIs Públicas Utilizadas

- JSONPlaceholder: https://jsonplaceholder.typicode.com/ (API REST de teste)
- Google: Apenas para exemplos de automação web

## Exercícios

Os exercícios estão disponíveis em `exercicios/README.md`

## Recursos Adicionais

### Documentação Oficial
- Selenium: https://www.selenium.dev/documentation/
- Playwright: https://playwright.dev/python/
- Pytest: https://docs.pytest.org/
- Requests: https://requests.readthedocs.io/
- Locust: https://docs.locust.io/

### APIs para Praticar
- JSONPlaceholder: https://jsonplaceholder.typicode.com/ (API REST fake)
- ReqRes: https://reqres.in/ (API REST para testes)
- PokéAPI: https://pokeapi.co/ (API de Pokémon)
- Fake Store API: https://fakestoreapi.com/ (API de e-commerce)

### Livros Recomendados
- "Test Automation using Selenium with Python" - Ashwin Pajankar
- "Python Testing with pytest" - Brian Okken
- "API Testing and Development with Postman" - Dave Westerveld

## Troubleshooting

### Chrome/ChromeDriver não encontrado
Sintoma: `google-chrome: not found` ou `ChromeDriver not found`

Solução:

    # Ubuntu/Debian
    sudo apt-get update
    sudo apt-get install google-chrome-stable
    
    # Ou execute apenas testes de API
    pytest tests/ -v -m "not web"

### Erro de permissão no setup.sh
Sintoma: `Permission denied`

Solução:

    chmod +x setup.sh
    ./setup.sh

### Testes lentos
Sintoma: Testes demorando muito

Solução:

    # Executar em paralelo (instale pytest-xdist)
    pip install pytest-xdist
    pytest tests/ -n auto

## Métricas Esperadas

Ao executar `pytest tests/ -v`:

- 16 testes PASSED (API + Integração)
- 7 testes SKIPPED (Web - se Chrome não instalado)
- Tempo: aproximadamente 1-2 segundos

## Contribuindo

Este é material didático. Sugestões e melhorias são bem-vindas!

## Licença

Material educacional - GNU General Public License v3.0

---

**Disciplina:** Simulação e Teste de Software (CC8550)  
**Professor:** Luciano Rossi  
**Instituição:** Centro Universitário FEI  
**Semestre:** 2º/2025