# Exercicio de avaliacao de expressao aritmetica.
# So podem ser usadas as estruturas Pilha e Fila implementadas em aulas anteriores.
# Deve ser analise de tempo e espaco para funcao avaliacao


from aula04.Pilha import Pilha
from aula05.Fila import Fila

def num(s):
    try:
        s = int(s)
        return True
    except ValueError:
        return False

class ErroLexico(Exception):
    pass


class ErroSintatico(Exception):
    pass


def analise_lexica(expressao):
    def caracteres(param1):
        return param1 in "(){.}[]+-*/"

    fila = Fila()
    count = 0
    pilha = Pilha()
    while count != len(expressao):
        if not (caracteres(expressao[count]) or num(expressao[count])):
            raise ErroLexico
        else:
            if caracteres(expressao[count]):
                if not pilha.vazia():
                    fila.enfileirar(pilha.desempilhar())
                fila.enfileirar(expressao[count])
            if num(expressao[count]):
                if pilha.vazia():
                    pilha.empilhar(expressao[count])
                else:
                    final = pilha.desempilhar()
                    pilha.empilhar(final + expressao[count])
        count += 1
    if not pilha.vazia():
        fila.enfileirar(pilha.desempilhar())
    return fila


def analise_sintatica(fila):
    novafila = Fila()
    if fila.vazia():
        raise ErroSintatico;
    save = ''
    while not fila.vazia():
        item = fila.desenfileirar()
        if num(item):
            save = int(item)
            if fila.vazia():
                novafila.enfileirar(save)
                return novafila
            if fila.primeiro() != '.':
                novafila.enfileirar(save)
        elif item == '.':
            item = fila.desenfileirar()
            save = float(save)
            save += (float(item)) / (10 ** (len(item)))
            novafila.enfileirar(save)
        else:
            novafila.enfileirar(item)
    return novafila


def avaliar(expressao):
    fila = analise_sintatica(analise_lexica(expressao))
    resultado = Pilha()
    if fila.vazia():
        raise ErroSintatico
    if fila.__len__()== 1:
        return fila.desenfileirar()
    for elemento in fila:
        resultado.empilhar(elemento)
        if resultado.__len__() >=3:
            v1 = resultado.desempilhar()
            v2 = resultado.desempilhar()
            v3 = resultado.desempilhar()
            if num(v1) and v2 in '+/*-' and num(v3):
                if v2 == '+':
                    resultado.empilhar(v3+v1)
                elif v2 == '-':
                    resultado.empilhar(v3-v1)
                elif v2 == '/':
                    resultado.empilhar(v3/v1)
                elif v2 == '*':
                    resultado.empilhar(v3*v1)
            elif str(v3) in '({[' and num(v2) and str(v1) in ')}]':
                resultado.empilhar(v2)
            elif str(v1) in '}])':
                verificar = resultado.desempilhar()
                if num(verificar) and num(v2):
                    resultado.desempilhar()
                    if str(v3) == '+':
                        resultado.empilhar(verificar+v2)
                    elif str(v3) == '-':
                        resultado.empilhar(verificar-v2)
                    elif str(v3) == '/':
                        resultado.empilhar(verificar/v2)
                    elif str(v3) == '*':
                        resultado.empilhar(verificar*v2)
            elif str(v1) in '/*-+' and num(v2) and str(v3) in ']})':
                verificar = fila.desenfileirar()
                if num(verificar):
                    if v1 == '+':
                        resultado.empilhar(v2+verificar)
                    elif v1 == '-':
                        resultado.empilhar(v2-verificar)
                    elif v1 == '/':
                        resultado.empilhar(v2/verificar)
                    elif v1 == '*':
                        resultado.empilhar(v2*verificar)
                else:
                    resultado.empilhar(verificar)
                    resultado.empilhar(v3)
                    resultado.empilhar(v2)
                    resultado.empilhar(v1)
            elif str(v2) in '/*-+':
                resultado.empilhar(v3)
                resultado.empilhar(v2)
                resultado.empilhar(v1)
            else:
                resultado.empilhar(v3)
                resultado.empilhar(v2)
                resultado.empilhar(v1)
    if resultado.__len__()==3:
        v1 = resultado.desempilhar()
        v2 = resultado.desempilhar()
        v3 = resultado.desempilhar()
        if v2 == '+':
                resultado.empilhar(v3+v1)
        elif v2 == '-':
                resultado.empilhar(v3-v1)
        elif v2 == '/':
                resultado.empilhar(v3/v1)
        elif v2 == '*':
                resultado.empilhar(v3*v1)

    return resultado.desempilhar()

import unittest


class AnaliseLexicaTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        fila = analise_lexica('')
        self.assertTrue(fila.vazia())

    def test_caracter_estranho(self):
        self.assertRaises(ErroLexico, analise_lexica, 'a')
        self.assertRaises(ErroLexico, analise_lexica, 'ab')

    def test_inteiro_com_um_algarismo(self):
        fila = analise_lexica('1')
        self.assertEqual('1', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_inteiro_com_varios_algarismos(self):
        fila = analise_lexica('1234567890')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_float(self):
        fila = analise_lexica('1234567890.34')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('34', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_parenteses(self):
        fila = analise_lexica('(1)')
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_chaves(self):
        fila = analise_lexica('{(1)}')
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_colchetes(self):
        fila = analise_lexica('[{(1.0)}]')
        self.assertEqual('[', fila.desenfileirar())
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertEqual(']', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_adicao(self):
        fila = analise_lexica('1+2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('+', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_subtracao(self):
        fila = analise_lexica('1-2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('-', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_multiplicacao(self):
        fila = analise_lexica('1*2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('*', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_divisao(self):
        fila = analise_lexica('1/2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('/', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_expresao_com_todos_simbolos(self):
        expressao = '1/{2.0+3*[7-(5-3)]}'
        fila = analise_lexica(expressao)
        self.assertListEqual(list(expressao), [e for e in fila])
        self.assertTrue(fila.vazia())

class AnaliseSintaticaTestes(unittest.TestCase):
    def test_fila_vazia(self):
        fila = Fila()
        self.assertRaises(ErroSintatico, analise_sintatica, fila)

    def test_int(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_float(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila.enfileirar('.')
        fila.enfileirar('4')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890.4, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_expressao_com_todos_elementos(self):
        fila = analise_lexica('1000/{222.125+3*[7-(5-3)]}')
        fila_sintatica = analise_sintatica(fila)
        self.assertListEqual([1000, '/', '{', 222.125, '+', 3, '*', '[', 7, '-', '(', 5, '-', 3, ')', ']', '}'],
                             [e for e in fila_sintatica])

class AvaliacaoTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertRaises(ErroSintatico, avaliar,(''))

    def test_inteiro(self):
        self.assert_avaliacao('1')

    def test_float(self):
        self.assert_avaliacao('2.1')

    def test_soma(self):
        self.assert_avaliacao('2+1')

    def test_subtracao_e_parenteses(self):
        self.assert_avaliacao('(2-1)')

    def test_expressao_com_todos_elementos(self):
        self.assertEqual(1.0, avaliar('2.0/[4*3+1-{15-(1+3)}]'))

    def assert_avaliacao(self, expressao):
        self.assertEqual(eval(expressao), avaliar(expressao))


if __name__ == '__main__':
    unittest.main()
