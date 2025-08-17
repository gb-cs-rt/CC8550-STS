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
| **Nome da Métrica** | Sucesso de Tarefas |
| **Característica de Qualidade Relacionada** | Fácil de Usar |
| **Fórmula de Cálculo** | (Usuário de conseguem concluir uma tarefa / Usuários que tentaram realizar uma tarefa) * 100 |
| **Unidade de Medida** | % |
| **Meta ou valor de referência desejado** | >= 90% |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | Tentativa de Reserva |
| **Objetivo** | Verificar se usuários conseguem reservar um livro sem ajuda |
| **Pré-condições** | Possuir um livro para reserva |
| **Passos para a execução** | 1- Usuário realizar todo o processo de reserva de um livro <br> 2- Observar todo o processo até a finalização |
| **Resultado esperado** | Que pelo menos 95% dos usuários consigam reservar um livro sem nenhuma ajuda |

---
### 6. Interoperável

**Como se aplica ao sistema**: *O sistema utiliza as mesma credenciais de acesso que a universidade possui (dispõe do mesmo banco de dados)*
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | Erros de Sincronização |
| **Característica de Qualidade Relacionada** | Interoperável |
| **Fórmula de Cálculo** | Número de falhas ao consultar/validar dados no banco de dados da universidade |
| **Unidade de Medida** | Contagem |
| **Meta ou valor de referência desejado** | 0 falhas críticas por semana |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | Realizar Login com Credenciais da Universidade |
| **Objetivo** | Verfificar se o sistema aceita o login com usuário/senha já cadastrados na universidade |
| **Pré-condições** | Já possuir um cadastro ativo no sistema da universidade |
| **Passos para a execução** | 1- Acessar a tela de login <br> 2- Inserir usuário e senha válidos da universidade <br> 3- Confirmar o login |
| **Resultado esperado** | Conseguir acessar o sistema |

## Características de Manutenção

### 1. Manutenível

**Como se aplica ao sistema**: *Cada funcionalidade terá seu serviço operando de forma individual*
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | Tempo Médio de Correção de Erros |
| **Característica de Qualidade Relacionada** | Manutenível |
| **Fórmula de Cálculo** | Soma do tempo gasto para corrgir uma falha / número de falhas corrigidas |
| **Unidade de Medida** | Dias |
| **Meta ou valor de referência desejado** | <= 2 dias |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | Teste de Isolamento de Serviço |
| **Objetivo** | Garantir que ao modificar um serviço, os outros continuem funcionando normalmente |
| **Pré-condições** | Sistemas divididos em serviços independentes |
| **Passos para a execução** | 1- Alterar código de um serviço qualquer <br> 2- Verificar se os demais continuam funcionando |
| **Resultado esperado** | Apenas o serviço alterado devem ser afetado |

---
### 2. Flexível

**Como se aplica ao sistema**: *Permitir com que o bibliotecário possa alterar o prazo de um livro sem precisar reprogramá-lo*
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | Tempo para Alterar Prazo |
| **Característica de Qualidade Relacionada** | Flexível |
| **Fórmula de Cálculo** | Tempo necessário para alterar o prazo de devolução de um livro |
| **Unidade de Medida** | Minutos |
| **Meta ou valor de referência desejado** | <= 5 minutos |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | Alterar Prazo pelo Painel |
| **Objetivo** | Verificar se o bibliotecário consegue mudar o prazo de um livro sem precisar reprogramá-lo |
| **Pré-condições** | Estar logado com usuário de bibliotecário |
| **Passos para a execução** | 1- Acessar o painel administrativo <br> 2- Alterar o prazo de devolução <br> Salvar as configurações |
| **Resultado esperado** | O novo prazo passa a valer imediatamente |

---
### 3. Testável

