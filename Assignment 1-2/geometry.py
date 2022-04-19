from turtle import pos
from typing import Generator
import rhino3dm as rg
import networkx as nx


def createHouseGraph():

    House = nx.house_graph()
    # explicitly set positions
    pos = {0: (0, 0), 1: (1, 0), 2: (0, 1), 3: (1, 1), 4: (0.5, 2.0)}

    return House

def getNodes(House):

    lay =  nx.kamada_kawai_layout(House)
    
    nodes = []
    for d in lay.values():
        pt = rg.Point3d( d[0], d[1] , 0)
        nodes.append(pt)

    return nodes

def getEdges(G):

    lay =  nx.kamada_kawai_layout(G)

    edges = []
    for e in G.edges:
        p1 = rg.Point3d( lay[e[0]][0], lay[e[0]][1], 0 )
        p2 = rg.Point3d( lay[e[1]][0], lay[e[1]][1], 0 )
        line = rg.LineCurve(p1, p2)
        edges.append(line)

    return edges
