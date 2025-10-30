# Simulacao e Teste de Software (CC8550) — Aula 11 – Testes Nao Funcionais: Desempenho, Carga, Estresse, Escalabilidade e Seguranca

**Prof. Luciano Rossi**  
**Ciência da Computação — Centro Universitário FEI**  
**2º Semestre de 2025**

---

## Testes Não Funcionais

### Definição
Testes não funcionais avaliam como o sistema se comporta sob diferentes condições, focando em aspectos de qualidade como desempenho, segurança, usabilidade e confiabilidade, ao invés de verificar se o sistema faz o que deveria fazer.

**Objetivo:** Garantir que o sistema atenda aos requisitos de qualidade e seja adequado para uso em produção.

### Tipos de Testes Não Funcionais
- **Testes de Desempenho:** Velocidade e responsividade do sistema
- **Testes de Carga:** Comportamento sob carga normal e esperada
- **Testes de Estresse:** Limites máximos e ponto de quebra
- **Testes de Escalabilidade:** Capacidade de crescimento
- **Testes de Segurança:** Proteção contra vulnerabilidades

---

## Testes de Desempenho

### Descrição
Avaliam a velocidade, responsividade e estabilidade do sistema sob uma carga de trabalho normal, medindo métricas como tempo de resposta e throughput.

**Métricas principais:**
- Tempo de resposta (response time)
- Throughput (requisições por segundo)
- Utilização de recursos (CPU, memoria, I/O)
- Latência de rede

**Exemplo:** Verificar se uma página web carrega em menos de 2 segundos

### Métrica: Tempo de Resposta

**Definição**  
Intervalo entre o envio de uma requisição e o recebimento completo da resposta. Mede a velocidade percebida pelo usuário final.

**Componentes:** DNS + Conexão + Processamento + Transmissão

| Contexto      | Meta   | Limite |
|---------------|--------|--------|
| Páginas web   | < 200ms | < 500ms |
| APIs REST     | < 300ms | < 800ms |
| Transações    | < 3s    | < 10s   |

**Interpretação:**
- **Média:** Performance geral do sistema
- **P95:** 95% dos usuários têm boa experiência
- **P99:** Identifica gargalos ocasionais

**Regra prática:** 40% usuários abandonam se > 3 segundos

### Métrica: Throughput (Requisições por Segundo)

**Definição**  
Throughput mede quantas requisições o sistema consegue processar por unidade de tempo (req/s). Indica a capacidade máxima e eficiência do sistema sob carga.

**Fórmula:** Throughput = Total de Requisições / Tempo Total

| Tipo de Sistema     | Throughput Típico | Meta Alta Performance |
|---------------------|-------------------|-----------------------|
| Site institucional  | 50–200 req/s      | > 500 req/s           |
| E-commerce médio    | 100–500 req/s     | > 1000 req/s          |
| API REST simples    | 200–1000 req/s    | > 2000 req/s          |
| Sistema de pagamento| 50–200 req/s      | > 300 req/s           |
| CDN/Cache           | 1000–10000 req/s  | > 50000 req/s         |

**Fatores que Impactam:**
- Hardware: CPU, memória, rede disponível
- Arquitetura: Load balancers, cache, microserviços
- Código: Eficiência algoritmos, queries de banco
- Concorrência: Threads, conexões simultâneas

**Exemplo:** 10.000 req em 50s = 200 req/s de throughput

### Métrica: Utilização de Recursos (CPU, Memória, I/O)

**Definição**  
Utilização de recursos mede o consumo de CPU, memória e I/O durante a execução dos testes. Identifica gargalos de hardware e limites de capacidade do sistema.

| Recurso   | Normal | Alto   | Crítico |
|-----------|--------|--------|---------|
| CPU       | < 70%  | 70–85% | > 85%   |
| Memória   | < 80%  | 80–90% | > 90%   |
| I/O Disco | < 80%  | 80–95% | > 95%   |
| I/O Rede  | < 70%  | 70–90% | > 90%   |

**Sinais de Gargalo por Recurso:**
- CPU > 85%: Processamento intensivo, algoritmos ineficientes
- Memória > 90%: Memory leaks, cache excessivo, dados grandes
- I/O Disco alto: Queries lentas, logs excessivos, swap ativo
- I/O Rede alto: Payload grande, latência externa, muitas conexões

**Monitoramento:** Coletar antes, durante e após o teste para identificar degradação de performance relacionada aos recursos.

