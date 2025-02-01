import easyocr
import re
import alicesql
import os
import numpy as np
import glob
import sys

def get_lines_from_pattern(text, start_pattern):
    """
    Get lines starting from a specific pattern.
    Args:
        text (str): The extracted text.
        start_pattern (str): The regex pattern to identify the starting line.
    Returns:
        list: Lines starting from the matched pattern.
    """
    # Split the text into lines
    lines = text.splitlines()
    
    # Flag to track when to start collecting lines
    collecting = False
    collected_lines = []
    
    # Iterate through lines
    for line in lines:
        if collecting:
            collected_lines.append(line)
        elif re.search(start_pattern, line):
            collecting = True
            collected_lines.append(line)
    
    return collected_lines

def extract_text_from_image(image_path):
    try:
        # Initialize the EasyOCR reader
        reader = easyocr.Reader(['en'],gpu=False)  # Add languages as needed, e.g., ['en', 'fr']
        
        # Perform OCR on the image
        results = reader.readtext(image_path, detail=0)  # Set detail=0 for plain text
        
        # Join results into a single string
        extracted_text = "\n".join(results)
        
        return extracted_text
    except Exception as e:
        return f"Error: {e}"

def find_SNid(_ra,_dec):
    hostname, username, passwd, database = alicesql.getconnection()
    conn = alicesql.dbConnect(hostname, username, passwd, database)
    command=['select id from idsupernovae where ra0='+str(_ra)+'and dec0='+str(_dec)]
    _targetid = alicesql.gettargetid(_name='',_ra=_ra,_dec=_dec,connection=conn)
    return _targetid
    
def find_SNname(_targetid):
    hostname, username, passwd, database = alicesql.getconnection()
    conn = alicesql.dbConnect(hostname, username, passwd, database)
    command=['select name from supernovanames where targetid='+str(_targetid)]
    _name = alicesql.query(command,conn)
    return _name[0]['name']


def ingest_to_database(_targetid,_SNname,nn,xr,yr,AB,CD,r,d):
    import alicesql
    hostname, username, passwd, database = alicesql.getconnection()
    conn = alicesql.dbConnect(hostname, username, passwd, database)
    dictionary2 ={'targetid':_targetid,
                  'name':_SNname +'_S'+str(nn+1),
                  'offset_EW': str(AB),
                  'offset_NS':str(CD),
                  'ra0':  xr,
                  'dec0': yr,
                  'SNname':_SNname,
                  'SN_RA':r,
                  'SN_Dec':d,
    }
    alicesql.insert_values(conn, 'offsetstars' ,dictionary2)
    
    


