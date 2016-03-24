import unittest
 '''complexidade de tempo O(n)²  e de espaço O(1) '''

def bubble_sort(seq):

    size = len(seq) -1
    f = False
    for num in range(size, 0, -1):
        for i in range(num):
            if seq[i] > seq[i+1]:
                seq[i],seq[i+1] = seq[i+1],seq[i]
                f = True
            if(f == False):
               break
    return seq


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