### Métrica: Latência de Rede

**Definição**  
Latência de rede é o tempo que um pacote de dados leva para viajar de origem ao destino, medindo apenas o atraso da transmissão física, sem incluir processamento no servidor.

**Medição:** RTT (Round Trip Time) — tempo ida + volta do pacote

| Tipo de Conexão        | Latência Típica | Classificação |
|------------------------|-----------------|---------------|
| LAN (mesmo prédio)     | 1–5ms           | Excelente     |
| Cidade (fibra)         | 5–20ms          | Muito boa     |
| Nacional (cabo)        | 20–50ms         | Boa           |
| Internacional          | 50–150ms        | Aceitável     |
| Satélite               | 500–700ms       | Problemática  |
| 4G/5G Mobile           | 30–100ms        | Variável      |

**Fatores que Impactam:**
- Distância física: Velocidade da luz é o limite absoluto
- Infraestrutura: Fibra vs cabo vs wireless vs satélite
- Roteamento: Número de hops entre origem e destino
- Congestionamento: Tráfego na rede durante horário de pico

**Impacto:** Latência alta = Tempo de resposta mínimo inescapável

---

## Testes de Carga

### Descrição
Verificam como o sistema se comporta sob carga esperada normal e picos de trafego, simulando numero realista de usuários simultâneos.

**Características:**
- Simula carga realista de produção
- Testa cenários de pico
- Identifica gargalos antes da quebra
- Valida requisitos de desempenho

**Exemplo:** 1000 usuários simultâneos acessando um e-commerce

### Testes de Carga: Simula Carga Realista de Produção

**Definição**  
Reproduz padrões de uso real dos usuários em produção, incluindo distribuição de ações, timing natural e comportamento típico da aplicação.

**Elementos de Realismo:**
- Mix de operações: 70% leitura, 20% escrita, 10% relatórios
- Padrão temporal: Picos manhã/tarde, baixa madrugada
- Think time: 2–5s entre ações (simula usuário real)
- Sessões variáveis: 5–30min de duração por usuário

| Cenário            | Usuários Simultâneos | Duração |
|--------------------|----------------------|---------|
| E-commerce normal  | 500–1000             | 1–2 horas |
| Sistema bancário   | 200–500              | 8 horas |
| Rede social        | 1000–5000            | 4 horas |
| API corporativa    | 100–300              | 2 horas |

**Objetivo:** Validar se o sistema suporta a carga esperada do dia a dia

### Testes de Carga: Testa Cenários de Pico

**Definição**  
Simula momentos de tráfego intenso como Black Friday, lançamentos de produtos, promoções ou eventos sazonais que geram picos de acesso.

**Tipos de Cenários de Pico:**
- Black Friday: 10x–20x tráfego normal em 2–4 horas
- Lançamento: 5x–15x usuários em 30–60 minutos
- Campanhas: 3x–8x carga durante propagandas
- Fim do mês: 2x–4x aumento gradual (sistemas corporativos)

| Evento        | Multiplicador | Duração do Pico |
|---------------|---------------|-----------------|
| Black Friday  | 15x–20x       | 4–6 horas       |
| Cyber Monday  | 10x–15x       | 8–12 horas      |
| Flash sale    | 20x–50x       | 15–30 minutos   |
| Horário comercial | 3x–5x    | 6–8 horas       |

**Objetivo:** Garantir que sistema não falhe em momentos críticos de negócio

### Testes de Carga: Identifica Gargalos Antes da Quebra

**Definição**  
Detecta pontos fracos do sistema (CPU, memória, banco, rede) antes que causem falhas completas, permitindo otimizações preventivas.

**Sinais de Gargalo por Componente:**
- Banco de dados: Tempo queries > 500ms, conexões esgotando
- CPU: Utilização > 80%, tempo resposta crescendo linear
- Memória: > 85% uso, garbage collection frequente
- Rede: Latência aumentando, timeouts ocasionais

| Gargalo          | Sintoma                 | Ação Preventiva     |
|------------------|-------------------------|---------------------|
| Banco slow       | queries > 500ms         | Otimizar índices    |
| Memory leak      | RAM crescendo           | Revisar código      |
| CPU bound        | > 80% uso               | Scale vertical      |
| Connection pool  | Timeouts                | Aumentar pool       |

**Objetivo:** Antecipar problemas e otimizar antes da falha total

### Testes de Carga: Valida Requisitos de Desempenho

