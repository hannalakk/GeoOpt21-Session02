#Geo-opt Session02 Assignment 1-2
#Hanna Läkk

from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo
import networkx as nx

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/housegraph",
    name = "Create House Graph",
    inputs=[
    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)
    ]
)


def createGraph():

    G = geo.createHouseGraph()

    nodes = geo.getNodes(G)
    edges = geo.getEdges(G) 

    return nodes, edges


if __name__== "__main__":
    app.run(debug=True)