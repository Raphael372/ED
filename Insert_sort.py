import unittest


def insert_sort(seq):
    ''' sorteia a sequencia usando o insertion sort ,
     complexidade O(n)²   '''
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insert_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insert_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insert_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insert_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
