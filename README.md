# Caso para Avaliação - Plataforma de Biblioteca Digital

Cenário: Imagine que você foi convidado a participar do
planejamento de uma nova plataforma de biblioteca digital
para uma universidade. O sistema deverá:
<br><br>
▶ Permitir que alunos e professores pesquisem por título,
autor ou assunto;
<br>
▶ Disponibilizar o acesso a e-books e permitir reserva de
livros físicos;
<br>
▶ Enviar lembretes sobre prazos de devolução;
<br>
▶ Oferecer aos bibliotecários ferramentas para gerenciar o
acervo e gerar relatórios.


## Características Técnicas

### 1. Correto

**Funcionalidade Relacionada**:  *Enviar lembretes sobre prazos de devolução*
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** |  |
| **Característica de Qualidade Relacionada** |  |
| **Fórmula de Cálculo** |  |
| **Unidade de Medida** |  |
| **Meta ou valor de referência desejado** |  |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** |  |
| **Objetivo** |  |
| **Pré-condições** |  |
| **Passos para a execução** |  |
| **Resultado esperado** |  |

---
### 2. Confiável

**Funcionalidade Relacionada:** *Permitir que alunos e professores pesquisem por título, autor ou assunto*
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** |  |
| **Característica de Qualidade Relacionada** |  |
| **Fórmula de Cálculo** |  |
| **Unidade de Medida** |  |
| **Meta ou valor de referência desejado** |  |

**Teste**
 |  ||
| -------- | ----- |
| **Nome do Teste** |  |
| **Objetivo** |  |
| **Pré-condições** |  |
| **Passos para a execução** |  |
| **Resultado esperado** |  |

---
### 3. Eficiente

**Funcionalidade Relacionada**: *Permitir que alunos e professores pesquisem por título, autor ou assunto.*
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | Tempo médio de resposta |
| **Característica de Qualidade Relacionada** | Eficiente |
| **Fórmula de Cálculo** | Soma dos tempos de resposta / Número de requisições |
| **Unidade de Medida** | Milissegundos |
| **Meta ou valor de referência desejado** | ≤ 750 ms |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | Teste de desempenho com medições do tempo das respostas |
| **Objetivo** | Reduzir atrasos e garantir agilidade no acesso |
| **Pré-condições** | Uma lista de termos de busca a serem utilizados no teste |
| **Passos para a execução** | 1. O teste recebe como entrada um termo de busca a ser avaliado no sistema; 2. Chama-se a funcionalidade de busca (por título, autor, ou assunto) com o termo de busca selecionado; 3. Mede-se o tempo de resposta da requisição; 4. Usando a fórmula, descobre-se o tempo médio das requisições da funcionalidade de busca do sistema. |
| **Resultado esperado** | Espera-se que a tempo médio seja igual ou menor ao valor de referência (≤ 750 ms), com o sistema utilizando estratégias de cache para buscas muito frequentes e com paginação para buscas com resultados muito grandes. |

---
### 4. Íntegro

**Funcionalidade Relacionada**: *Oferecer aos bibliotecários ferramentas para gerenciar o acervo e gerar relatórios.*

**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | Taxa de requisições não autorizadas à funções de administrador de acervo bloqueadas  |
| **Característica de Qualidade Relacionada** | Íntegro |
| **Fórmula de Cálculo** | Número de requisições não autorizadas bloqueadas / Número de requisições não autorizadas |
| **Unidade de Medida** | Não se aplica (porcentagem) |
| **Meta ou valor de referência desejado** | 100% |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | Testes de segurança da proteção de funções de administrador |
| **Objetivo** | Garantir que apenas usuários autorizados acessem dados e funções restritas |
| **Pré-condições** | Uma lista de usuários (mock) cadastrados mas sem acesso a funções de administrador |
| **Passos para a execução** | 1. O teste recebe como entrada a lista de usuários teste; 2. Chama-se as funcionalidade de administrador de acervo; 3. Conta-se quantas funcionalidades restritas são acessadas por usuários não autorizados; 4. Usando a fórmula, descobre-se a taxa de sucesso em bloquear acessos não autorizados. |
| **Resultado esperado** | Espera-se que a taxa de acessos não autorizados bloqueados seja igual ao valor de referência (100%) |

