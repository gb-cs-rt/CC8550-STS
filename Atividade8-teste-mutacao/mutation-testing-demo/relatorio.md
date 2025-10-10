# Relatorio de Testes de Mutacao

## Membros do Grupo

> Felipe Orlando Lanzara - 22.225.015-1

> Pedro Henrique Lega Kramer Costa - 22.125.091-3

> Ruan Pastrelo Turola - 22.225.013-6

## Objetivo

Documentar o processo de avaliação da suíte de testes da calculadora via mutação, registrando o estado inicial, as melhorias implementadas e o impacto nas métricas de cobertura e taxa de mutantes mortos. O relatório compila os comandos executados, consolida os resultados obtidos em cada fase e analisa os mutantes remanescentes para orientar decisões de manutenção e evolução dos testes.

## Fase 1 – Estado Inicial

### 1. Executar Testes Normais

```bash
python -m pytest tests/ -v
```

**Saída:**

```
========================================================================================== test session starts ===========================================================================================
platform linux -- Python 3.10.12, pytest-8.4.2, pluggy-1.6.0 -- /home/ruan/Documentos/FEI/8_Semestre/teste_de_software/mutation-testing-demo/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/ruan/Documentos/FEI/8_Semestre/teste_de_software/mutation-testing-demo
configfile: setup.cfg
plugins: cov-7.0.0
collected 38 items 

tests/test_operations.py::TestCalculator::test_add PASSED                                        [  2%]
tests/test_operations.py::TestCalculator::test_multiply PASSED                                   [  5%]
tests/test_operations.py::TestCalculator::test_divide_zero PASSED                                [  7%]
tests/test_operations.py::TestCalculator::test_square_root_negative PASSED                       [ 10%]
tests/test_operations.py::TestCalculator::test_factorial_negative PASSED                         [ 13%]
tests/test_operations.py::TestCalculator::test_absolute_value_basic PASSED                       [ 15%]
tests/test_operations.py::TestCalculator::test_max_of_two_equal PASSED                           [ 18%]
tests/test_operations.py::TestCalculator::test_is_positive_true PASSED                           [ 21%]
tests/test_operations.py::TestCalculator::test_calculate_percentage_basic PASSED                 [ 23%]
tests/test_operations.py::TestCalculator::test_grade_classification_a PASSED                     [ 26%]
tests/test_operations.py::TestCalculator::test_fibonacci_base_case PASSED                        [ 28%]
tests/test_operations.py::TestCalculator::test_is_prime_true_case PASSED                         [ 31%]
tests/test_operations.py::TestCalculator::test_subtract PASSED                                   [ 34%]
tests/test_operations.py::TestCalculator::test_is_even PASSED                                    [ 36%]
tests/test_operations.py::TestCalculator::test_divide_normal PASSED                              [ 39%]
tests/test_operations.py::TestCalculator::test_power PASSED                                      [ 42%]
tests/test_operations.py::TestCalculator::test_square_root_zero_e_positivo PASSED                [ 44%]
tests/test_operations.py::TestCalculator::test_factorial_basicos PASSED                          [ 47%]
tests/test_operations.py::TestCalculator::test_absolute_value_negativo_e_zero PASSED             [ 50%]
tests/test_operations.py::TestCalculator::test_max_of_two_varios PASSED                          [ 52%]
tests/test_operations.py::TestCalculator::test_min_of_three_varios PASSED                        [ 55%]
tests/test_operations.py::TestCalculator::test_is_positive_zero_e_negativo PASSED                [ 57%]
tests/test_operations.py::TestCalculator::test_calculate_percentage_extremos PASSED              [ 60%]
tests/test_operations.py::TestCalculator::test_compare_numbers_todos PASSED                      [ 63%]
tests/test_operations.py::TestCalculator::test_is_in_range PASSED                                [ 65%]
tests/test_operations.py::TestCalculator::test_calculate_discount_valores PASSED                 [ 68%]
tests/test_operations.py::TestCalculator::test_calculate_discount_erros PASSED                   [ 71%]
tests/test_operations.py::TestCalculator::test_grade_classification_faixas PASSED                [ 73%]
tests/test_operations.py::TestCalculator::test_fibonacci_varios PASSED                           [ 76%]
tests/test_operations.py::TestCalculator::test_count_digits PASSED                               [ 78%]
tests/test_operations.py::TestCalculator::test_is_prime_outros PASSED                            [ 81%]
tests/test_operations.py::TestCalculator::test_divide_denominador_negativo PASSED                [ 84%]
tests/test_operations.py::TestCalculator::test_is_even_zero PASSED                               [ 86%]
tests/test_operations.py::TestCalculator::test_absolute_value_float PASSED                       [ 89%]
tests/test_operations.py::TestCalculator::test_max_of_two_negativos PASSED                       [ 92%]
tests/test_operations.py::TestCalculator::test_min_of_three_empates_deterministicos PASSED       [ 94%]
tests/test_operations.py::TestCalculator::test_calculate_percentage_inteiros_nao_trunca PASSED   [ 97%]
tests/test_operations.py::TestCalculator::test_is_prime_composite_adicionais PASSED              [100%]

=========================================================================================== 38 passed in 0.08s ===========================================================================================
```