**Definição**  
Confirma se o sistema atende aos SLAs definidos (tempo resposta, throughput, disponibilidade) sob condições de carga especificadas.

**Tipos de Requisitos Validados:**
- Tempo resposta: P95 < 500ms, P99 < 1s
- Throughput: Sistema deve processar ⩾ 1000 req/s
- Disponibilidade: Taxa erro < 0.1% durante teste
- Capacidade: Suportar 500 usuários simultâneos

| SLA            | Critério              | Status          |
|----------------|-----------------------|-----------------|
| Tempo resposta | P95 < 500ms           | PASSOU/FALHOU   |
| Throughput     | ⩾ 1000 req/s          | PASSOU/FALHOU   |
| Disponibilidade| < 0.1% erro           | PASSOU/FALHOU   |
| Escalabilidade | 500 usuários          | PASSOU/FALHOU   |

**Objetivo:** Aprovar ou reprovar sistema baseado em critérios objetivos

---

## Testes de Estresse

### Descrição
Encontram o ponto de quebra do sistema aplicando carga além da capacidade planejada, identificando como o sistema falha e se recupera.

**Objetivos:**
- Descobrir limites máximos do sistema
- Testar recuperação apos falhas
- Validar mensagens de erro adequadas
- Verificar estabilidade apos sobrecarga

**Exemplo:** Aumentar usuários gradualmente ate o sistema falhar

### Testes de Estresse: Descobrir Limites Máximos do Sistema

**Definição**  
Aumenta progressivamente a carga até encontrar o ponto de quebra, determinando a capacidade máxima real do sistema antes da falha completa.

**Métodos de Descoberta:**
- Ramp-up gradual: +10 usuários a cada 30s até falhar
- Spike testing: Saltos súbitos de carga (100→1000→5000)
- Volume testing: Aumentar dados processados até limite
- Soak testing: Carga alta sustentada por horas

| Indicador de Limite | Sintoma                   | Valor Crítico     |
|---------------------|---------------------------|-------------------|
| Taxa de erro        | Erros 5xx aumentando      | > 5%              |
| Tempo resposta      | Crescimento exponencial   | > 10x normal      |
| Throughput          | Platô ou queda            | < 50% máximo      |
| Recursos            | CPU/Memória saturados     | > 95%             |

**Objetivo:** Determinar capacidade máxima real para dimensionamento adequado

### Testes de Estresse: Testar Recuperação Após Falhas

**Definição**  
Avalia como o sistema se comporta após atingir o ponto de quebra, verificando se consegue retornar ao funcionamento normal quando a carga diminui.

**Cenários de Recuperação:**
- Graceful degradation: Sistema reduz funcionalidades mas mantém núcleo
- Auto-healing: Recuperação automática sem intervenção manual
- Circuit breaker: Proteção contra cascata de falhas
- Restart recovery: Tempo para voltar após reinicialização

| Tipo de Falha        | Tempo Recuperação | Classificação |
|----------------------|-------------------|---------------|
| Sobrecarga temporária| < 30 segundos     | Excelente     |
| Saturação de memória | 1–5 minutos       | Boa           |
| Crash de serviço     | 5–15 minutos      | Aceitável     |
| Corrupção de dados   | > 30 minutos      | Problemática  |

**Objetivo:** Garantir que falhas sejam temporárias e sistema volte ao normal

### Testes de Estresse: Validar Mensagens de Erro Adequadas

**Definição**  
Verifica se o sistema fornece mensagens de erro claras e úteis quando atinge limites, evitando falhas silenciosas ou erros confusos.

**Tipos de Mensagens Validadas:**
- HTTP Status corretos: 503 Service Unavailable, 429 Too Many Requests
- Mensagens descritivas: "Sistema temporariamente indisponível"
- Códigos de erro específicos: RATE_LIMIT_EXCEEDED, MEMORY_FULL
- Logs detalhados: Registro adequado para troubleshooting

| Situação              | Erro Adequado         | Erro Inadequado       |
|-----------------------|-----------------------|------------------------|
| Sistema sobrecarregado| 503 + retry-after     | 500 Internal Error     |
| Rate limit atingido   | 429 + limite/tempo    | Timeout silencioso     |
| Memória esgotada      | 503 + mensagem clara  | Conexão recusada       |
| Queue cheia           | 503 + tempo espera    | Erro genérico          |

**Objetivo:** Facilitar diagnóstico e melhorar experiência do usuário em falhas

