import unittest
from src.calculadora import Calculadora

class TestIntegracao(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculadora()

    ## TESTE DE OPERACOES SEQUENCIAIS

    def test_operacoes_sequenciais(self):
        calc = Calculadora()
        # Sequencia: 2 + 3 = 5, depois 5 * 4 = 20, depois 20 / 2 = 10
        calc.somar(2, 3)
        resultado1 = calc.obter_ultimo_resultado()
        calc.multiplicar(resultado1, 4)
        resultado2 = calc.obter_ultimo_resultado()
        calc.dividir(resultado2, 2)
        resultado_final = calc.obter_ultimo_resultado()
        self.assertEqual(resultado_final, 10)
        self.assertEqual(len(calc.historico), 3)

    # Extra: operacoes sequenciais incorretas
    def test_operacoes_sequenciais_incorretas(self):
        calc = Calculadora()
        # Sequencia: 10 - 2 = 8, depois 8 ^ 2 = 64, depois 64 / 4 = 16
        calc.subtrair(10, 2)
        resultado1 = calc.obter_ultimo_resultado()
        calc.potencia(resultado1, 2)
        resultado2 = calc.obter_ultimo_resultado()
        calc.dividir(resultado2, 4)
        resultado_final = calc.obter_ultimo_resultado()
        self.assertEqual(resultado_final, 15)
        self.assertEqual(len(calc.historico), 3) 

    ## TESTE DE INTERFACE ENTRE METODOS

    def test_integracao_historico_resultado(self):
        calc = Calculadora()
        calc.potencia(2, 3)  # 2^3 = 8
        calc.somar(calc.obter_ultimo_resultado(), 2)  # 8 + 2 = 10
        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 ^ 3 = 8", calc.historico)
        self.assertIn("8 + 2 = 10", calc.historico)

    # Extra: continuar após limpar histórico usando o último resultado
    def test_integracao_limpar_historico_e_continuar(self):
        calc = Calculadora()
        calc.somar(5, 5)  # 10
        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)
        calc.multiplicar(calc.obter_ultimo_resultado(), 3)  # 30
        self.assertEqual(calc.obter_ultimo_resultado(), 30)
        self.assertEqual(len(calc.historico), 1)
        self.assertIn("10 * 3 = 30", calc.historico)

if __name__ == '__main__':
    unittest.main()
             
