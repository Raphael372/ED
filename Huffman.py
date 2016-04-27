def calcular_frequencias(s):
    n= len(s)
    dicionario={}
    if n <1:
        return {}
    else:
        for i in s:
            if i not in dicionario.keys():
                dicionario[i]=1
            else:
                dicionario[i]+=1
        return dicionario

def gerar_arvore_de_huffman(s):
    dicionario_folhas = calcular_frequencias(s)
    folhas = []

    for folha in dicionario_folhas:
        folhas.append(Folha(folha,dicionario_folhas[folha]))

    folhas.sort(key=lambda f: f.peso)
    folha = folhas.pop(0)
    arvore = Arvore(folha.char, folha.peso)

    while folhas:
        folha = folhas.pop(0)
        arvore2 = Arvore(folha.char, folha.peso)
        arvore = arvore2.fundir(arvore)

    return arvore


def codificar(cod_dict, s):
    codigo = ""
    for letra in s:
        codigo+=cod_dict[letra]
    return codigo


class Noh:
    def __init__(self, peso, esquerdo = None, direito = None):
        self.peso = peso
        self.esquerdo = esquerdo
        self.direito = direito

    def __hash__(self):
        return hash(self.peso)

    def __eq__(self, other):
        if other is None or not isinstance(other, Noh):
            return False
        return self.peso == other.peso and self.esquerdo == other.esquerdo and self.direito == other.direito


class Folha():
    def __init__(self, char = None, peso = None):
        self.char = char
        self.peso = peso

    def __hash__(self):
        return hash(self.__dict__)

    def __eq__(self, other):
        if other is None or not isinstance(other, Folha):
            return False
        return self.__dict__ == other.__dict__


class Arvore(object):
    def __init__(self, char = None, num = None):
        if char == None and num == None:
            self.raiz = None
        else:
            self.raiz = Folha(char, num)

    def __hash__(self):
        return hash(self.raiz)

    def __eq__(self, other):
        if other is None:
            return False
        return self.raiz == other.raiz

    def fundir (self, arvore2):
        raiz = Noh(self.raiz.peso + arvore2.raiz.peso)
        raiz.esquerdo = self.raiz
        raiz.direito = arvore2.raiz

        Novarvore = Arvore()
        Novarvore.raiz = raiz

        return Novarvore

    def cod_dict(self):
        dicionario = {}
        codigo = []
        noh_e_folhas = []
        noh_e_folhas.append(self.raiz)

        while noh_e_folhas:
            noh_folha_atual = noh_e_folhas.pop()
            if isinstance(noh_folha_atual, Noh):
                noh_e_folhas.append(noh_folha_atual.direito)
                noh_e_folhas.append(noh_folha_atual.esquerdo)
                codigo.append('0')
            elif isinstance(noh_folha_atual, Folha):
                letra = noh_folha_atual.char
                dicionario[letra] = ''.join(codigo)
                codigo.pop()
                codigo.append('1')

        return dicionario

    def decodificar(self, codigo):
        Dicionarionovo = {}
        palavra = ""
        a = ""

        for valor in self.cod_dict():
            Dicionarionovo[self.cod_dict()[valor]] = valor


        for i in codigo:
            a+=i
            if a in Dicionarionovo:
                palavra+=Dicionarionovo[a]
                a = ""

        return palavra



from unittest import TestCase


class CalcularFrequenciaCarecteresTestes(TestCase):
    def teste_string_vazia(self):
        self.assertDictEqual({}, calcular_frequencias(''))

    def teste_string_nao_vazia(self):
        self.assertDictEqual({'a': 3, 'b': 2, 'c': 1}, calcular_frequencias('aaabbc'))


class NohTestes(TestCase):
    def teste_folha_init(self):
        folha = Folha('a', 3)
        self.assertEqual('a', folha.char)
        self.assertEqual(3, folha.peso)

    def teste_folha_eq(self):
        self.assertEqual(Folha('a', 3), Folha('a', 3))
        self.assertNotEqual(Folha('a', 3), Folha('b', 3))
        self.assertNotEqual(Folha('a', 3), Folha('a', 2))
        self.assertNotEqual(Folha('a', 3), Folha('b', 2))

    def testes_eq_sem_filhos(self):
        self.assertEqual(Noh(2), Noh(2))
        self.assertNotEqual(Noh(2), Noh(3))

    def testes_eq_com_filhos(self):
        noh_com_filho = Noh(2)
        noh_com_filho.esquerdo = Noh(3)
        self.assertNotEqual(Noh(2), noh_com_filho)

    def teste_noh_init(self):
        noh = Noh(3)
        self.assertEqual(3, noh.peso)
        self.assertIsNone(noh.esquerdo)
        self.assertIsNone(noh.direito)


def _gerar_arvore_aaaa_bb_c():
    raiz = Noh(7)
    raiz.esquerdo = Folha('a', 4)
    noh = Noh(3)
    raiz.direito = noh
    noh.esquerdo = Folha('b', 2)
    noh.direito = Folha('c', 1)
    arvore_esperada = Arvore()
    arvore_esperada.raiz = raiz
    return arvore_esperada


class ArvoreTestes(TestCase):
    def teste_init_com_defaults(self):
        arvore = Arvore()
        self.assertIsNone(arvore.raiz)

    def teste_init_sem_defaults(self):
        arvore = Arvore('a', 3)
        self.assertEqual(Folha('a', 3), arvore.raiz)

    def teste_fundir_arvores_iniciais(self):
        raiz = Noh(3)
        raiz.esquerdo = Folha('b', 2)
        raiz.direito = Folha('c', 1)
        arvore_esperada = Arvore()
        arvore_esperada.raiz = raiz

        arvore = Arvore('b', 2)
        arvore2 = Arvore('c', 1)
        arvore_fundida = arvore.fundir(arvore2)
        self.assertEqual(arvore_esperada, arvore_fundida)

    def teste_fundir_arvores_nao_iniciais(self):
        arvore_esperada = _gerar_arvore_aaaa_bb_c()

        arvore = Arvore('b', 2)
        arvore2 = Arvore('c', 1)
        arvore3 = Arvore('a', 4)
        arvore_fundida = arvore.fundir(arvore2)
        arvore_fundida = arvore3.fundir(arvore_fundida)

        self.assertEqual(arvore_esperada, arvore_fundida)

    def teste_gerar_dicionario_de_codificacao(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertDictEqual({'a': '0', 'b': '10', 'c': '11'}, arvore.cod_dict())

    def teste_decodificar(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertEqual('aaaabbc', arvore.decodificar('0000101011'))


class TestesDeIntegracao(TestCase):
    def teste_gerar_arvore_de_huffman(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertEqual(arvore, gerar_arvore_de_huffman('aaaabbc'))

    def teste_codificar(self):
        arvore = gerar_arvore_de_huffman('aaaabbc')
        self.assertEqual('0000101011', codificar(arvore.cod_dict(), 'aaaabbc'))
        self.assertEqual('aaaabbc', arvore.decodificar('0000101011'))