if __name__ == "__main__":
    files = glob.glob("/dark/hal/test_yize/finding_chart/*.png")
    for image_file_path in files:
        try:
                extracted_text = extract_text_from_image(image_file_path)

                start_pattern = r'SN' 
                lines_from_pattern = get_lines_from_pattern(extracted_text, start_pattern)
        
                SNpos = False
                stars = []
                stars_coord = []
                for line in lines_from_pattern:
                        if 'From' in line:
                                pass
                        elif 'SN' in line and SNpos is False:
                                SNpos = line
                        elif '"E' in line or '"N' in line or '"S' in line or '"W' in line:
                                stars.append(line)
                        elif '#' in line:
                                stars_coord.append(line)  
    
                SNcoord = SNpos.strip('SN ')
                RA = SNcoord.split(' ')[0]
                Dec = SNcoord.split(' ')[1]
    
                _ra=re.split(r'[:.]',RA)
                ra_deg=int(_ra[0])
                ra_min=int(_ra[1])
                ra_sec=float(_ra[2] + '.' + _ra[3])
    
                ra = (ra_deg + ra_min/60 + ra_sec/3600)*15
                
                ra0 = str(ra_deg).zfill(2) + ':' + str(ra_min).zfill(2) + ':' + str(_ra[2].zfill(2)+ '.'+_ra[3].zfill(2))
    
                _dec=re.split(r'[:.]',Dec) 
    
                if bool(re.search('-',_dec[0]))==True:
                        _dec[0]=_dec[0][1:]
                        dec_deg='-'+_dec[0].zfill(2)
                else:
                        dec_deg='+'+_dec[0].zfill(2) 
     
                dec_min=int(_dec[1])
                dec_sec=float(_dec[2] + '.' + _dec[3])
                
                dec0 = str(dec_deg) + ':' + str(dec_min).zfill(2) + ':' + str(_dec[2].zfill(2)+ '.'+_dec[3].zfill(2))
                
                dec = (int(_dec[0]) + dec_min/60 + dec_sec/3600)
    
                if int(_dec[0]) < 0 or _dec[0]=='-0':
                        dec_final = -1.00 * dec
                else:
                        dec_final = dec
           
                #Finding the SN in the database, or else picking the name from the filename
                targetid = find_SNid(ra,dec_final)
                if targetid == None:
                        fname = image_file_path.split('/')[5]
                        snname = re.split(r'[_.]',fname)[0]
                        snyear = re.split('(\D+)',snname)
                        if len(snyear[0])<4:
                                snyear_new = '20' + snyear[0]
                                SNname = snyear_new + snyear[1] 
                        else:
                                SNname = snname
                else:
                        SNname = find_SNname (targetid)
                print (SNname)
    
                for i,star in enumerate(stars):
                        offset_ew = float(star.split('"')[0])
                        offset_ew_dir = str((star.split('"')[1]).split(' ')[0])
                        offset_ns = float((star.split('"')[1]).split(' ')[1])
                        offset_ns_dir = str(star.split('"')[2])
        
                        offset_EW = 0
                        offset_NS = 0 
        
                        if offset_ew_dir == 'E':
                                offset_EW = 1.00 * offset_ew
                        elif offset_ew_dir == 'W':
                                offset_EW = -1.00 * offset_ew
            
                        if offset_ns_dir == 'N':
                                offset_NS = 1.00 * offset_ns
                        elif offset_ns_dir == 'S' or offset_ns_dir == '5' :
                                offset_NS = -1.00 * offset_ns
            
        
                        _coord = re.split(r'[\s-]+',stars_coord[i])
                        RA = _coord[1]
                        if len(_coord)<3:
                                index = lines_from_pattern.index(stars_coord[i]) 
                                Dec = lines_from_pattern[index+1]
                        else:
                                Dec = _coord[2]
        
                        _ra=re.split(r'[:.]',RA)
                        ra_deg=int(_ra[0])
                        ra_min=int(_ra[1])
                        ra_sec=float(_ra[2] + '.' + _ra[3])
    
                        ra = (ra_deg + ra_min/60 + ra_sec/3600)*15
                        
                        ra_star = str(ra_deg).zfill(2) + ':' + str(ra_min).zfill(2) + ':' + str(_ra[2].zfill(2)+ '.' + _ra[3].zfill(2))
        
                        _dec=re.split(r'[:.]',Dec) 
        
                        if bool(re.search('-',stars_coord[i]))==True:
                                dec_deg='-'+_dec[0].zfill(2)
                        else:
                                dec_deg='+'+_dec[0].zfill(2) 
            
                        dec_min=int(_dec[1])
                        dec_sec=float(_dec[2] + '.' + _dec[3])
                        dec_star = str(dec_deg) + ':' + str(dec_min).zfill(2) + ':' + str(_dec[2].zfill(2)+ '.' + _dec[3].zfill(2))
    
                        ingest_to_database(targetid,SNname,i,ra_star,dec_star,offset_EW,offset_NS,ra0,dec0)
    
        except Exception as e:
                f = open("error_log.txt","a")
                f.write(image_file_path + ':' + str(e))
                f.close()
                            
        
        
        #dec = (abs(dec_deg) + dec_min/60 + dec_sec/3600)
        #if dec_deg < 0 or _dec[0]=='-0' or bool(re.search('-',stars_coord[i]))==True:
        #    dec_final = -1.00 * dec
        #else:
        #    dec_final = dec
        
        
        
        

    
  