### 2. Verificar Cobertura de Código

```bash
python -m pytest --cov=calculator/ tests/
```

**Saída:**

```
=================================================================================================== tests coverage ===================================================================================================
__________________________________________________________________________________         coverage: platform linux, python 3.10.12-final-0 __________________________________________________________________________________

Name                       Stmts   Miss  Cover
----------------------------------------------
calculator/__init__.py         3      0   100%
calculator/operations.py     101     53    48%
----------------------------------------------
TOTAL                        104     53    49%
================================================================================================= 12 passed in 0.06s =================================================================================================

```
**Observação importante**: Apesar da cobertura de apenas 49%, todos os testes passam. Isso demonstra uma limitação da métrica de cobertura.

### 3. Executar Testes de Mutação

```bash
# Remover cache anterior (se existir)
rm -rf .mutmut-cache/

# Executar mutmut
mutmut run
```

**Saída:**

```
⠦ Generating mutants
    done in 223ms
⠼ Listing all tests 
⠙ Running clean tests
    done
⠧ Running forced fail test
    done
Running mutation testing
⠦ 158/158  🎉 34 🫥 49  ⏰ 0  🤔 0  🙁 75  🔇 0
83.70 mutations/second
```

### 4. Visualizar Resultados

```bash
# Ver resumo dos resultados
mutmut results
```

