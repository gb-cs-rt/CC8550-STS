"""Testes para as operações da calculadora - Versão estrategicamente enfraquecida."""

import math

import pytest
from calculator import Calculator


class TaggedNumber(int):
    """Inteiro com rótulo para validar qual instância é retornada."""

    def __new__(cls, value: int, tag: str):
        obj = int.__new__(cls, value)
        obj.tag = tag
        return obj


class TestCalculator:
    """Testes para a classe Calculator."""

    def setup_method(self):
        """Configuração executada antes de cada teste."""
        self.calc = Calculator()

    def test_add(self):
        """Testa a operação de soma - apenas um caso."""
        assert self.calc.add(2, 3) == 5

    def test_multiply(self):
        """Testa a operação de multiplicação - apenas um caso."""
        assert self.calc.multiply(2, 3) == 6

    def test_divide_zero(self):
        """Testa apenas divisão por zero."""
        with pytest.raises(ValueError) as exc:
            self.calc.divide(5, 0)
        assert str(exc.value) == "Divisão por zero não é permitida"

    def test_square_root_negative(self):
        """Testa apenas raiz de número negativo."""
        with pytest.raises(ValueError) as exc:
            self.calc.square_root(-1)
        assert str(exc.value) == "Raiz quadrada de número negativo não é real"

    def test_factorial_negative(self):
        """Testa apenas fatorial de número negativo."""
        with pytest.raises(ValueError) as exc:
            self.calc.factorial(-1)
        assert str(exc.value) == "Fatorial não definido para números negativos"

    def test_absolute_value_basic(self):
        """Testa valor absoluto apenas para números positivos."""
        assert self.calc.absolute_value(5) == 5
        assert self.calc.absolute_value(0.3) == pytest.approx(0.3)

    def test_max_of_two_equal(self):
        """Testa max apenas quando números são iguais."""
        primeiro = TaggedNumber(5, "primeiro")
        segundo = TaggedNumber(5, "segundo")
        assert self.calc.max_of_two(primeiro, segundo) is segundo

    def test_is_positive_true(self):
        """Testa is_positive apenas para números positivos."""
        assert self.calc.is_positive(10) is True
        assert self.calc.is_positive(1) is True
        assert self.calc.is_positive(0.1) is True

    def test_calculate_percentage_basic(self):
        """Testa porcentagem apenas para um caso simples."""
        assert self.calc.calculate_percentage(100, 10) == 10.0

    def test_grade_classification_a(self):
        """Testa classificação apenas para nota A."""
        assert self.calc.grade_classification(95) == "A"

    def test_fibonacci_base_case(self):
        """Testa Fibonacci apenas para caso base."""
        assert self.calc.fibonacci(1) == 1

    def test_is_prime_true_case(self):
        """Testa is_prime apenas para um número primo."""
        assert self.calc.is_prime(7) is True

    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(1, 1) == 0

    def test_is_even(self):
        assert self.calc.is_even(2) is True
        assert self.calc.is_even(3) is False

    # NOVOS TESTES ADICIONADOS

    def test_divide_normal(self):
        assert self.calc.divide(6, 3) == 2
        assert self.calc.divide(-9, 3) == -3

    def test_power(self):
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(9, 0.5) == 3

    def test_square_root_zero_e_positivo(self):
        assert self.calc.square_root(0) == 0
        assert self.calc.square_root(25) == 5

    def test_factorial_basicos(self):
        assert self.calc.factorial(0) == 1
        assert self.calc.factorial(1) == 1
        assert self.calc.factorial(2) == 2
        assert self.calc.factorial(5) == 120

    def test_absolute_value_negativo_e_zero(self):
        assert self.calc.absolute_value(-7) == 7
        assert self.calc.absolute_value(0) == 0
        zero_float = self.calc.absolute_value(0.0)
        assert math.copysign(1, zero_float) == 1.0

    def test_max_of_two_varios(self):
        assert self.calc.max_of_two(10, 5) == 10  # a > b
        assert self.calc.max_of_two(3, 8) == 8   # a < b

    def test_min_of_three_varios(self):
        assert self.calc.min_of_three(1, 2, 3) == 1  # primeiro é o menor
        assert self.calc.min_of_three(3, 1, 2) == 1  # segundo é o menor
        assert self.calc.min_of_three(3, 2, 1) == 1  # terceiro é o menor
        assert self.calc.min_of_three(2, 2, 3) == 2  # empate
        assert self.calc.min_of_three(3, 2, 2) == 2  # empate
        assert self.calc.min_of_three(2, 5, 1) == 1  # garante avaliação correta quando apenas uma comparação é verdadeira

    def test_is_positive_zero_e_negativo(self):
        assert self.calc.is_positive(0) is False
        assert self.calc.is_positive(-1) is False

    def test_calculate_percentage_extremos(self):
        assert self.calc.calculate_percentage(100, 0) == 0
        assert self.calc.calculate_percentage(200, 50) == 100

    def test_compare_numbers_todos(self):
        assert self.calc.compare_numbers(5, 3) == "maior"
        assert self.calc.compare_numbers(3, 5) == "menor"
        assert self.calc.compare_numbers(7, 7) == "igual"

    def test_is_in_range(self):
        assert self.calc.is_in_range(5, 1, 10) is True  # dentro
        assert self.calc.is_in_range(1, 1, 10) is True  # limite inferior
        assert self.calc.is_in_range(10, 1, 10) is True  # limite superior
        assert self.calc.is_in_range(0, 1, 10) is False  # fora
        assert self.calc.is_in_range(11, 1, 10) is False  # fora

    def test_calculate_discount_valores(self):
        assert self.calc.calculate_discount(100, 0) == 100
        assert self.calc.calculate_discount(100, 25) == 75
        assert self.calc.calculate_discount(100, 100) == 0

    def test_calculate_discount_erros(self):
        with pytest.raises(ValueError) as exc:
            self.calc.calculate_discount(100, -1)
        assert str(exc.value) == "Desconto deve estar entre 0 e 100"
        with pytest.raises(ValueError) as exc:
            self.calc.calculate_discount(100, 101)
        assert str(exc.value) == "Desconto deve estar entre 0 e 100"

    def test_grade_classification_faixas(self):
        assert self.calc.grade_classification(90) == "A"
        assert self.calc.grade_classification(89) == "B"
        assert self.calc.grade_classification(80) == "B"
        assert self.calc.grade_classification(79) == "C"
        assert self.calc.grade_classification(70) == "C"
        assert self.calc.grade_classification(69) == "D"
        assert self.calc.grade_classification(60) == "D"
        assert self.calc.grade_classification(59) == "F"

    def test_fibonacci_varios(self):
        assert self.calc.fibonacci(0) == 0
        assert self.calc.fibonacci(2) == 1
        assert self.calc.fibonacci(7) == 13

    def test_count_digits(self):
        assert self.calc.count_digits(0) == 1
        assert self.calc.count_digits(5) == 1
        assert self.calc.count_digits(12345) == 5
        assert self.calc.count_digits(-987) == 3

    def test_is_prime_outros(self):
        assert self.calc.is_prime(0) is False
        assert self.calc.is_prime(1) is False
        assert self.calc.is_prime(2) is True
        assert self.calc.is_prime(4) is False
        assert self.calc.is_prime(9) is False
        assert self.calc.is_prime(97) is True

    def test_divide_denominador_negativo(self):
        assert self.calc.divide(6, -3) == -2
        assert self.calc.divide(-6, -3) == 2

    def test_is_even_zero(self):
        assert self.calc.is_even(0) is True

    def test_absolute_value_float(self):
        assert self.calc.absolute_value(-3.5) == 3.5

    def test_max_of_two_negativos(self):
        assert self.calc.max_of_two(-1, -5) == -1
        assert self.calc.max_of_two(-5, -1) == -1

    def test_min_of_three_empates_deterministicos(self):
        a = TaggedNumber(5, "a")
        b = TaggedNumber(2, "b")
        c = TaggedNumber(2, "c")
        assert self.calc.min_of_three(a, b, c) is b
        menor_a = TaggedNumber(1, "a")
        menor_b = TaggedNumber(1, "b")
        maior_c = TaggedNumber(3, "c")
        assert self.calc.min_of_three(menor_a, menor_b, maior_c) is menor_a
        igual_c = TaggedNumber(1, "c")
        assert self.calc.min_of_three(menor_a, TaggedNumber(2, "b"), igual_c) is menor_a

    def test_calculate_percentage_inteiros_nao_trunca(self):
        assert self.calc.calculate_percentage(45, 10) == 4.5

    def test_is_prime_composite_adicionais(self):
        assert self.calc.is_prime(21) is False
        assert self.calc.is_prime(25) is False
        assert self.calc.is_prime(91) is False 
