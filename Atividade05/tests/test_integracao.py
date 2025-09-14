## teste de entrada e saida 

def test_entrada_saida_soma(self):
    calc = Calculadora()
    resultado = calc.somar(5, 3)
    self.assertEqual(resultado, 8)
    self.assertEqual(calc.obter_ultimo_resultado(), 8)
