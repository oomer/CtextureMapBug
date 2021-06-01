  
from pymaxwell5 import *
import platform

if platform.system() == 'Linux':
    texturePath ='/mnt/job/Maxwell/python/checker.png'
    OUTPUTDEFAULT='/mnt/job/Maxwell/python/LinuxMaterialDefault.mxs'
    OUTPUTMODIFIED='/mnt/job/Maxwell/python/LinuxMaterialModified.mxs'
elif platform.system() == 'Darwin':
    texturePath ='/Volumes/pokadot/job/Maxwell/python/checker.png'
    OUTPUTDEFAULT='/Volumes/pokadot/job/Maxwell/python/OsxMaterialDefault.mxs'
    OUTPUTMODIFIED='/Volumes/pokadot/job/Maxwell/python/OsxMaterialModified.mxs'
elif platform.system() == 'Windows':
    texturePath ='J:/job/Maxwell/python/checker.png'
    OUTPUTDEFAULT='J:/job/Maxwell/python/WindowsMaterialDefault.mxs'
    OUTPUTMODIFIED='J:/job/Maxwell/python/WindowsMaterialModified.mxs'

scene = Cmaxwell(mwcallback_cb) 

#Create material layer
myMaterial = scene.createMaterial('myMaterial') 
layer = myMaterial.addLayer() 
layer.setName( 'myLayer' )

#Add BSDF
bsdf = layer.addBSDF()
reflectance = bsdf.getReflectance()

#Insert texturemap 
attr= Cattribute()
attr.activeType = MAP_TYPE_BITMAP
attr.textureMap.setPath(texturePath)
reflectance.setAttribute('color',attr) #aka reflectance0 in Studio
reflectance.setAttribute('color.tangential',attr) #aka reflectance90 in Studio
reflectance.setAttribute('transmittance.color',attr) #aka transmittance in Studio

transmittance,ok=reflectance.getAttribute('transmittance.color')
if ok:
    print("DEFAULT nothing done to scale or rotation")
    print("scale:",str(transmittance.textureMap.scale))
    print("rotation:",transmittance.textureMap.rotation)

#Write out mxs with texturemaps and no changes to scale and rotation
scene.writeMXS(OUTPUTDEFAULT)

#Modify scale and rotation
attr.textureMap.scale.add(5) #Cvector2D
attr.textureMap.rotation=1.5 #float
reflectance.setAttribute('transmittance.color',attr) #aka transmittance in Studio
reflectance.setAttribute('color',attr) #aka reflectance0 in Studio
reflectance.setAttribute('color.tangential',attr) #aka reflectance90 in Studio

transmittance,ok=reflectance.getAttribute('transmittance.color')
if ok:
    print("MODIFIED scale and rotation")
    print("scale:",str(transmittance.textureMap.scale))
    print("rotation:",transmittance.textureMap.rotation)

scene.writeMXS(OUTPUTMODIFIED)