### Testes de Estresse: Verificar Estabilidade Após Sobrecarga

**Definição**  
Confirma que o sistema mantém performance estável e não apresenta degradação permanente após períodos de estresse intenso.

**Indicadores de Estabilidade:**
- Performance baseline: Tempo resposta volta aos níveis originais
- Memory leaks: Uso de memória retorna ao normal
- Connection pools: Conexões liberadas adequadamente
- Cache consistency: Dados em cache permanecem íntegros

| Métrica               | Antes Estresse | Após Estresse |
|-----------------------|----------------|---------------|
| Tempo resposta médio  | 200ms          | ⩽ 220ms       |
| Uso de memória        | 60%            | ⩽ 65%         |
| Conexões ativas       | 50             | ⩽ 55          |
| Taxa de cache hit     | 85%            | ⩾ 80%         |

**Objetivo:** Assegurar que estresse não cause degradação permanente do sistema

---

## Testes de Escalabilidade

### Descrição
Verificam a capacidade do sistema de crescer e se adaptar ao aumento de carga através de escalabilidade horizontal (mais servidores) ou vertical (mais recursos).

**Tipos de escalabilidade:**
- **Horizontal:** Adicionar mais instâncias/servidores
- **Vertical:** Aumentar CPU, RAM, storage
- **Funcional:** Distribuir funcionalidades

**Exemplo:** Adicionar servidores e medir melhoria de performance

### Testes de Escalabilidade: Escalabilidade Horizontal

**Definição**  
Verifica como o sistema se comporta ao adicionar mais instâncias/servidores, medindo se a performance melhora proporcionalmente ao número de nós adicionados.

**Cenários de Teste:**
- Baseline: 1 servidor com 1000 usuários = 200 req/s
- Scale out: 2 servidores = 400 req/s esperado (2x)
- Load balancing: Distribuição uniforme entre instâncias
- Session affinity: Teste com sticky sessions

| Servidores | Throughput Real | Throughput Ideal | Eficiência |
|------------|------------------|------------------|------------|
| 1          | 200 req/s        | 200 req/s        | 100%       |
| 2          | 380 req/s        | 400 req/s        | 95%        |
| 4          | 720 req/s        | 800 req/s        | 90%        |
| 8          | 1280 req/s       | 1600 req/s       | 80%        |

**Objetivo:** Validar se adicionar servidores melhora performance proporcionalmente

### Testes de Escalabilidade: Escalabilidade Vertical

**Definição**  
Avalia como o sistema aproveita recursos adicionais (CPU, RAM, storage) em uma única máquina, medindo o ganho de performance por recurso adicionado.

**Recursos Testados:**
- CPU: 2→4→8 cores, medir throughput por core
- RAM: 8→16→32GB, verificar cache hits e GC
- Storage: HDD→SSD→NVMe, tempo I/O de banco
- Rede: 1Gbps→10Gbps, latência e throughput

| Configuração    | Performance | Melhoria | Custo/Benefício |
|-----------------|------------:|---------:|-----------------|
| 2 cores, 8GB    | 300 req/s   | Baseline | -               |
| 4 cores, 16GB   | 550 req/s   | +83%     | Bom             |
| 8 cores, 32GB   | 900 req/s   | +200%    | Excelente       |
| 16 cores, 64GB  | 1100 req/s  | +267%    | Diminuindo      |

**Objetivo:** Encontrar ponto ótimo de recursos vs performance vs custo

### Testes de Escalabilidade: Escalabilidade Funcional

**Definição**  
Testa a distribuição de funcionalidades em diferentes serviços especializados (microserviços), verificando se a separação melhora performance e isolamento.

**Estratégias de Distribuição:**
- Por domínio: Usuários, Produtos, Pagamentos em serviços separados
- Por operação: Read vs Write services (CQRS)
- Por carga: APIs públicas vs dashboards internos
- Por criticidade: Serviços core vs auxiliares

| Arquitetura     | Latência | Disponibilidade | Manutenibilidade |
|-----------------|---------:|----------------:|------------------|
| Monolítico      | 150ms    | 99.5%           | Baixa            |
| 3 Microserviços | 180ms    | 99.8%           | Média            |
| 6 Microserviços | 220ms    | 99.9%           | Alta             |
| 12 Microserviços| 300ms    | 99.7%           | Complexa         |

**Objetivo:** Balancear performance, confiabilidade e complexidade operacional

