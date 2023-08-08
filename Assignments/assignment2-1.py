#PART 1
## Import VTK
from vtk import *
import sys

reader = vtkXMLImageDataReader()
reader.SetFileName('Data\Isabel_2D.vti') # Load data
reader.Update()
data = reader.GetOutput()
isovalue=float(sys.argv[1]) #Take float value for isocontour value

points = vtkPoints() 
cells = vtkCellArray()
numCells = data.GetNumberOfCells()

for i in range(numCells): #For every cell
    Flag=0
    cell = data.GetCell(i) # Get vertex id
    pid1 = cell.GetPointId(0)
    pid2 = cell.GetPointId(1)
    pid3 = cell.GetPointId(3)
    pid4 = cell.GetPointId(2)
    dataArr = data.GetPointData().GetArray('Pressure') #Get pressure array
    val1 = dataArr.GetTuple1(pid1) #Get vertex scalar value
    val2 = dataArr.GetTuple1(pid2)
    val3 = dataArr.GetTuple1(pid3)
    val4 = dataArr.GetTuple1(pid4)
    if ((val1>isovalue and val2>isovalue and val3>isovalue and val4>isovalue) or (val1<isovalue and val2<isovalue and val3<isovalue and val4<isovalue)): #This means that the cell does not contain the isocontour
        continue
    else:
        if((val1-isovalue)*(val2-isovalue)<0): #There exists an isocontour through this edge
            Flag+=1 #To track the number of isocontour edges
            ratio1=abs(val1-isovalue)/abs(val1-val2)
            ratio2=(1-ratio1)
            points.InsertNextPoint((ratio1*data.GetPoint(pid1)[0]+ratio2*data.GetPoint(pid2)[0],ratio1*data.GetPoint(pid1)[1]+ratio2*data.GetPoint(pid2)[1],ratio1*data.GetPoint(pid1)[2]+ratio2*data.GetPoint(pid2)[2]))
        
        if((val2-isovalue)*(val3-isovalue)<0):
            Flag+=1
            ratio1=abs(val2-isovalue)/abs(val2-val3)
            ratio2=(1-ratio1)
            points.InsertNextPoint((ratio1*data.GetPoint(pid2)[0]+ratio2*data.GetPoint(pid3)[0],ratio1*data.GetPoint(pid2)[1]+ratio2*data.GetPoint(pid3)[1],ratio1*data.GetPoint(pid2)[2]+ratio2*data.GetPoint(pid3)[2]))
        
        if((val3-isovalue)*(val4-isovalue)<0):
            Flag+=1
            ratio1=abs(val3-isovalue)/abs(val3-val4)
            ratio2=(1-ratio1)
            points.InsertNextPoint((ratio1*data.GetPoint(pid3)[0]+ratio2*data.GetPoint(pid4)[0],ratio1*data.GetPoint(pid3)[1]+ratio2*data.GetPoint(pid4)[1],ratio1*data.GetPoint(pid3)[2]+ratio2*data.GetPoint(pid4)[2]))

        if((val4-isovalue)*(val1-isovalue)<0):
            Flag+=1
            ratio1=abs(val4-isovalue)/abs(val4-val1)
            ratio2=(1-ratio1)
            points.InsertNextPoint((ratio1*data.GetPoint(pid4)[0]+ratio2*data.GetPoint(pid1)[0],ratio1*data.GetPoint(pid4)[1]+ratio2*data.GetPoint(pid1)[1],ratio1*data.GetPoint(pid4)[2]+ratio2*data.GetPoint(pid1)[2]))    
        
    ## Create the cell, which is a polyline
    polyLine = vtkPolyLine()
    if (Flag==2): #2 isocontour edges
        polyLine.GetPointIds().SetNumberOfIds(2)    
        polyLine.GetPointIds().SetId(0, points.GetNumberOfPoints()-2)
        polyLine.GetPointIds().SetId(1, points.GetNumberOfPoints()-1)
        cells.InsertNextCell(polyLine)
    elif (Flag==4): #4 isocontour edges
        polyLine.GetPointIds().SetNumberOfIds(2)    
        polyLine.GetPointIds().SetId(0, points.GetNumberOfPoints()-4)
        polyLine.GetPointIds().SetId(1, points.GetNumberOfPoints()-3)
        cells.InsertNextCell(polyLine)
        polyLine.GetPointIds().SetId(0, points.GetNumberOfPoints()-2)
        polyLine.GetPointIds().SetId(1, points.GetNumberOfPoints()-1)
        cells.InsertNextCell(polyLine)


pdata = vtkPolyData()  #Feed points and cell object to polydata
pdata.SetPoints(points)
pdata.SetLines(cells)

writer = vtkXMLPolyDataWriter() #Writing it on a file
writer.SetInputData(pdata)
writer.SetFileName('contour.vtp')
writer.Write()