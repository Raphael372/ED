class Noh:

    def __init__(self, valor, pai = None, filho_esquerdo = None, irmao_direito = None):
        self.valor = valor
        self.pai = pai
        self.filho_esquerdo = filho_esquerdo
        self.irmao_direito = irmao_direito

        if pai != None:
            pai.filho_esquerdo = self
#nessa classe nao tem o que mudar

    def adicionar(self, filho):


        if self.filho_esquerdo:
            proxFilho = self.filho_esquerdo
            while proxFilho.irmao_direito:
                proxFilho = proxFilho.irmao_direito
            proxFilho.irmao_direito = filho
        else:
            filho.pai = self
            self.filho_esquerdo = filho
            filho.irmao_direito = None

class Arvore:

    def __init__(self, raiz = None):
        self.raiz = raiz

    def altura(self):
        altura_arvore = 0
        while self.raiz != None:
            self.raiz = self.raiz.filho_esquerdo
            altura_arvore+=1
        return altura_arvore


        return 0



from unittest.case import TestCase


class NohTestes(TestCase):
    def teste_init_com_defaults(self):
        noh = Noh(5)
        self.assertEqual(5, noh.valor)
        self.assertIsNone(noh.pai)
        self.assertIsNone(noh.irmao_direito)
        self.assertIsNone(noh.filho_esquerdo)

    def teste_init_com_pai_justaposto(self):
        pai = Noh(5)
        filho = Noh(4, pai)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)

    def teste_init_com_pai_nomeado(self):
        pai = Noh(5)
        filho = Noh(4, pai=pai)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)

    def teste_adicionar_um_filho(self):
        pai = Noh(5)
        filho = Noh(4)
        pai.adicionar(filho)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)
        self.assertIsNone(filho.irmao_direito)

    def teste_adicionar_dois_filhos(self):
        pai = Noh(5)
        filho = Noh(4)
        filho2 = Noh(3)
        pai.adicionar(filho)
        pai.adicionar(filho2)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)
        self.assertIs(filho2, filho.irmao_direito)
        self.assertIsNone(filho2.irmao_direito)

    def teste_adicionar_tres_filhos(self):
        pai = Noh(5)
        filho = Noh(4)
        filho2 = Noh(3)
        filho3 = Noh(2)
        pai.adicionar(filho)
        pai.adicionar(filho2)
        pai.adicionar(filho3)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)
        self.assertIs(filho2, filho.irmao_direito)
        self.assertIs(filho3, filho2.irmao_direito)
        self.assertIsNone(filho3.irmao_direito)
