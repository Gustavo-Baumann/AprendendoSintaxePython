from msilib.schema import Class

class pessoa:
    def __init__(self,nome,altura):
        self.nome = nome
        self.altura = altura
    
    def infonome(self):
        print("Olá, Meu Nome é",self.nome)

    def infoaltura(self):
        print("Minha Altura é", self.altura)

eu = pessoa("Gustavo",1.72)
eu.infonome()

class trabalhador(pessoa):
    def __init__(self, nome, altura, profissao):
        super().__init__(nome, altura)
        self.profissao = profissao
    
    def infoprofissao(self):
        print("Minha Profissão é", self.profissao)

meuAmigo = trabalhador("Rodrigo",1.75,"Agricultor")
meuAmigo.infonome()
meuAmigo.infoprofissao()