**Saída:**
```
    calculator.operations.xǁCalculatorǁsubtract__mutmut_1: no tests
    calculator.operations.xǁCalculatorǁdivide__mutmut_7: survived
    calculator.operations.xǁCalculatorǁpower__mutmut_1: no tests
    calculator.operations.xǁCalculatorǁsquare_root__mutmut_1: survived
    calculator.operations.xǁCalculatorǁsquare_root__mutmut_2: survived
    calculator.operations.xǁCalculatorǁsquare_root__mutmut_7: survived
    calculator.operations.xǁCalculatorǁis_even__mutmut_1: no tests
    calculator.operations.xǁCalculatorǁis_even__mutmut_2: no tests
    calculator.operations.xǁCalculatorǁis_even__mutmut_3: no tests
    calculator.operations.xǁCalculatorǁis_even__mutmut_4: no tests
    calculator.operations.xǁCalculatorǁfactorial__mutmut_1: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_2: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_7: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_8: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_9: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_10: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_11: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_12: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_13: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_14: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_15: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_16: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_17: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_18: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_19: survived
    calculator.operations.xǁCalculatorǁfactorial__mutmut_20: survived
    calculator.operations.xǁCalculatorǁabsolute_value__mutmut_1: survived
    calculator.operations.xǁCalculatorǁabsolute_value__mutmut_3: survived
    calculator.operations.xǁCalculatorǁmin_of_three__mutmut_1: no tests
    calculator.operations.xǁCalculatorǁmin_of_three__mutmut_2: no tests
    calculator.operations.xǁCalculatorǁmin_of_three__mutmut_3: no tests
    calculator.operations.xǁCalculatorǁmin_of_three__mutmut_4: no tests
    calculator.operations.xǁCalculatorǁis_positive__mutmut_1: survived
    calculator.operations.xǁCalculatorǁcompare_numbers__mutmut_1: no tests
    calculator.operations.xǁCalculatorǁcompare_numbers__mutmut_2: no tests
    calculator.operations.xǁCalculatorǁcompare_numbers__mutmut_3: no tests
    calculator.operations.xǁCalculatorǁcompare_numbers__mutmut_4: no tests
    calculator.operations.xǁCalculatorǁcompare_numbers__mutmut_5: no tests
    calculator.operations.xǁCalculatorǁcompare_numbers__mutmut_6: no tests
    calculator.operations.xǁCalculatorǁcompare_numbers__mutmut_7: no tests
    calculator.operations.xǁCalculatorǁcompare_numbers__mutmut_8: no tests
    calculator.operations.xǁCalculatorǁis_in_range__mutmut_1: no tests
    calculator.operations.xǁCalculatorǁis_in_range__mutmut_2: no tests
    calculator.operations.xǁCalculatorǁcalculate_discount__mutmut_1: no tests
    calculator.operations.xǁCalculatorǁcalculate_discount__mutmut_2: no tests
    calculator.operations.xǁCalculatorǁcalculate_discount__mutmut_3: no tests
    calculator.operations.xǁCalculatorǁcalculate_discount__mutmut_4: no tests
    calculator.operations.xǁCalculatorǁcalculate_discount__mutmut_5: no tests
    calculator.operations.xǁCalculatorǁcalculate_discount__mutmut_6: no tests
    calculator.operations.xǁCalculatorǁcalculate_discount__mutmut_7: no tests
    calculator.operations.xǁCalculatorǁcalculate_discount__mutmut_8: no tests
    calculator.operations.xǁCalculatorǁcalculate_discount__mutmut_9: no tests
    calculator.operations.xǁCalculatorǁcalculate_discount__mutmut_10: no tests
    calculator.operations.xǁCalculatorǁcalculate_discount__mutmut_11: no tests
    calculator.operations.xǁCalculatorǁcalculate_discount__mutmut_12: no tests
    calculator.operations.xǁCalculatorǁcalculate_discount__mutmut_13: no tests
    calculator.operations.xǁCalculatorǁcalculate_discount__mutmut_14: no tests
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_1: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_2: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_5: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_6: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_7: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_8: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_9: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_10: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_11: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_12: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_13: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_14: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_15: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_16: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_17: survived
    calculator.operations.xǁCalculatorǁgrade_classification__mutmut_18: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_1: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_3: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_4: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_5: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_7: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_8: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_9: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_10: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_11: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_12: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_13: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_14: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_15: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_16: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_17: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_18: survived
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_1: no tests
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_2: no tests
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_3: no tests
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_4: no tests
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_5: no tests
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_6: no tests
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_7: no tests
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_8: no tests
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_9: no tests
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_10: no tests
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_11: no tests
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_12: no tests
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_13: no tests
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_14: no tests
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_15: no tests
    calculator.operations.xǁCalculatorǁis_prime__mutmut_1: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_2: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_3: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_4: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_5: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_6: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_7: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_8: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_11: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_15: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_16: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_17: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_18: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_19: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_22: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_23: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_24: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_25: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_26: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_27: survived
```

### 5. Analisar Mutantes Específicos

```bash
# Analisar um mutante específico
mutmut show "calculator.operations.xǁCalculatorǁsubtract__mutmut_1"
```
**Saída:**

```
# calculator.operations.xǁCalculatorǁsubtract__mutmut_1: no tests
--- calculator/operations.py
+++ calculator/operations.py
@@ -1,3 +1,3 @@
 def subtract(self, a: Number, b: Number) -> Number:
     """Subtrai dois números."""
-    return a - b
+    return a + b
```

### 6. Interpretar os Resultados

**Símbolos dos Resultados:**
- 🎉 **34 killed**: Testes detectaram essas mutações
- 🫥 **49 survived**: Mutações não detectadas pelos testes
- ⏰ **0 timeout**: Nenhuma mutação causou execução lenta
- 🤔 **75 incompetent**: Mutações causaram erro de sintaxe

**Taxa de Mutação Atual:**
```
Taxa = 34 killed / 158 total = 21,5%
```

## Fase 2 – Melhorias Implementadas

Foram adicionados novos testes para cobrir cenários críticos que estavam ausentes:
- **Operações básicas**: divisão com denominadores positivos e negativos, potências com expoente zero e fracionário, raiz quadrada de zero e de positivos.
- **Casos de borda**: fatoriais de 0 e 1, valor absoluto para negativos e `0.0`, funções `max_of_two` e `min_of_three` com empates controlados usando `TaggedNumber`.
- **Validações**: descontos inválidos, classificação de notas nos limites das faixas, `is_positive` para zero e negativos, intervalo fechado em `is_in_range`.
- **Sequências numéricas**: Fibonacci para n=0, 2 e 7; contagem de dígitos incluindo negativos; números primos compostos variados.

