import copy

# Para um grafo ter um Caminho Euleriano, é suficiente e necessário satisfazer uma de duas condições:
#  - Todos os vértices do grafo tem que ter grau par.
#  - Todos os vértices (ignorando-se os de grau zero) tem grau par, exceto dois vértices que possuem grau ímpar.
# https://repl.it/repls/AnxiousDarkmagentaComputergraphics

if __name__=='__main__':
    
    # Euleriano
    grafoA = {
        0 : [1,3],
        1 : [2,0],
        2 : [3,1],
        3 : [2,0]
    }

    # Não é euleriano
    grafoB = {
        0 : [],
        1 : [],
        2 : [],
        3 : []
    }

    # Não é euleriano
    grafoC = {
        0 : [1,2,3],
        1 : [2,3,0],
        2 : [3,0,1],
        3 : [2,3,0]
    }

    # Euleriano
    grafoD = {
        0 : [1,2,3],
        1 : [2,3],
        2 : [3,0],
        3 : [2,3]
    }

    # Euleriano
    grafo = {
        0 : [1,4],
        1 : [0,2,3],
        2 : [1,3,5],
        3 : [4,2,1,5],
        4 : [0,3],
        5 : [2,3]
    }

    arestasVisitadas     = []
    caminhoEulerVisitado = []
    
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
  
    def printCaminhoEuleriano(grafo):
        caminhoEulerVisitado = []

        index = 0
        for aresta in grafo:
            grau = grauAresta(grafo, aresta)
            
            if (grau % 2 != 0):
                index = aresta
                break
        printarCaminhoEuleriano(grafo, index)
    

    def printarCaminhoEuleriano(grafo, index):
        cloneGrafo = copy.deepcopy(grafo)
        
        for v in cloneGrafo[index]:
            if validarProximoPasso(grafo, index, v):
                if (index not in caminhoEulerVisitado):
                    print('[>>]', index)
                    caminhoEulerVisitado.append(index)
                    grafo = removerCaminho(grafo, index, v)
                    printarCaminhoEuleriano(grafo, v)


    def removerCaminho(grafo, u, v):
        for index, key in enumerate(grafo[u]):
            if key == v:
                grafo[u].pop(index)
        for index, key in enumerate(grafo[v]):
            if key == u:
                grafo[v].pop(index)
        return grafo

    def validarProximoPasso(grafo, index, v):
        if len(grafo[index]) == 1:
            return True
        else:
            # print('index:', index) 
            countA = algoritmoDFS(grafo, index, [])
            grafo  = removerCaminho(grafo, index, v)
            countB = algoritmoDFS(grafo, v, [])            
            
            if (len(countA) > len(countB)):
                return False
            return True

    grafoConexo = algoritmoDFS(grafo, 0, arestasVisitadas)
    if (grafoConexo):
        grafoPossuiCaminhoEuleriano = euleriano(grafo)

        if (grafoPossuiCaminhoEuleriano):
            print('O grafo gerado possui caminho euleriano.')
            printCaminhoEuleriano(grafo)
        else:
            print('O grafo gerado NÃO possui caminho euleriano.')
    else:
        print('O grafo gerado NÃO possui caminho euleriano.')