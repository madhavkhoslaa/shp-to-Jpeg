import shapefile
import numpy as np
from PIL import Image
from shapely.geometry import Polygon
import os
import cv2


os.chdir("/Users/madhav/Desktop/Images/OUTPUT/Output/Defence Colony/01")
img = Image.fromarray(np.zeros((640, 640, 3), dtype=np.uint8))
name = '1'
shape = []
shape_polygon= []
sf = shapefile.Reader(name+ ".shp")

for polygon_ in range(len(sf.__geo_interface__)):
    feature = sf.shapeRecords()[polygon_]
    poly_= feature.shape.__geo_interface__["coordinates"][0]
    shape.append(poly_)
    shape_polygon.append(Polygon(poly_))
    xy= lambda x: [elemen for elemen in poly_]
    abbs= lambda x: list(map(abs, x))
    ll= list(map(abbs, list(map(list,xy(poly_)))))
    img= cv2.fillPoly(np.array(img),pts=np.int32([ll]), color= (255,255,255))