---
### 5. Fácil de Usar

**Funcionalidade Relacionada**: *Disponibilizar o acesso a e-books e permitir reserva de livros físicos*

**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | Tempo médio para realizar fazer reserva de livro |
| **Característica de Qualidade Relacionada** | Fácil de Usar |
| **Fórmula de Cálculo** | Soma dos tempos no processo de reserva de livro / Número de usuários testados |
| **Unidade de Medida** | Minutos |
| **Meta ou valor de referência desejado** | ≤ 1.5 minutos |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | Teste de usabilidade com usuários reais |
| **Objetivo** | Reduzir curva de aprendizado e erros de uso |
| **Pré-condições** | Protótipo funcional do sistema em ambiente de teste |
| **Passos para a execução** | 1. Seleciona-se grupo de usuários para teste da funcionalidade; 2. Mede-se o tempo gasto para cada usuário; 3. Observa-se possíveis obstáculos no processo; 4. Usando a fórmula, descobre-se o tempo médio no processo. |
| **Resultado esperado** | Espera-se que o tempo médio para realizar a reserva do seja igual ou inferior ao valor de referência (1.5 minutos) |

---
### 6. Interoperável

#### Funcionalidade Relacionada: 
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | ... |
| **Característica de Qualidade Relacionada** | ... |
| **Fórmula de Cálculo** | ... |
| **Unidade de Medida** | ... |
| **Meta ou valor de referência desejado** | ... |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | ... |
| **Objetivo** | ... |
| **Pré-condições** | ... |
| **Passos para a execução** | ... |
| **Resultado esperado** | ... |

## Características de Manutenção

### 1. Manutenível

#### Funcionalidade Relacionada: 
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | ... |
| **Característica de Qualidade Relacionada** | ... |
| **Fórmula de Cálculo** | ... |
| **Unidade de Medida** | ... |
| **Meta ou valor de referência desejado** | ... |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | ... |
| **Objetivo** | ... |
| **Pré-condições** | ... |
| **Passos para a execução** | ... |
| **Resultado esperado** | ... |

---
### 2. Flexível

#### Funcionalidade Relacionada: 
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | ... |
| **Característica de Qualidade Relacionada** | ... |
| **Fórmula de Cálculo** | ... |
| **Unidade de Medida** | ... |
| **Meta ou valor de referência desejado** | ... |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | ... |
| **Objetivo** | ... |
| **Pré-condições** | ... |
| **Passos para a execução** | ... |
| **Resultado esperado** | ... |

---
### 3. Testável

#### Funcionalidade Relacionada: 
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | ... |
| **Característica de Qualidade Relacionada** | ... |
| **Fórmula de Cálculo** | ... |
| **Unidade de Medida** | ... |
| **Meta ou valor de referência desejado** | ... |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | ... |
| **Objetivo** | ... |
| **Pré-condições** | ... |
| **Passos para a execução** | ... |
| **Resultado esperado** | ... |

---
### 4. Portável

#### Funcionalidade Relacionada: 
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | ... |
| **Característica de Qualidade Relacionada** | ... |
| **Fórmula de Cálculo** | ... |
| **Unidade de Medida** | ... |
| **Meta ou valor de referência desejado** | ... |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | ... |
| **Objetivo** | ... |
| **Pré-condições** | ... |
| **Passos para a execução** | ... |
| **Resultado esperado** | ... |

---
### 5. Reutilizável

#### Funcionalidade Relacionada: 
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | ... |
| **Característica de Qualidade Relacionada** | ... |
| **Fórmula de Cálculo** | ... |
| **Unidade de Medida** | ... |
| **Meta ou valor de referência desejado** | ... |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | ... |
| **Objetivo** | ... |
| **Pré-condições** | ... |
| **Passos para a execução** | ... |
| **Resultado esperado** | ... |
