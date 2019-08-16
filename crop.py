import shapefile
import numpy as np
import sys
from PIL import Image
from shapely.geometry import Point,Polygon
import os

name = sys.argv[1]
os.chdir(name[:-1])
sf = shapefile.Reader(name+'.shp')
for poly_ in range(len(sf.__geo_interface__)): 
    poly =list(sf.__geo_interface__['features'][poly_]['geometry']['coordinates'][0])
    poly = [(-v,k) for (k,v) in poly]
    im = Image.open(name+'.png').convert("RGBA")
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
    newIm = Image.fromarray(im_copy, "RGBA")
    nm = name+str(poly_)+'_cropped.png'
    newIm.save(nm)
