import unittest

def min_max (seq):
    '''Atendendo aos casos especiais onde a lista tem 2 elementos ou menos'''
    if (len(seq) == 2):
        if (seq[0] > seq[1]):
            return seq[0], seq[1]
        else:
            return seq[1], seq[0]
    elif (len(seq) == 1):
        return seq[0], seq[0]
    elif (len(seq) == 0):
        return None, None
    '''Retornando os valores minimo e maximo respectivamente.
    se o tamanho da sequencia for igual a 0 retorna nulo '''
    return pegaMin(seq), pegaMax(seq)

def pegaMin(seq):
    if len(seq) == 1:
        return seq[0]
    else:
        m = pegaMax(seq[1:])
        return m if m < seq[0] else seq[0] 

def pegaMax(seq):
    if len(seq) == 1:
        return seq[0]
    else:
        m = pegaMax(seq[1:])
        return m if m > seq[0] else seq[0]

class MinMaxTestes(unittest.TestCase):
    def test_lista_vazia(self):
        self.assertTupleEqual((None, None), min_max([]))

    def test_lista_len_1(self):
        self.assertTupleEqual((1, 1), min_max([1]))

    def test_lista_consecutivos(self):
        self.assertTupleEqual((0, 500), min_max(list(range(501))))


if __name__ == '__main__':
    unittest.main()

