#!/opt/epd/bin/python
description='Make a finding chart.'
usage= "%prog  image [--z1 zmin --z2 zmax ]\n"

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pyraf import iraf
import os,string,re,sys
import math
import argparse

try:
    import pyfits
except:
    from astropy.io import fits as pyfits
    
import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u
iraf.set(stdimage='imt2048')
#############################
if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=usage, description=description, version="%prog 1.0")
    parser.add_argument('filename', help='file name of a .fits image to use as the finding chart')
    parser.add_argument('-n', '--name', help='name of the supernova (default is the OBJECT keyword in the header)')
    parser.add_argument('--z1', type=float, help='z-scale in main image (default same as ds9 zscale)')
    parser.add_argument('--z2', type=float, help='z-scale in main image (default same as ds9 zscale)')
    parser.add_argument('--z1-inset', type=float, help='z-scale in inset (default same as main image)')
    parser.add_argument('--z2-inset', type=float, help='z-scale in inset (default same as main image)')
    parser.add_argument('--fov', default=5., type=float, help='size of main image in arcmin')
    parser.add_argument('--fov-inset', default=1., type=float, help='size of inset in arcmin')
    args = parser.parse_args()
    img = args.filename
    name = args.name
    _z1 = args.z1
    _z2 = args.z2
    _z1inset = args.z1_inset
    _z2inset = args.z2_inset
    fov = args.fov/60 # convert to degrees
    fovinset = args.fov_inset/60

    X, hdr = pyfits.getdata(img, header=True)
    height, width = X.shape
    if name is None and 'object' in hdr: name = hdr['object']
    crpix1 = hdr['crpix1']
    crval1 = hdr['crval1']
    cd1 = hdr['cd1_1']
    crpix2 = hdr['crpix2']
    crval2 = hdr['crval2']
    cd2 = hdr['cd2_2']
    def col2RA(column):
        return crval1 + (column-crpix1)*cd1
    def row2dec(row):
        return crval2 + (row-crpix2)*cd2
    left = col2RA(0.5)
    right = col2RA(width+0.5)
    bottom = row2dec(0.5)
    top = row2dec(height+0.5)

    # select the object
    if _z1 is None and _z2 is None:
        sss = iraf.display(img, frame=1, fill='yes', zscale='yes', zrange='yes', Stdout=1)[0]
        print sss
        z1str, z2str = sss.split()
        _z1 = float(z1str.split('=')[1])
        _z2 = float(z2str.split('=')[1])
    else: 
        iraf.display(img, frame=1, fill='yes', Stdout=1, zscale='no', zrange='no', z1=_z1, z2=_z2)

    raw_input('stop')
    print '>> Identify target  (mark with "<a> then press <q>")' 
    os.system('rm tmp.coo')
    try:
        iraf.imexamine(img,1,logfile='tmp.coo',keeplog='yes',wcs='world',xformat='%12.3H',yformat='%12.3h')
        iraf.tvmark(1,'tmp.coo',mark="circle",number='yes',label='no',radii=10,nxoffse=5,nyoffse=5,color=214,txsize=4)
        xycoo = iraf.fields('tmp.coo','1,2,3,4,13',Stdout=1)
    except:
        print 'mark with x'
        os.system('rm tmp.coo')
        iraf.imexamine(img,1,logfile='tmp.coo',keeplog='yes',wcs='world',xformat='%12.3H',yformat='%12.3h')
        iraf.tvmark(1,'tmp.coo',mark="circle",number='yes',label='no',radii=10,nxoffse=5,nyoffse=5,color=214,txsize=4)
        xycoo = iraf.fields('tmp.coo','1,2,3,4,13',Stdout=1)
    if len(xycoo)==2:
        x,y,r,d=string.split(xycoo[0])[0:2]+string.split(xycoo[1])[0:2]
        print 'use x'
    else:
        x,y,r,d=string.split(xycoo[0])[0:2]+string.split(xycoo[0])[2:4]
        print 'use a'
    xd = col2RA(float(x))
    yd = row2dec(float(y))

    raw_input('stop')
    plt.ion()
    plt.rcParams['figure.figsize'] =12, 7
    plt.rcParams['figure.facecolor']='white'
    ax = plt.axes([.09,.103,.5,.85])
    ax.imshow(X, cmap='gray_r', aspect='equal', interpolation='nearest', vmin=_z1, vmax=_z2, origin='lower', extent=(left, right, bottom, top))
    plt.xlabel('R.A. (degrees)')
    plt.ylabel('Dec. (degrees)')
    ax.get_xaxis().get_major_formatter().set_useOffset(False)
    ax.get_yaxis().get_major_formatter().set_useOffset(False)

    plt.plot(xd, yd, marker='o', mfc='none', ms=25, mew=2, mec='r', label='SN '+r+' '+d, linestyle='none')
    plt.xlim(xd + fov/2, xd - fov/2)
    plt.ylim(yd - fov/2, yd + fov/2)

    # draw the compass
    xcomp = xd - 0.9*fov/2
    ycomp = yd - 0.9*fov/2
    #plt.arrow(xcomp, ycomp, 0, 1/60., fc='k', ec='none', length_includes_head=True)
    #plt.arrow(xcomp, ycomp, 1/60., 0, fc='k', ec='none', length_includes_head=True)
    plt.text(xcomp, ycomp+1/60., 'N', ha='center', va='bottom', size='large', weight='bold')
    plt.text(xcomp+1/60., ycomp, 'E', ha='right', va='center', size='large', weight='bold')
    #plt.text(xcomp+1/120., ycomp+0.001, "1'", ha='center', va='bottom', size='large', weight='bold')

    # find the reference stars
    print '>> Identify reference stars (mark with "<a> then press <q>")' 
    os.system('rm tmp1.coo')
    iraf.imexamine(img,1,logfile='tmp1.coo',keeplog='yes',wcs='world',xformat='%12.3H',yformat='%12.3h')
    iraf.tvmark(1,'tmp1.coo',mark="rectangle",number='yes',label='no',radii=10,nxoffse=5,lengths=10,nyoffse=5,color=204,txsize=4)
    xycoo1 = iraf.fields('tmp1.coo','1,2,3,4,13',Stdout=1)
    
    x0=string.split(r,':')[0]
    x1=string.split(r,':')[1]
    x2=string.split(r,':')[2]
    y0=string.split(d,':')[0]
    y1=string.split(d,':')[1]
    y2=string.split(d,':')[2]

    xx=int(x0)+((int(x1)+(float(x2)/60.))/60.)*15
    if '-' in str(y0):            yy=abs(int(y0))+((int(y1)+(float(y2)/60.))/60.)*(-1.)
    else:        yy=int(y0)+((int(y1)+(float(y2)/60.))/60.)
    simbolo=['d','*','p','s']
    colore=['b','g','m','c','w']
    for nn, i in enumerate(xycoo1):
        cx,cy=string.split(i)[0],string.split(i)[1]
        xr,yr=string.split(i)[2],string.split(i)[3]
        cxd = col2RA(float(cx))
        cyd = row2dec(float(cy))
        plt.plot(cxd, cyd, marker=simbolo[nn], mfc='none', ms=25, mew=2, mec=colore[nn], label='#'+str(nn+1)+' '+xr+' '+yr, linestyle='none')

        xr1 = string.split(xr,':')[0]+'h'+string.split(xr,':')[1]+'m'+string.split(xr,':')[2]+'s'
        yr1 = string.split(yr,':')[0]+'d'+string.split(yr,':')[1]+'m'+string.split(yr,':')[2]+'s'        
        r1 = string.split(r,':')[0]+'h'+string.split(r,':')[1]+'m'+string.split(r,':')[2]+'s'
        d1 = string.split(d,':')[0]+'d'+string.split(d,':')[1]+'m'+string.split(d,':')[2]+'s'

        mm2 = SkyCoord(r1, d1)
        mm1 = SkyCoord(xr1, yr1)        
        ra_offset = (mm2.ra - mm1.ra) * np.cos(mm1.dec.to('radian'))
        dec_offset = (mm2.dec - mm1.dec)

        AB = ra_offset.to('arcsec').value
        CD = dec_offset.to('arcsec').value

        ###### old way
        #x00=string.split(xr,':')[0]
        #x10=string.split(xr,':')[1]
        #x20=string.split(xr,':')[2]
        #y00=string.split(yr,':')[0]
        #y10=string.split(yr,':')[1]
        #y20=string.split(yr,':')[2]
        #xx0=(int(x00)+((int(x10)+(float(x20)/60.))/60.))*15
        #if '-' in str(y00):            yy0 = (abs(int(y00))+((int(y10)+(float(y20)/60.))/60.))*(-1.)
        #else:                          yy0 = int(y00)+((int(y10)+(float(y20)/60.))/60.)
        #print xx0,yy0
        #decmed=(yy+yy0)/2
        #AB=(xx-xx0)*3600*math.cos(decmed*math.pi/180)
        #AB=(xx-xx0)*3600*math.cos(yy0*math.pi/180)
        #CD=(yy-yy0)*3600
        
        print 'offset:', AB,CD
        if float(AB)<0:  AB1='W'
        else:            AB1='E'
        if float(CD)<0:  CD1='S'
        else:            CD1='N'
        plt.figtext(0.7, 0.7-nn*.06, 'From #'+str(nn+1)+' to SN', color=colore[nn], backgroundcolor='white', size='large')
        plt.figtext(0.7, 0.67-nn*.06, '{:4.2f}"{} {:4.2f}"{}'.format(abs(AB), str(AB1), abs(CD), str(CD1)), color=colore[nn], backgroundcolor='white', size='large')
    plt.legend(numpoints=1, markerscale=.6, loc=(1.1,.8), fancybox=True)

    # draw the inset
    ax = plt.axes([.62,.1,.35,.35])
    if _z1inset is None: _z1inset = _z1
    if _z2inset is None: _z2inset = _z2
    ax.imshow(X, cmap='gray_r', aspect='equal', interpolation='nearest', vmin=_z1inset, vmax=_z2inset, origin='lower', extent=(left, right, bottom, top))
    plt.xlabel('R.A. (degrees)')
    plt.xlabel('Dec. (degrees)')
    plt.title(name)
    ax.get_xaxis().get_major_formatter().set_useOffset(False)
    ax.get_yaxis().get_major_formatter().set_useOffset(False)
    ax.plot(xd, yd, marker='o', mfc='none', ms=25, mew=2, mec='r')
    plt.xlim(xd + fovinset/2, xd - fovinset/2)
    plt.ylim(yd - fovinset/2, yd + fovinset/2)
    ax.get_xaxis().set_major_locator(ticker.MultipleLocator(round(fovinset/3,3)))
    raw_input('\n Save the FC and then press <enter> ')

