#!/opt/epd/bin/python
description='Make a finding chart.'
usage= "%prog  image [--z1 zmin --z2 zmax ]\n"
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#from pyraf import iraf
import os,string,re,sys
import math
import argparse
import csv
#try:
#    import pyfits
#except:
#    from astropy.io import fits as pyfits
    
import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u
#iraf.set(stdimage='imt4096')
import alicesql






def find_offsets(_name):
    hostname, username, passwd, database = alicesql.getconnection()
    conn = alicesql.dbConnect(hostname, username, passwd, database)
    command=['select name,ra0,dec0,offset_EW,offset_NS from offsetstars where SNname='+"'"+_name+"'"]
    _list = alicesql.query(command,conn)
    #if bool(re.search('-',_list[i]['dec0']))==True:
     #       dec_deg='-'+_dec[0].zfill(2)
    #else:
     #       dec_deg='+'_dec[0].zfill(2)
    
    return [(_list[i]['name'],_list[i]['ra0'],_list[i]['dec0'],2000.0,"#raoffset="+str(format(float(_list[i]['offset_EW']),".2f")),"decoffset="+str(format(float(_list[i]['offset_NS']),".2f"))) for i in range(len(_list))]
       

def find_SN(_name):
    hostname, username, passwd, database = alicesql.getconnection()
    conn = alicesql.dbConnect(hostname, username, passwd, database)
    command=['select SNname,SN_RA,SN_Dec from offsetstars where SNname='+"'"+_name+"'"]
    _list = alicesql.query(command,conn)
    #for i in range(len(_list)):
    return (_list[0]['SNname'],_list[0]['SN_RA'],_list[0]['SN_Dec'],2000.0,'','')

def find_std(std):
    fname = '/dark/hal/test_darshana/standards.txt'
    stdname = np.genfromtxt(fname,dtype=str,delimiter=',',comments='#',usecols=0)
    stdra = np.genfromtxt(fname,dtype=str,delimiter=',',comments='#',usecols=1)
    stddec = np.genfromtxt(fname,dtype=str,delimiter=',',comments='#',usecols=2)
    stddata = []
    if std in stdname:
        index = np.where(stdname == std)[0][0]
        stddata.append (stdname[index]+' '+stdra[index]+' '+stddec[index]+' '+'2000.0'+''+'')
    else:
        stddata.append ('SORRY! Couldn`t find this standard in the list. Please update with details in /dark/hal/test_darshana/standards.txt and try again!')
    return stddata

       
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--names', nargs='+', help='List of names of the supernova seperated by space e.g. 2024xxa 2024xxb ..')
    parser.add_argument('-s', '--stds', nargs='+', help='List of either 2 or 4 standards seperated by space e.g. BDxxx HZxx ... The first one/two will be placed in the beginning of the night and the last one/two at the end')
    parser.add_argument('-o', '--output', nargs='+', help='Output starlist name in .txt, e.g. starlist_20250101.txt')
    parser.add_argument('-b', '--backups', nargs='+', help='List of names of the backups seperated by space e.g. 2024xxa 2024xxb ..')
    args = parser.parse_args()

    if args.names:
       with open(str(args.output[0]),'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ') 
            headers = ["#name","ra_hms","dec_dms","equinox","RA_OFFSET","DEC_OFFSET"]
            writer.writerow(headers)
           
            if len(args.stds) == 2:
               s1 = args.stds[0]
               s2 = args.stds[1]
               writer.writerow(find_std(s1))
                
            
               for name in args.names:
                   writer.writerow(find_SN(name))
                   offsets = find_offsets(name)
                   for o in offsets: 
                       writer.writerow(o)
                
               writer.writerow(find_std(s2))
               pass
                
            elif len(args.stds) == 4:
                 s1 = args.stds[0]
                 s2 = args.stds[1]
                 writer.writerow(find_std(s1))
                 writer.writerow(find_std(s2))
                 for name in args.names:
                     writer.writerow(find_SN(name))
                     offsets = find_offsets(name)
                     for o in offsets: 
                         writer.writerow(o)
                 s3 = args.stds[2]
                 s4 = args.stds[3]
                 writer.writerow(find_std(s3))
                 writer.writerow(find_std(s4))
                 pass

           
            if args.backups: 
               writer.writerow('#Backups')
               for name in args.backups:
                   writer.writerow(find_SN(name))
                   offsets = find_offsets(name)
                   for o in offsets: 
                       writer.writerow(o)
           
           		
       with open(str(args.output[0]),'r') as f:
            text = f.read()
       
       text = text.replace('"','')
       
       with open(str(args.output[0]),'w') as f:
            f.write(text)

if __name__ == "__main__":
    main()

