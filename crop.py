import shapefile
import numpy as np
from PIL import Image
from shapely.geometry import Point,Polygon
import os, glob
import shutil
from tqdm import tqdm


for i in tqdm(range(0, 500)):
    try:
        name = "/Users/madhav/Desktop/OUTPUT/Output/Defence Colony/{}".format(i)
        shape_file= glob.glob(name+"/*.shp")[0]
        image_name= glob.glob(name+"/*.png")[0]
        sf = shapefile.Reader(shape_file)
        for poly_ in range(len(sf.__geo_interface__)):
            poly =list(sf.__geo_interface__['features'][poly_]['geometry']['coordinates'][0])
            poly = [(-v,k) for (k,v) in poly]
            im = Image.open(image_name).convert("RGBA")
            pixels = np.array(im)
            im_copy = np.array(im)
            region=Polygon(poly)
            for index, pixel in np.ndenumerate(pixels):
            	row,col,channel = index
            	if channel != 0:
            		continue
            	point = Point(row,col)
            	if not region.contains(point):
            		im_copy[(row,col,0)]=255
            		im_copy[(row,col,1)]=255
            		im_copy[(row,col,2)]=255
            		im_copy[(row,col,3)]=0
            # back to Image from numpy
            os.chdir(name)
            newIm = Image.fromarray(im_copy, "RGBA")
            nm = name+"_"+str(poly_)+'_cropped.png'
            newIm.save(nm)
            shutil.move(nm, name)
    except :
        pass
