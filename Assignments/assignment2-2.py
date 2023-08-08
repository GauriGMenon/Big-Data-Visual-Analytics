from vtk import *
import sys
reader = vtkXMLImageDataReader()
reader.SetFileName('Data\Isabel_3D.vti') #Load the Data
reader.Update()
data = reader.GetOutput()
shading=sys.argv[1] #Takes string value for phong shading, "ON" or "OFF"

ColourFunction= vtkColorTransferFunction() #To map RGB colour
ColourFunction.AddRGBPoint(-4931.54 , 0.0, 1.0, 1.0)
ColourFunction.AddRGBPoint(-2508.95 , 0.0, 0.0, 1.0)
ColourFunction.AddRGBPoint(-1873.9 , 0.0, 0.0, 0.5)
ColourFunction.AddRGBPoint(-1027.16 , 1.0, 0.0, 0.0)
ColourFunction.AddRGBPoint(-298.031 , 1.0, 0.4, 0.0)
ColourFunction.AddRGBPoint(2594.97  , 1.0, 1.0, 0.0)
OpacityFunction= vtkPiecewiseFunction() #To map opacity
OpacityFunction.AddPoint(-4931.54 , 1.0)
OpacityFunction.AddPoint(101.815 , 0.002)
OpacityFunction.AddPoint(2594.97 , 0.0)

volumeMapper=vtkSmartVolumeMapper() #Maps volume based on rendering parameter
volumeMapper.SetInputData(data)

volumeProperty = vtkVolumeProperty() #Properties of Volume rendering
volumeProperty.SetColor(ColourFunction)
volumeProperty.SetScalarOpacity(OpacityFunction)

if(shading== "ON"): #For phong shading "ON"
    volumeProperty.SetShade(1)
    volumeProperty.SetAmbient(0.5)
    volumeProperty.SetDiffuse(0.5)
    volumeProperty.SetSpecular(0.5)

volume = vtkVolume() #To append the mapper and properties
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)

Outline = vtkOutlineFilter() #To set the outline of the data. It needs a separate mapper and actor
Outline.SetInputData(data)
mapper = vtkPolyDataMapper()
mapper.SetInputConnection(Outline.GetOutputPort())
actor = vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetLineWidth(2)
actor.GetProperty().SetColor(0,0,0)

renderer = vtkRenderer() #Rendering the data
renderWindowInteractor = vtkRenderWindowInteractor()
renderWindow = vtkRenderWindow()
renderer.SetBackground(1,1,1)
renderWindow.SetSize(1000,1000)
renderWindow.AddRenderer(renderer)
renderWindowInteractor.SetRenderWindow(renderWindow)
renderer.AddViewProp(volume)
renderer.AddActor(actor)
renderWindow.Render()
renderWindowInteractor.Start()