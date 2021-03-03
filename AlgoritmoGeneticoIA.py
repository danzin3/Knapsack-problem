
import populacao
import time
from random import randint
if __name__ == '__main__':
    objPop = populacao.Populacao(10,5,0,1000)
    print("Digite a quantidade de gerações:")
    quant = input()
    inicio = time.time()
    for i in range(int(quant)):
        print(i+1," Geração")
        objPop.imprimirPopulacao()
        objPop.buscarValidos()
        objPop.crossOverIndividuos()
        objPop.mutacaoIndividuos()

    print("*************************************************************")
    print("Indivíduos que não passou do limite de gasto (válidos):")
    objPop.imprimirValidos()
    print("*************************************************************")
    objPop.pegarMaiorBeneficio()
    fim = time.time()
    print("Tempo de execução: ",(fim-inicio))