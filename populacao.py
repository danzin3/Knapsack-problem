
import individuo
from random import randint

class Populacao(object):
    """Armazena e realiza operações com indivíduos"""

    # individuos   --> Lista de Indivíduos
    # nPop         --> tamanho da população (quantidade máxima de indivíduos)
    # nInd         --> tamanho do cromossomo de cada Indivíduo
    # min          --> Intervalo Mínimo real da fitness
    # max          --> Intervalo Máximo real da fitness
    # indValidos  --> Lista de indivíduos que não ultrapassam o limite da mochila
    
    
    def __init__(self, tamPop, tamInd, minParam, maxParam):
        self.individuos = []        
        self.nPop = tamPop
        self.nInd = tamInd      
        self.min = minParam
        self.max = maxParam
        self.indValidos = []

        # criando uma  população de indivíduos de tamanho nPop
        for i in range(self.nPop):
            self.individuos.append(individuo.Individuo(self.nInd,self.min,self.max))
            self.individuos[i].pressaoAmbiente()

    # Função que realiza a mutação em todos os indivíduos da população
    def mutacaoIndividuos(self):
        for ind in self.individuos:
            ind.mutacao()


    # Função que realiza o cruzamento dos indivíduos da população
    def crossOverIndividuos(self):
        i=0
        j=0
        max=0
        geneMae = 0
        pontoCorte = randint(1,(self.nInd-1))

        # Se o número de indivíduos da população for par, o cruzamento ocorre
        # normalmente. Se o número for ímpar, o ultimo indivíduo não terá
        # outro um par para a reprodução, logo o último indivíduo de uma população
        # de número impar não terá filhos... coitado :(

        if((self.nInd%2) == 0):
            max = self.nInd
        else:
            max = (self.nInd - 1)


        # percorrer a população para realizar o cruzamento
        while(i < max):
            # Percorrer o cromossomo dos indivíduos
            while(j < pontoCorte):
                # guardar o gene da mãe (i+1)
                geneMae = self.individuos[i+1].cromossomo[j]
                # colocar o gene do pai (i) no cromossomo da mãe (i+1)
                self.individuos[i+1].cromossomo[j] = self.individuos[i].cromossomo[j]
                # colocar o gene da mãe (i+1) no gene do pai (i)
                self.individuos[i].cromossomo[j] = geneMae
                j = j + 1
            j = 0
            i = i + 1



    # Função que separa as soluções (indivíduos) viáveis para o problema
    def buscarValidos(self):
        for ind in self.individuos:
            if(ind.somaCusto < self.max):
                self.indValidos.append(individuo.Individuo(self.nInd,self.min,self.max))
                self.indValidos[-1].recebeDados(ind)


    # Função que imprime os indivíduos adaptaveis (soluções viáveis)
    def imprimirValidos(self):
        for ind in self.indValidos:
            ind.showIndividuo()


    # Função que realiza uma busca sequencial para identificar o indivíduo 
    # adaptável de maior benefício
    def pegarMaiorBeneficio(self):
        if(len(self.indValidos) > 0):
            aux = self.indValidos[0]
            for ind in self.indValidos:
                if(aux.somaImportancia < ind.somaImportancia):
                    aux = ind
            print("Melhor de Todos os Válidos: ")
            aux.showIndividuo()
        else:
            print("Nenhuma solução viável encontrada")

    # Função que imprime todos os indivíduos de uma população
    def imprimirPopulacao(self):
        for ind in self.individuos:
            ind.showIndividuo()
