
# Para um grafo ter um Caminho Euleriano, é suficiente e necessário satisfazer uma de duas condições:
#  - Todos os vértices do grafo tem que ter grau par.
#  - Todos os vértices (ignorando-se os de grau zero) tem grau par, exceto dois vértices que possuem grau ímpar.
#    Nesse caso, os dois vértices de grau ímpar são o início e o fim do Caminho.

def euleriano(listaVertices, listaArestas):
    numeroVerticesComGrauImpar = 0
    
    for vertice in listaVertices:
        grau = grauVertice(vertice, listaArestas)
        
        if (grau % 2 != 0):
            numeroVerticesComGrauImpar = (numeroVerticesComGrauImpar + 1)

            if (countGrauImpar > 2):
                return False
    return True

def grauVertice(vertice, listaArestasVertice):
    grau = 0
        
    for arestaVertice in listaArestasVertice:
        verticeA, verticeB = arestaVertice

        if (vertice == verticeA or vertice ==  verticeB):
            grau += 1

    return grau

def criarListVertices():
    listaVertices = []

    listaVertices.append(1)
    listaVertices.append(2)
    listaVertices.append(3)
    listaVertices.append(4)
    listaVertices.append(5)

    return listaVertices

def criarListVertices():
    listaArestas = []

    listaArestas.append((1, 2))
    listaArestas.append((1, 3))
    listaArestas.append((1, 5))
    listaArestas.append((2, 4))
    listaArestas.append((4, 5))
    listaArestas.append((5, 3))

    return listaArestas

if __name__=='__main__':
    print('Criando um grafo conexo...')
    print('...')
    print('...')
    print('...')
    listaVertices = criarListVertices()
    listaArestas  = criarListVertices()
    print('Grafo criado.')

    print('...')
    print('...')
    print('...')
    
    print('Verificando se o grafo possui Caminho Euleriano...')
    euler = euleriano(listaVertices, listaArestas)

    print('...')
    print('...')
    print('...')
    
    if(euler):
        print('O grafico apresentado possui um Caminho Euleriano!')
    else:
        print('O grafico apresentado NÃO possui um Caminho Euleriano!')











