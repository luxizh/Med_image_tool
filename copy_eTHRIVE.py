# -*- coding: utf-8 -*-
import shutil
import os
import csv
import pydicom

#institution name
#e-THRIVE 

def dcmcopy(get_path,save_path):
    for files in os.listdir(get_path):
        get_name=os.path.join(get_path,files)
        save_name=os.path.join(save_path,files)
        try:
            ds=pydicom.dcmread(get_name)
        except:
            print("Warning: Not a dcm file!")
        else:
            #hide institution name
            try:
                ds.InstitutionName='Anonymous'
            except:
                print('Warning: No institution information!')
            else:
                pass
            #save to another folder
            try:
                ds.save_as(save_name)
            except
                print('Error: Save Error!')
            else:
                pass
            
def extract_an(row,root,filename,i):
    get_path=root+i+'/'+row[0]+'/'+row[1]
    save_path=root+i+'_e-THRIVE/'+row[0]+'/'+row[1]
    if not os.path.exists(save_path):
        os.makefile(save_path)
    dcmcopy(get_path,save_path)
    fw=open(filename,'w')
    fw_csv=csv.writer(f,lineterminator='\n')
    fw_csv.writerow(row)
    fw.close()
    pass

def main():
    root='G:/class_'
    filename='G:/summary'
    year_list=['2016','2017','2018','2019']
    for i in year_list:
        fw=open(filename+i+'_e-THRIVE.csv','w')
        fw_csv=csv.writer(f,lineterminator='\n')
        fw_csv.writerow(['Date and Patient','Series and Description','Number of Slices',
                        'Slice Thickness','Spacing Between Silces'])
        fw.close()
        f=open(filename+i+'.csv','r')
        f_reader=csv.reader(f)
            self.h=next(f_reader)
        for row in f_reader:
            if row[2]>=300 and str(row[1]).endswith('e-THRIVE_dyn_BH'):
                extract_an(row,root,filename+i+'_e-THRIVE.csv',i)
        f_csv=csv.writer(f,lineterminator='\n'))
        f.close()
    savename=filename+'.csv'
    #print(savename)
    #f=open(savename,'w')
    #f.close()

if __name__ == "__main__":
    main()