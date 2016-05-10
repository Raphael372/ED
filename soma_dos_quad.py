from collections import Counter   
lru={0:[0]}
def soma_quadrados(n):
    max=1
    def soma_quadrados(n):
        if n == 0:
            return [0]
        if n == 1:
            return [1]
    quad=[]
    while(max**2<=n):
        quad.append(max**2)
        max+=1
    while len(quad)>0:
        num=n
        quad1=quad.copy()
        a=quad1.pop()
        resp=[]
        while(num>0):
            if num in lru.keys() and num is not n:
                resp=resp+lru[num]
                num=0
            else:
                if len(quad1)>0:
                    if num-a<0:
                       a=quad1.pop()
                    else:
                        num-=a
                        resp.append(a)
                        if(num<quad1[-1]):
                            a=quad1.pop()
                else:
                    num-=a
                    resp.append(a)
        if n not in lru.keys():
            lru[n]=resp.copy()
        elif len(resp)<len(lru[n]):
            lru[n]=resp.copy()
        quad.pop()
    return lru[n]
import unittest
class SomaQuadradosPerfeitosTestes(unittest.TestCase):
    def teste_0(self):
        self.assert_possui_mesmo_elementos([0], soma_quadrados(0))

    def teste_1(self):
        self.assert_possui_mesmo_elementos([1], soma_quadrados(1))

    def teste_2(self):
        self.assert_possui_mesmo_elementos([1, 1], soma_quadrados(2))

    def teste_3(self):
        self.assert_possui_mesmo_elementos([1, 1, 1], soma_quadrados(3))

    def teste_4(self):
        self.assert_possui_mesmo_elementos([4], soma_quadrados(4))

    def teste_5(self):
        self.assert_possui_mesmo_elementos([4, 1], soma_quadrados(5))

    def teste_11(self):
        self.assert_possui_mesmo_elementos([9, 1, 1], soma_quadrados(11))

    def teste_12(self):
        self.assert_possui_mesmo_elementos([4, 4, 4], soma_quadrados(12))

    def assert_possui_mesmo_elementos(self, esperado, resultado):
        self.assertEqual(Counter(esperado), Counter(resultado))