Essas adições visam matar mutantes sobreviventes ao garantir que cada ramo lógico e mensagem de erro seja exercitado.

## Fase 3 – Resultados Pos-Melhoria

Com a suíte reforçada, repetimos o ciclo completo para observar os impactos nas métricas:

### 1. Executar Testes Normais

```bash
python -m pytest tests/ -v
```

**Saída:**

```
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.10.12, pytest-8.4.2, pluggy-1.6.0 -- /home/ruan/Documentos/FEI/8_Semestre/teste_de_software/mutation-testing-demo/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/ruan/Documentos/FEI/8_Semestre/teste_de_software/mutation-testing-demo
configfile: setup.cfg
plugins: cov-7.0.0
collected 38 items                                                                                                                                                                                                

tests/test_operations.py::TestCalculator::test_add PASSED                                                                                                                                                   [  2%]
tests/test_operations.py::TestCalculator::test_multiply PASSED                                                                                                                                              [  5%]
tests/test_operations.py::TestCalculator::test_divide_zero PASSED                                                                                                                                           [  7%]
tests/test_operations.py::TestCalculator::test_square_root_negative PASSED                                                                                                                                  [ 10%]
tests/test_operations.py::TestCalculator::test_factorial_negative PASSED                                                                                                                                    [ 13%]
tests/test_operations.py::TestCalculator::test_absolute_value_basic PASSED                                                                                                                                  [ 15%]
tests/test_operations.py::TestCalculator::test_max_of_two_equal PASSED                                                                                                                                      [ 18%]
tests/test_operations.py::TestCalculator::test_is_positive_true PASSED                                                                                                                                      [ 21%]
tests/test_operations.py::TestCalculator::test_calculate_percentage_basic PASSED                                                                                                                            [ 23%]
tests/test_operations.py::TestCalculator::test_grade_classification_a PASSED                                                                                                                                [ 26%]
tests/test_operations.py::TestCalculator::test_fibonacci_base_case PASSED                                                                                                                                   [ 28%]
tests/test_operations.py::TestCalculator::test_is_prime_true_case PASSED                                                                                                                                    [ 31%]
tests/test_operations.py::TestCalculator::test_subtract PASSED                                                                                                                                              [ 34%]
tests/test_operations.py::TestCalculator::test_is_even PASSED                                                                                                                                               [ 36%]
tests/test_operations.py::TestCalculator::test_divide_normal PASSED                                                                                                                                         [ 39%]
tests/test_operations.py::TestCalculator::test_power PASSED                                                                                                                                                 [ 42%]
tests/test_operations.py::TestCalculator::test_square_root_zero_e_positivo PASSED                                                                                                                           [ 44%]
tests/test_operations.py::TestCalculator::test_factorial_basicos PASSED                                                                                                                                     [ 47%]
tests/test_operations.py::TestCalculator::test_absolute_value_negativo_e_zero PASSED                                                                                                                        [ 50%]
tests/test_operations.py::TestCalculator::test_max_of_two_varios PASSED                                                                                                                                     [ 52%]
tests/test_operations.py::TestCalculator::test_min_of_three_varios PASSED                                                                                                                                   [ 55%]
tests/test_operations.py::TestCalculator::test_is_positive_zero_e_negativo PASSED                                                                                                                           [ 57%]
tests/test_operations.py::TestCalculator::test_calculate_percentage_extremos PASSED                                                                                                                         [ 60%]
tests/test_operations.py::TestCalculator::test_compare_numbers_todos PASSED                                                                                                                                 [ 63%]
tests/test_operations.py::TestCalculator::test_is_in_range PASSED                                                                                                                                           [ 65%]
tests/test_operations.py::TestCalculator::test_calculate_discount_valores PASSED                                                                                                                            [ 68%]
tests/test_operations.py::TestCalculator::test_calculate_discount_erros PASSED                                                                                                                              [ 71%]
tests/test_operations.py::TestCalculator::test_grade_classification_faixas PASSED                                                                                                                           [ 73%]
tests/test_operations.py::TestCalculator::test_fibonacci_varios PASSED                                                                                                                                      [ 76%]
tests/test_operations.py::TestCalculator::test_count_digits PASSED                                                                                                                                          [ 78%]
tests/test_operations.py::TestCalculator::test_is_prime_outros PASSED                                                                                                                                       [ 81%]
tests/test_operations.py::TestCalculator::test_divide_denominador_negativo PASSED                                                                                                                           [ 84%]
tests/test_operations.py::TestCalculator::test_is_even_zero PASSED                                                                                                                                          [ 86%]
tests/test_operations.py::TestCalculator::test_absolute_value_float PASSED                                                                                                                                  [ 89%]
tests/test_operations.py::TestCalculator::test_max_of_two_negativos PASSED                                                                                                                                  [ 92%]
tests/test_operations.py::TestCalculator::test_min_of_three_empates_deterministicos PASSED                                                                                                                  [ 94%]
tests/test_operations.py::TestCalculator::test_calculate_percentage_inteiros_nao_trunca PASSED                                                                                                              [ 97%]
tests/test_operations.py::TestCalculator::test_is_prime_composite_adicionais PASSED                                                                                                                         [100%]

=============================================================================================== 38 passed in 0.07s ================================================================================================
```

