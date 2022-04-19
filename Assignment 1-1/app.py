#Geo-opt Session02 Assignment 1-1
#Hanna Läkk

#importing flask and hops to create a workflow
from flask import Flask
import ghhops_server as hs
import building as bl

#importing rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)

#creating the hops component
@hops.component(
    "/createRowBuildings",
    name = "Create a Row of Buildings",
    inputs=[
        hs.HopsCurve("Curve", "C", "Closed planar curve to extrude", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Height", "H", "Height of the building", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("Number", "Nr", "Number of buildings in a row", hs.HopsParamAccess.ITEM,),
        hs.HopsNumber("Distance", "D", "Disctance between buildings", hs.HopsParamAccess.ITEM,)
        
    ],
    outputs=[
       hs.HopsBrep("Extrusion","E","Resulting Extrusion", hs.HopsParamAccess.LIST),
    ]
)

def createBuildings(curve, height, number, distance):
   
    buildings = bl.createRowBuildings(curve, height, number, distance)
    return buildings


if __name__== "__main__":
    app.run(debug=True)
