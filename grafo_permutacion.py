# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:04:56 2016
@author: guttag
"""


class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class Digraph(object):
    """edges is a dict mapping each node to a list of
    its children"""

    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '--->' \
                         + dest.getName() + '\n'
        return result[:-1]  # omit final newline


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


alumnos = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
nodes = []
print("---CREACION DE LOS NODOS---")
for orden in alumnos:
    nodes.append(Node(orden)) # nodes[0]
    print("Creando el Nodo-------->", Node(orden))

g = Graph() # Creo un grafo dirigido g
print()
print("---AGREGANDO LOS NODOS---")
for n in nodes:
    print("Agregando Nodo---------> ", n)
    g.addNode(n)
print()
nodos = []
for i in nodes:
    nodos.append(i.getName())
print("Lista de Nodos agregados:", nodos)
print()
# 1RA FORMA
temp = nodes[:]
while temp:
    current = temp.pop()
    print("-----ITERACIÓN-------->", current)
    print("Sacamos ultimo Nodo agregado POP:", current)
    print("1er Alumno del nodo extraido:", current.getName()[0])
    print("Lista de Nodos Actualizada:", [node.getName() for node in temp])
    for node in temp:
        if current.getName()[0] == node.getName()[0] or current.getName()[2] == node.getName()[2]:
            print("Analisis de los Nodos:", current, "vs", node)
            print("Como", current.getName()[0], "=", node.getName()[0])
            print("\tó")
            print("Como", current.getName()[2], "=", node.getName()[2])
            g.addEdge(Edge(current, node))
            print("Agregamos la Arista (EGDE):", Edge(current, node))
            print()

"""#2DA FORMA
for i, n0 in enumerate(nodes):
    for n1 in nodes[i+1:]:
        if n0.name[0] == n1.name[0] or n0.name[2] == n1.name[2]:
            g.addEdge(Edge(n0, n1))"""
print()
print("Lista de Permutaciones VALIDAS para el Nodo", nodos, ":")
print(g)