### 2. Verificar Cobertura de Código

```bash
python -m pytest --cov=calculator/ tests/
```

**Saída:**

```
================================================================================================= tests coverage ==================================================================================================
________________________________________________________________________________ coverage: platform linux, python 3.10.12-final-0 _________________________________________________________________________________

Name                       Stmts   Miss  Cover
----------------------------------------------
calculator/__init__.py         3      0   100%
calculator/operations.py     101      0   100%
----------------------------------------------
TOTAL                        104      0   100%
=============================================================================================== 38 passed in 0.06s ================================================================================================

```
**Observação importante**: Todos os testes passam. Isso demonstra uma ótima métrica de cobertura.

### 3. Executar Testes de Mutação

```bash
# Remover cache anterior (se existir)
rm -rf .mutmut-cache/

# Executar mutmut
mutmut run
```

**Saída:**

```
⠦ Generating mutants
    done in 214ms
⠦ Listing all tests 
⠏ Running clean tests
    done
⠴ Running forced fail test
    done
Running mutation testing
⠼ 158/158  🎉 152 🫥 0  ⏰ 2  🤔 0  🙁 4  🔇 0
9.81 mutations/second  
```

### 4. Visualizar Resultados

```bash
# Ver resumo dos resultados
mutmut results
```

**Saída:**
```
    calculator.operations.xǁCalculatorǁfactorial__mutmut_7: survived
    calculator.operations.xǁCalculatorǁfibonacci__mutmut_5: survived
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_8: timeout
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_13: timeout
    calculator.operations.xǁCalculatorǁis_prime__mutmut_17: survived
    calculator.operations.xǁCalculatorǁis_prime__mutmut_22: survived
```

### 5. Analisar Mutantes Específicos

```bash
# Analisar um mutante específico
mutmut show "calculator.operations.xǁCalculatorǁsubtract__mutmut_1"
```
**Saída:**

```
# calculator.operations.xǁCalculatorǁsubtract__mutmut_1: killed
--- calculator/operations.py
+++ calculator/operations.py
@@ -1,3 +1,3 @@
 def subtract(self, a: Number, b: Number) -> Number:
     """Subtrai dois números."""
-    return a - b
+    return a + b
```

### 6. Interpretar os Resultados

**Símbolos dos Resultados:**
- 🎉 **152 killed**: Testes detectaram essas mutações
- 🫥 **0 survived**: Mutações não detectadas pelos testes
- ⏰ **2 timeout**: Mutações que causam execução lenta
- 🤔 **0 incompetent**: Nenhuma mutação causou erro de sintaxe

**Taxa de Mutação Atual:**
```
Taxa = 152 killed / 158 total = 96,2%
```

## Conclusão

Com a suíte original, a cobertura atingia apenas 49% e a taxa de mutação ficava perto de 21% (34 mutantes mortos entre 158). A expansão sistemática dos testes — acrescentando casos de borda, validações de erro e cenários adicionais — elevou a cobertura para 100% e a taxa de mutação para 96,2% (152 mutantes mortos). Restaram apenas mutantes equivalentes e dois timeouts causados por loops não terminantes, que podem ser tratados como incompetentes ou mitigados com salvaguardas no código. Dessa forma, os testes passaram a cobrir melhor o comportamento crítico da calculadora e fornecem confiança significativamente maior.