### Testes de Escalabilidade: Métricas de Avaliação

**Definição**  
Define métricas específicas para avaliar a eficácia de cada tipo de escalabilidade, considerando performance, custo e complexidade operacional.

**Métricas por Tipo:**
- **Horizontal:** Eficiência = (Throughput real / Throughput ideal) × 100
- **Vertical:** ROI = Melhoria performance / Aumento custo
- **Funcional:** Isolamento = Falhas contidas vs falhas em cascata
- **Geral:** Elasticidade = Tempo para adaptar à demanda

| Tipo       | Vantagem            | Desvantagem        | Melhor Para           |
|------------|---------------------|--------------------|-----------------------|
| Horizontal | Sem limite teórico  | Complexidade rede  | Aplicações stateless  |
| Vertical   | Simplicidade        | Limite hardware    | CPU/Memory intensive  |
| Funcional  | Isolamento falhas   | Latência adicional | Sistemas complexos    |

**Objetivo:** Escolher estratégia de escalabilidade adequada para cada contexto

---

## Testes de Segurança

### Descrição
Identificam vulnerabilidades e verificam se os mecanismos de proteção funcionam adequadamente contra ataques e acessos não autorizados.

**Áreas testadas:**
- Autenticação e autorização
- Criptografia de dados
- Injeção de código (SQL, XSS, CSRF)
- Controle de acesso
- Auditoria e logs

**Ferramentas:** OWASP ZAP, Burp Suite, Nessus

### Testes de Segurança: Autenticação e Autorização

**Definição**  
Verifica se os mecanismos de autenticação (quem é o usuário) e autorização (o que pode fazer) funcionam adequadamente, impedindo acessos não autorizados.

**Cenários de Teste:**
- Login válido: Credenciais corretas → acesso permitido
- Login inválido: Credenciais erradas → acesso negado
- Token expirado: JWT/Session timeout → reautenticação
- Privilégios: Usuário comum tentando acesso admin

| Teste             | Entrada                        | Resultado Esperado           |
|-------------------|--------------------------------|------------------------------|
| Credenciais válidas | user: admin, pass: 123456    | 200 OK + token               |
| Senha incorreta   | user: admin, pass: wrong       | 401 Unauthorized             |
| Usuário inexistente| user: fake, pass: any          | 401 Unauthorized             |
| Acesso sem token  | GET /admin sem auth            | 401 Unauthorized             |
| Token expirado    | JWT vencido                    | 401 + refresh needed         |

**Objetivo:** Garantir que apenas usuários autorizados acessem recursos protegidos

### Testes de Segurança: Criptografia de Dados

**Definição**  
Valida se dados sensíveis são adequadamente criptografados em trânsito (HTTPS) e em repouso (banco de dados), protegendo informações confidenciais.

**Aspectos Testados:**
- HTTPS obrigatório: Todas requisições via SSL/TLS
- Senhas hash: bcrypt, scrypt, Argon2 (nunca plain text)
- Dados PII: CPF, cartão, email criptografados na base
- Certificados: Validação de certificados SSL válidos

| Dado     | Armazenamento Seguro     | Vulnerabilidade          |
|----------|---------------------------|--------------------------|
| Senha    | $2b$12$hash...            | plain text password      |
| CPF      | AES-256 encrypted         | 123.456.789-00           |
| Cartão   | Tokenizado PCI DSS        | 4111-1111-1111-1111      |
| API Key  | SHA-256 hashed            | sk-abc123def456...       |
| Session  | HttpOnly + Secure cookie  | sem flags                |

**Objetivo:** Proteger dados sensíveis contra exposição e vazamentos

### Testes de Segurança: Injeção de Código (SQL, XSS, CSRF)

**Definição**  
Detecta vulnerabilidades de injeção que permitem execução de código malicioso, como SQL injection, Cross-Site Scripting e Cross-Site Request Forgery.

**Tipos de Ataques Testados:**
- SQL Injection: ’; DROP TABLE users; -
- XSS Stored: `<script>alert(’XSS’)</script>`
- XSS Reflected: URL com payload JavaScript malicioso
- CSRF: Requisições forjadas de sites externos

| Vulnerabilidade   | Payload de Teste                 | Defesa                |
|-------------------|----------------------------------|-----------------------|
| SQL Injection     | ’ OR ’1’=’1                      | Prepared statements   |
| XSS Stored        | `<img src=x onerror=alert(1)>`   | Sanitização HTML      |
| XSS Reflected     | `?search=<script>...`            | Escape de output      |
| CSRF              | Form submit externo              | CSRF tokens           |
| Command Injection | `; rm -rf /`                     | Input validation      |

