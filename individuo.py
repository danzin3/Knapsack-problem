
from random import randint
class Individuo:
    """Classe que representa um indivíduo"""
    # n              --> Tamanho máximo do cromossomo
    # cromossomo     --> Vetor de bits para representar o cromossomo
    # numAleatorio   --> Objeto para geração de número aleatórios
    # intervalMin    --> Menor valor de x (raiz) na função fitness
    # intervalMax    --> Maior valor de x (raiz) da função fitness
    # nomeProd       --> Lista com o nome dos produtos
    # custo          --> Lista de custos dos produtos
    # importancia    --> Lista de benefícios dos produtos
    # somaCusto      --> Soma dos custos dos itens que estão dentro da mochila
    # somaImportancia--> Soma do benefícios dos itens da mochila

    numAleatorio = {}

    def __init__(self,tam,minVal,maxVal):
        # Atributos internos do Indivíduo:
        self.cromossomo = []
        self.numAleatorio = randint

        self.nomeProd = []
        self.custo = []
        self.importancia = []
        self.somaCusto = 0
        self.somaImportancia = 0

        # Criar um indivíduo com valores dos cromossomos aleatórios
        for i in range(tam):
            self.cromossomo.append(self.numAleatorio(0,1))
            
        self.n = tam
        self.intervalMin = minVal
        self.intervalMax = maxVal
        # Instância 1 (Instância para 5 objetos)
        self.nomeProd.append("Tijolo")
        self.custo.append(250)
        self.importancia.append(8)
        
        self.nomeProd.append("Telha")
        self.custo.append(300)
        self.importancia.append(6)
        
        self.nomeProd.append("Cimento")
        self.custo.append(180)
        self.importancia.append(9)
        
        self.nomeProd.append("Janela")
        self.custo.append(220)
        self.importancia.append(5)
        
        self.nomeProd.append("Ferragem")
        self.custo.append(320)
        self.importancia.append(9)
        
        # Instância 2
        #self.nomeProd.append("Sofá")
        #self.custo.append(500)
        #self.importancia.append(3)

        #self.nomeProd.append("Cerâmica")
        #self.custo.append(280)
        #self.importancia.append(7)

        #self.nomeProd.append("Porta")
        #self.custo.append(180)
        #self.importancia.append(4)

        #self.nomeProd.append("Cama")
        #self.custo.append(220)
        #self.importancia.append(5)

        #self.nomeProd.append("Pia")
        #self.custo.append(200)
        #self.importancia.append(4)



    # Efetua a soma dos custos e benefícios dos itens que estão na mochila
    def gerarAdaptabilidade(self):
        self.somaCusto = 0
        for i in range(self.n):
            if(self.cromossomo[i] == 1):
                self.somaCusto = self.somaCusto + self.custo[i]
                self.somaImportancia = self.somaImportancia + self.importancia[i]
        

    # Método que simula a pressão do Ambiente no Indivíduo
    def pressaoAmbiente(self):
        self.gerarAdaptabilidade();

    # Método que recebe um indivíduo como parâmetro e obtem os dados desse indivíduo
    # Pode-se entender que esse método realiza uma cópia do Indivíduo passado como parametro
    def recebeDados(self,IndParam):
        # A cópia só poderá ser feita se o tamano do cromossomo dos Indivíduos forem Iguais
        if(self.n == IndParam.n):
            self.cromossomo = IndParam.cromossomo.copy()
            self.n = IndParam.n
            self.numAleatorio = IndParam.numAleatorio
            self.intervalMin = IndParam.intervalMin
            self.intervalMax = IndParam.intervalMax
            
            self.custo = IndParam.custo
            self.importancia = IndParam.importancia
            self.somaCusto = IndParam.somaCusto
            self.somaImportancia = IndParam.somaImportancia 
            
        else:
            print("Não é possível clonar Individuos com o tamanho do cromossomo difentes")


    # Função para mostrar os atributos de um indivíduo
    def showIndividuo(self):
        print("Tamanho do Cromossomo: ",self.n)
        print("Cromossomo: ",self.cromossomo)
        print("xMin: ",self.intervalMin)
        print("xMax: ",self.intervalMax)
        print("Custos: ",self.custo)
        print("Importancia: ",self.importancia)
        print("Soma dos Custos válidos: ",self.somaCusto)
        print("Soma da importancia válida:",self.somaImportancia)
        print("--------------------------------------------------------------")

    # Função que realiza a mutação de um indivíduo
    def mutacao(self):
        aux = self.numAleatorio(0,(self.n -1))
        if(self.cromossomo[aux] == 1):
            self.cromossomo[aux] = 0
        else:
            self.cromossomo[aux] = 1
        self.pressaoAmbiente()
        