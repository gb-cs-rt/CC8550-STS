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

    # Extra: entrada/saída com floats e negativos
    def test_entrada_saida_misto_float_negativo(self):
        calc = Calculadora()
        resultado = calc.somar(-2.5, 0.5)
        self.assertEqual(resultado, -2.0)
        self.assertEqual(calc.obter_ultimo_resultado(), -2.0)

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

    # Extra: Tipos estruturados inválidos
    def test_tipagem_invalida_estruturas(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar([1, 2], 3)
        with self.assertRaises(TypeError):
            calc.multiplicar({"a": 1}, 2)

    # Extra: Booleanos são aceitos como números (bool é subclass de int em Python)
    def test_tipagem_booleana_deve_ser_rejeitada(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar(True, 3)
        with self.assertRaises(TypeError):
            calc.multiplicar(False, 10)

    ## TESTE DE CONSISTENCIA

    def test_consistencia_historico(self):
        calc = Calculadora()
        calc.somar(2, 3)
        calc.multiplicar(4, 5)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 + 3 = 5", calc.historico)
        self.assertIn("4 * 5 = 20", calc.historico)

    # Extra: formatação de floats no histórico: 0.1 + 0.2 deveria registrar 0.3.
    def test_formatacao_decimal_no_historico(self):
        calc = Calculadora()
        calc.somar(0.1, 0.2)
        self.assertIn("0.1 + 0.2 = 0.3", calc.historico)

    # Extra: Ordem exata do histórico
    def test_consistencia_ordem_historico(self):
        calc = Calculadora()
        calc.subtrair(10, 4)
        calc.dividir(12, 3)
        esperado = [
            "10 - 4 = 6",
            "12 / 3 = 4.0",
        ]
        self.assertEqual(calc.historico, esperado)

    ## TESTE DE INICIALIZACAO

    def teste_inicializacao(self):
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)
        self.assertEqual(len(calc.historico), 0)

    # Extra: Inicialização independente entre instâncias
    def test_inicializacao_instancias_independentes(self):
        a = Calculadora()
        b = Calculadora()
        a.somar(1, 2)
        self.assertEqual(len(a.historico), 1)
        self.assertEqual(len(b.historico), 0)

    ## TESTE DE MODIFICACAO DE DADOS

    def test_modificacao_historico(self):
        calc = Calculadora()
        calc.somar(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

    # Extra: encapsulamento do histórico: não deve poder ser mutado externamente.
    def test_historico_nao_deve_poder_ser_mutado_externamente(self):
        calc = Calculadora()
        calc.somar(1, 2)
        tamanho_antes = len(calc.historico)
        # Mutação externa indevida
        calc.historico.append("insercao indevida")
        self.assertEqual(len(calc.historico), tamanho_antes)

    # Extra: limpar histórico não altera resultado
    def test_limpar_historico_preserva_resultado(self):
        calc = Calculadora()
        calc.multiplicar(3, 3)
        self.assertEqual(calc.obter_ultimo_resultado(), 9)
        calc.limpar_historico()
        self.assertEqual(calc.obter_ultimo_resultado(), 9)

    ## TESTE DE LIMITE INFERIOR

    def test_limite_inferior(self):
        calc = Calculadora()
        # teste com zero
        resultado = calc.somar(0, 5)
        self.assertEqual(resultado, 5)
        # Teste com numeros negativos muito pequenos
        resultado = calc.multiplicar(-1e-10, 2)
        self.assertEqual(resultado, -2e-10)

    # Extra: potencia com expoente zero
    def test_limite_inferior_potencia_expoente_zero(self):
        calc = Calculadora()
        resultado = calc.potencia(5, 0)
        self.assertEqual(resultado, 1)

    ## TESTE DE LIMITE SUPERIOR

    def test_limite_superior(self):
        calc = Calculadora()
        # Teste com numeros  grandes
        resultado = calc.somar(1e10, 1e10)
        self.assertEqual(resultado, 2e10)

    def test_limite_superior_float(self):
        calc = Calculadora()
        resultado = calc.somar(1e308, 1e308)
        self.assertEqual(resultado, float("inf"))

    # Extra: multiplicação que estoura para infinito
    def test_limite_superior_multiplicacao_inf(self):
        calc = Calculadora()
        resultado = calc.multiplicar(1e308, 2)
        self.assertEqual(resultado, float("inf"))

    ## TESTE DE VALORES FORA DO INTERVALO 

    def test_divisao_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    # Extra: potência com base negativa e expoente fracionário deve gerar erro (não real).
    def test_potencia_base_negativa_expoente_fracionario(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.potencia(-8, 1/3)

    # Extra: NaN/Inf devem ser rejeitados para evitar resultados não finitos.
    def test_rejeitar_nan_e_inf(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.somar(float('nan'), 1)
        with self.assertRaises(ValueError):
            calc.subtrair(1, float('inf'))
        with self.assertRaises(ValueError):
            calc.dividir(1, float('-inf'))

    # Extra: divisão por zero em float
    def test_divisao_por_zero_float(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0.0)

    ## TESTE DE FLUXOS DE CONTROLE 

    def test_fluxos_divisao(self):
        calc = Calculadora()
        # Caminho normal
        resultado = calc.dividir(10, 2)
        self.assertEqual(resultado, 5)
        # Caminho de erro
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    # Extra: fluxo com números negativos
    def test_fluxos_divisao_negativos(self):
        calc = Calculadora()
        resultado = calc.dividir(-9, 3)
        self.assertEqual(resultado, -3)

    ## TESTE DE MENSAGENS DE ERRO

    def test_mensagens_erro(self):
        calc = Calculadora()
        try:
            calc.dividir(5, 0)
        except ValueError as e:
            self.assertEqual(str(e), "Divisão por zero nao permitida")

    # Extra: mensagem de erro com divisor float
    def test_mensagens_erro_float(self):
        calc = Calculadora()
        with self.assertRaises(ValueError) as ctx:
            calc.dividir(5, 0.0)
        self.assertEqual(str(ctx.exception), "Divisão por zero nao permitida")

if __name__ == '__main__':
    unittest.main()
