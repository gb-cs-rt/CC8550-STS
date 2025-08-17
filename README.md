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

**Como se aplica ao sistema**: *Todos os livros cadastrados devem possuir título, autor e assunto*
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | Taxa de Conformidade de Requisitos |
| **Característica de Qualidade Relacionada** | Correto |
| **Fórmula de Cálculo** | (Requisitor validados com sucesso / total de requisitos) * 100 |
| **Unidade de Medida** | % |
| **Meta ou valor de referência desejado** | 100% |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | Validação de busca por autor |
| **Objetivo** | Verificar se a busca retorna obras de determinado autor corretamente |
| **Pré-condições** | O usuário colocar o autor que deseja e o sistema identificar o autor |
| **Passos para a execução** | 1- Inserir o nome do autor <br> 2- Executar a pesquisa <br> 3- Verificar os resultados |
| **Resultado esperado** | O sistema retornar uma lista de obras do autor escolhido |

---
### 2. Confiável

**Como se aplica ao sistema**: *Todo aluno registrado na universidade deve ser permitido reservar um livro físico*
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | Taxa de Sucesso de Reserva |
| **Característica de Qualidade Relacionada** | Confiável |
| **Fórmula de Cálculo** | (Reservas confirmadas / tentativas de reservas válidas) * 100 |
| **Unidade de Medida** | % |
| **Meta ou valor de referência desejado** | >= 97% |

**Teste**
 |  ||
| -------- | ----- |
| **Nome do Teste** | Bloqueio de Reserva para Usuário não Registro |
| **Objetivo** | Garantir que apenas alunos registrados na universidade realizem reservas |
| **Pré-condições** | Usuário não ser registrado |
| **Passos para a execução** | 1- Aluno não registrado tentar reservar um livro |
| **Resultado esperado** | Sistema não permitir que este aluno faça uma reserva de livro |

---
### 3. Eficiente

**Como se aplica ao sistema**: *O tempo de exibição quando um aluno ou professor pesquisar um livro por título, autor ou assunto deve ser baixo*
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | Tempo Médio de Resposta de Busca |
| **Característica de Qualidade Relacionada** | Eficiente |
| **Fórmula de Cálculo** | Soma do tempo de resposta de cada busca / Número de buscas total |
| **Unidade de Medida** | Segundos |
| **Meta ou valor de referência desejado** | <= 3 segundos |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | Teste de Pesquisa |
| **Objetivo** | Verificar se a pesquisa retorna resultados dentro do tempo estimado |
| **Pré-condições** | O catálogo possuir livros cadastrados |
| **Passos para a execução** | 1- Pesquisar um livro por título 'X' <br> 2- Medir o tempo de resposta |
| **Resultado esperado** | O sistema deve retornar o resultado em até 3 segundos |

---
### 4. Íntegro

**Como se aplica ao sistema**: *Cada usuário (professor ou aluno) tem credenciais únicas providos pela universidade para acesso ao software*

**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | Tentativas de Login Inválidos |
| **Característica de Qualidade Relacionada** | Íntegro |
| **Fórmula de Cálculo** | Número de acessos negados por credenciais incorretas |
| **Unidade de Medida** | Contagem |
| **Meta ou valor de referência desejado** | <= 2 tentativas por dia |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | Login com Credenciais Incorretas |
| **Objetivo** | Garantir que pessoas sem credenciais não acessem o sistema |
| **Pré-condições** | Usuário não possuir credenciais únicas para acessar o sistema |
| **Passos para a execução** | 1- Abrir a página de login <br> 2- Inserir um login inexistente/incorreto <br> 3- Confirmar o acesso |
| **Resultado esperado** | O sistema retornar uma mensagem de acesso incorreto/inválido |

---
### 5. Fácil de Usar

**Como se aplica ao sistema**: *O software deve ter uma interface intuitiva*

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
### 6. Interoperável

**Como se aplica ao sistema**: *O sistema utiliza as mesma credenciais de acesso que a universidade possui (dispõe do mesmo banco de dados)*
 
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

**Como se aplica ao sistema**: *Cada funcionalidade terá seu serviço operando de forma individual*
 
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
| **Nome do Teste** | Validação de busca por autor |
| **Objetivo** | Verificar se a busca retorna obras de determinado autor corretamente |
| **Pré-condições** | O usuário colocar o autor que deseja e o sistema identificar o autor |
| **Passos para a execução** | 1- Inserir o nome do autor <br> 2- Executar a pesquisa <br> 3- Verificar os resultados |
| **Resultado esperado** | O sistema retornar uma lista de obras do autor escolhido |

---
### 2. Flexível

**Como se aplica ao sistema**: **
 
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
