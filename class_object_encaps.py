#----------CLASSE----------------------
class Carro:
    marca = "Toyota"
    modelo = "Corolla"

class Aluno:
    nome = "João"
    idade = 16

#----------OBJETO----------------------

class Carro:
    marca = "Toyota"

carro1 = Carro()

print(carro1.marca)

#--OUTRO
class Aluno:
    nome = "Maria"
    turma = "2° Ano"

aluno1 = Aluno()

print(aluno1.nome)
print(aluno1.turma)

#----------METODO INIT------------------

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

p1 = Pessoa("Carlos")

print(p1.nome)

#--OUTRO
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produto1 = Produto("Mouse", 80)

print(produto1.nome)
print(produto1.preco)

#--------------METODO------------------

class Pessoa:
    def falar(self):
        print("Olá!")


p1 = Pessoa()

p1.falar()

#--OUTRO
class Conta:
    def saldo(self):
        print("Seu saldo é R$500")

conta1 = Conta()

conta1.saldo()

#----------ENCAPSULAMENTO--------------------

class Conta:
    def __init__(self):
        self.__saldo = 1000

conta1 = Conta()

print(conta1.__saldo)

#----------ENCAPSULMENTO COM METODOS-----------------

class Conta:
    def __init__(self):
        self.__saldo = 1000

    def ver_saldo(self):
        print(self.__saldo)

conta1 = Conta()

conta1.ver_saldo()

#----------ALTERANDO ATRIBUTOS PRIVADO------------------

class Conta:
    def __init__(self):
        self.__saldo = 0

    def depositar(self, valor):
        self.__saldo += valor

    def mostrar_saldo(self):
        print(self.__saldo)

conta1 = Conta()

conta1.depositar(200)

conta1.mostrar_saldo()

#-------------EXEMPLO COMPLETO--------------

class Celular:
    def __init__(self, marca):
        self.marca = marca
        self.__bateria = 100

    def mostrar_bateria(self):
        print(self.__bateria)

celular1 = Celular("Samsung")

print(celular1.marca)

celular1.mostrar_bateria()

