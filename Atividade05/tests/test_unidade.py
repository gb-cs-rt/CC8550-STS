import unittest
from src.calculadora import Calculadora

class TestUnidade(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    ## TESTE DE ENTRADA E SAIDA 

    def test_entrada_saida_soma(self):
        calc = Calculadora()
        resultado = calc.somar(5, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)

    def test_entrada_saida_subtracao(self):
        calc = Calculadora()
        resultado = calc.subtrair(5, 3)
        self.assertEqual(resultado, 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 2)

    def test_entrada_saida_multiplicacao(self):
        calc = Calculadora()
        resultado = calc.multiplicar(5, 3)
        self.assertEqual(resultado, 15)
        self.assertEqual(calc.obter_ultimo_resultado(), 15)

    def test_entrada_saida_divisao(self):
        calc = Calculadora()
        resultado = calc.dividir(6, 3)
        self.assertEqual(resultado, 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 2)

    def test_entrada_saida_potencia(self):
        calc = Calculadora()
        resultado = calc.potencia(2, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)

    ## TESTE DE TIPAGEM

    def test_tipagem_invalida(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar("5", 3)  # String no lugar de número
        with self.assertRaises(TypeError):
            calc.dividir(10, None)  # None no lugar de número

    def test_tipagem_invalida_soma(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar("5", 3)  # String no lugar de número
        with self.assertRaises(TypeError):
            calc.somar(5, None)  # None no lugar de número

    def test_tipagem_invalida_subtracao(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.subtrair("5", 3)  # String no lugar de número
        with self.assertRaises(TypeError):
            calc.subtrair(5, None)  # None no lugar de número

    def test_tipagem_invalida_multiplicacao(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.multiplicar("5", 3)  # String no lugar de número
        with self.assertRaises(TypeError):
            calc.multiplicar(5, None)  # None no lugar de número

    def test_tipagem_invalida_divisao(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.dividir("5", 3)  # String no lugar de número
        with self.assertRaises(TypeError):
            calc.dividir(5, None)  # None no lugar de número

    def test_tipagem_invalida_potencia(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.potencia("2", 3)  # String no lugar de número
        with self.assertRaises(TypeError):
            calc.potencia(2, None)  # None no lugar de número

    ## TESTE DE CONSISTENCIA

    def test_consistencia_historico(self):
        calc = Calculadora()
        calc.somar(2, 3)
        calc.multiplicar(4, 5)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 + 3 = 5", calc.historico)
        self.assertIn("4 * 5 = 20", calc.historico)

    ## TESTE DE INICIALIZACAO

    def teste_inicializacao(self):
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)
        self.assertEqual(len(calc.historico), 0)

    ## TESTE DE MODIFICACAO DE DADOS

    def test_modificacao_historico(self):
        calc = Calculadora()
        calc.somar(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

    ## TESTE DE LIMITE INFERIOR

    def test_limite_inferior(self):
        calc = Calculadora()
        # teste com zero
        resultado = calc.somar(0, 5)
        self.assertEqual(resultado, 5)
        # Teste com numeros negativos muito pequenos
        resultado = calc.multiplicar(-1e-10, 2)
        self.assertEqual(resultado, -2e-10)

    ## TESTE DE LIMITE SUPERIOR

    def test_limite_superior(self):
        calc = Calculadora()
        # Teste com numeros  grandes
        resultado = calc.somar(1e10, 1e10)
        self.assertEqual(resultado, 2e10)

    # NAO SEI SE TA CERTO
    def test_limite_superior_float(self):
        calc = Calculadora()
        resultado = calc.somar(1e308, 1e308)
        self.assertEqual(resultado, float("inf"))

    ## TESTE DE VALORES FORA DO INTERVALO 

    def test_divisao_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    ## TESTE DE FLUXOS DE CONTROLE 

    def test_fluxos_divisao(self):
        calc = Calculadora()
        # Caminho normal
        resultado = calc.dividir(10, 2)
        self.assertEqual(resultado, 5)
        # Caminho de erro
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    ## TESTE DE MENSAGENS DE ERRO

    def test_mensagens_erro(self):
        calc = Calculadora()
        try:
            calc.dividir(5, 0)
        except ValueError as e:
            self.assertEqual(str(e), "Divisão por zero nao permitida")