**Objetivo:** Identificar e corrigir pontos de entrada para códigos maliciosos

### Testes de Segurança: Controle de Acesso

**Definição**  
Verifica se as regras de acesso a recursos são implementadas corretamente, garantindo que usuários só acessem dados e funcionalidades permitidas.

**Cenários de Controle:**
- RBAC: Role-Based Access Control (admin, user, guest)
- ABAC: Attribute-Based (departamento, projeto, nível)
- Path traversal: Tentativas de acesso a diretórios proibidos
- IDOR: Insecure Direct Object Reference (ID de outros usuários)

| Teste        | Cenário                          | Resultado Esperado |
|--------------|----------------------------------|--------------------|
| RBAC         | User acessa /admin               | 403 Forbidden      |
| IDOR         | GET /user/123 por user/456       | 403 ou dados filtrados |
| Path traversal| `../../../etc/passwd`           | 403 ou 404         |
| API endpoints| POST sem permissão               | 403 Forbidden      |
| File upload  | Upload de .php/.exe              | Rejeitado          |

**Objetivo:** Implementar princípio do menor privilégio e segregação de dados

### Testes de Segurança: Auditoria e Logs

**Definição**  
Valida se eventos de segurança são adequadamente registrados e monitorados, permitindo detecção de ataques e investigação de incidentes.

**Eventos que Devem ser Logados:**
- Autenticação: Login sucesso/falha, logout, mudança senha
- Autorização: Tentativas de acesso negado, escalação privilégio
- Dados sensíveis: Acesso, modificação, exclusão de PII
- Segurança: Tentativas de injection, rate limiting, bloqueios

| Evento           | Log Obrigatório | Informações                         |
|------------------|-----------------|-------------------------------------|
| Login falha      | SIM             | IP, user, timestamp, tentativas     |
| Acesso admin     | SIM             | User, ação, recurso, resultado      |
| SQL injection    | SIM             | IP, payload, endpoint afetado       |
| Download dados   | SIM             | User, arquivo, quantidade           |
| Rate limit hit   | SIM             | IP, endpoint, limite atingido       |

**Objetivo:** Detectar ataques em tempo real e facilitar investigação forense

---

## Principais Ferramentas

| Ferramenta | Características                        | Tipo            |
|------------|----------------------------------------|-----------------|
| Locust     | Python, interface web, distribuído     | Carga/Estresse  |
| JMeter     | Interface gráfica, protocolos múltiplos| Performance     |
| K6         | JavaScript, CLI, cloud integrado       | Carga moderna   |
| Gatling    | Scala, alta performance, relatórios    | Enterprise      |
| OWASP ZAP  | Proxy de interceptação                 | Segurança       |

**Nota:** Para Python: Locust é a ferramenta mais popular e intuitiva

---

## Atividade para entrega

### Atividade Prática: Teste Integrado de E-commerce

**Cenário**  
Desenvolva um plano de teste completo para um sistema de e-commerce que será lançado na Black Friday, incorporando uma métrica de cada tipo de teste não funcional.

**Requisitos do Sistema:**
- 10.000 usuários simultâneos esperados na Black Friday
- Tempo de resposta < 500ms para 95% das requisições
- Disponibilidade de 99.9% durante o evento
- Proteção contra ataques e vazamento de dados

| Tipo de Teste | Métrica Obrigatória      | Meta Definida      |
|---------------|---------------------------|--------------------|
| Desempenho    | Tempo de resposta         | P95 < 500ms        |
| Carga         | Throughput sustentado     | > 2000 req/s       |
| Estresse      | Ponto de quebra           | > 15.000 usuários  |
| Escalabilidade| Eficiência horizontal     | > 80%              |
| Segurança     | Rate limiting             | 100 req/min/IP     |

**Entregável:** Exemplos de testes implementados em Python para cada tipo, incluindo código funcional, métricas coletadas e relatório de resultados com análise de aprovação/reprovação das metas.

---

**Simulacao e Teste de Software (CC8550) — Aula 11 – Testes Nao Funcionais: Desempenho, Carga, Estresse, Escalabilidade e Seguranca**  
Prof. Luciano Rossi — Ciência da Computação — Centro Universitário FEI — 2º Semestre de 2025
