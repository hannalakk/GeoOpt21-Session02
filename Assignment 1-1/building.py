#we import all the libraries that our functions need here too
import rhino3dm as rg

def createRowBuildings(curve, height, number, distance):
   
    extrusions = []
    
    for item in range(number):

        #extrude the building
        base = rg.Extrusion.Create(curve, height, cap=True)
        
        #dublicate the created buuilding
        baseCopy = base.Duplicate()

        #translate the copies of buildings in x direction
        vectorx =  rg.Vector3d(number*item*distance,0,0)
        baseCopy.Translate(vectorx)

        #add new builsdings to the list
        extrusions.append(baseCopy)

    return extrusions
