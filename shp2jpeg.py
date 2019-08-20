import shapefile
import numpy as np
from PIL import Image
from shapely.geometry import Polygon
import os
import cv2
import imageio
import glob
import shutil

for i in range(0, 500):
    root_dir= "/{}".format(i)
   
    try:
        os.chdir(root_dir)
        img = Image.fromarray(np.zeros((640, 640, 3), dtype=np.uint8))
        name = root_dir.split("/")[-1]
        shape = []
        shape_polygon= []
        shape_file= glob.glob("*.shp")[0]
        sf = shapefile.Reader(shape_file)
        for polygon_ in range(len(sf.__geo_interface__)-1):
            feature = sf.shapeRecords()[polygon_]
            poly_= feature.shape.__geo_interface__["coordinates"][0]
            shape.append(poly_)
            shape_polygon.append(Polygon(poly_))
            xy= lambda x: [elemen for elemen in poly_]
            abbs= lambda x: list(map(abs, x))
            ll= list(map(abbs, list(map(list,xy(poly_)))))
            img= cv2.fillPoly(np.array(img),pts=np.int32([ll]), color= (255,255,255))
        
        imageio.imsave("{}_annotated.tif".format(name), img)
    except:
         imageio.imsave("{}_annotated.tif".format(name), img)
                    
