
# Para um grafo ter um Caminho Euleriano, é suficiente e necessário satisfazer uma de duas condições:
#  - Todos os vértices do grafo tem que ter grau par.
#  - Todos os vértices (ignorando-se os de grau zero) tem grau par, exceto dois vértices que possuem grau ímpar.

if __name__=='__main__':
    
    grafo = {
        '1' : ['1','3','5'],
        '2' : ['4','5'],
        '3' : ['1','5'],
        '4' : ['5','2'],
        '5' : ['1','2','3']
    }
    arestasVisitadas = []
    print('Grafo gerado: ',grafo)

    def algoritmoDFS(grafo, aresta, arestasVisitadas):
        if (aresta not in arestasVisitadas):
            arestasVisitadas.append(aresta)

            for arestaVizinha in grafo[aresta]:
                algoritmoDFS(grafo, arestaVizinha, arestasVisitadas)

        return arestasVisitadas

    def grauAresta(grafo, aresta):
        grau = 0

        for n in grafo[aresta]:
            grau = (grau + 1)

        return grau

    def euleriano(grafo):
        verticesComGrauImpar = 0
        
        for aresta in grafo:
            grau = grauAresta(grafo, aresta)

            if (grau == 1):
                return False
                
            if (grau % 2 != 0):
                verticesComGrauImpar = (verticesComGrauImpar + 1)
        
                if (verticesComGrauImpar > 2):
                    return False
        return True

    grafoPossuiCaminhoEuleriano = euleriano(grafo)

    if (grafoPossuiCaminhoEuleriano):
        camihoEuleriano = algoritmoDFS(grafo, '2', arestasVisitadas)
        print('O grafo gerado possui caminho euleriano: ')
        print(camihoEuleriano)
    else:
        print('O grafo gerado NÃO possui caminho euleriano')