**Como se aplica ao sistema**: *Poder testar separadamente cada funcionalidade*
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | Funcionalidades com Teste Automatizado |
| **Característica de Qualidade Relacionada** | Testável |
| **Fórmula de Cálculo** | (Quantidade de funcionalidades com testes automatizados / Total de funcionalidades) * 100 |
| **Unidade de Medida** | % |
| **Meta ou valor de referência desejado** | >= 90% |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | Teste de Reserva |
| **Objetivo** | Verificar o comportamento da função de reserva de livro isoladamente |
| **Pré-condições** | Estar em um ambiente de teste com dados fictícios |
| **Passos para a execução** | 1- Chamar uma função de reserva com livro disponível <br> 2- Chamar a mesma função de reserva, mas agora, sem livros disponíveis |
| **Resultado esperado** | Mostrar no primeiro caso uma fila de livros e no segundo caso mostrar que não há exemplares disponíveis |

---
### 4. Portável

**Como se aplica ao sistema**: *O sistema deve funcionar em diferentes dispositivos sem falhas* 
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | Problemas de Compatibilidade |
| **Característica de Qualidade Relacionada** | Portável |
| **Fórmula de Cálculo** | Quantidade de falhas específicas de dispositivo/navegador identificadas na baterias de testes |
| **Unidade de Medida** | Contagem |
| **Meta ou valor de referência desejado** | 0 falhas críticas por release |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | Funcionalidades Básicas em Múltiplos Dispositivos |
| **Objetivo** | Verificar se os usuários conseguem efetuar o login, buscar e reservar um livro em diferentes dispositivos |
| **Pré-condições** | Logar em diferentes dispositivos |
| **Passos para a execução** | 1- Efetuar login <br> 2- Pesquisar por um livro <br> 3- Reservar um livro |
| **Resultado esperado** | As 3 ações devem funcionar sem apresentar nenhum tipo de erro nos diferentes dispositivos testados |

---
### 5. Reutilizável

**Como se aplica ao sistema**: *O serviço de envio de notificações usado para lembretes de devolução também pode ser reaproveitado para avisar sobre confirmação de reservas ou outros comunicados* 
 
**Métrica**
 |||
| -------- | ----- |
| **Nome da Métrica** | Percentual de Reuso do Serviço de Notificação |
| **Característica de Qualidade Relacionada** | Reutilizável |
| **Fórmula de Cálculo** | (Números de funcionalidades que utilizam o mesmo serviço / Total de funcionalidades que precisam enviar notificações) * 100 |
| **Unidade de Medida** | % |
| **Meta ou valor de referência desejado** | >= 80% |

**Teste**
 |||
| -------- | ----- |
| **Nome do Teste** | Reuso do Serviço de Notificação em Diferentes Casos |
| **Objetivo** | Validar que o mesmo serviço de notificação funciona para lembretes de devolução e confirmaçao de reservas |
| **Pré-condições** | Serviço de notificação implementado |
| **Passos para a execução** | 1- Gerar lembrete de devolução <br> 2- Gerar confirmação de reserva <br> 3- Verificar se os lembretes foram enviado com sucesso |
| **Resultado esperado** | O mesmo serviço conseguir enviar corretamente os dois lembretes |


**Explique como essas métricas e testes garantem o bom funcionamento e a manutenção do sistema.**

As métricas e os testes definidos funcionam como uma forma de medir e validar continuamente a qualidade do sistema, garantindo que ele se mantenha confiável, eficiente e fácil de usar. As métricas permitem acompanhar de forma objetiva aspectos como tempo de resposta, taxa de erros ou sucesso em tarefas, ajudando a identificar pontos de melhoria antes que causem impacto aos usuários. Já os testes verificam na prática se cada funcionalidade está operando como esperado, simulando diferentes situações de uso (corretas, incorretas ou de falha). Juntos, eles asseguram que o sistema continue funcionando bem ao longo do tempo e que possa ser mantido e evoluído com segurança, evitando retrabalho e aumentando a confiança de alunos, professores e bibliotecários no uso da plataforma.
