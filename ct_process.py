# -*- coding: utf-8 -*-
import pydicom
import os
import pickle
import csv
import imghdr
import shutil
class Medimage_tool():
    def __init__(self,filename,savefolder):
        self.ds=pydicom.dcmread(filename)
        #sname=filename.rpartition('/')
        self.filename=os.path.basename(filename)
        self.savefolder=savefolder
        self.AnonymizeName=''
        self.Institution=''
    def get_patient_info(self):
        #get basic information
        self.AnonymizeName='D'+str(self.ds.StudyDate)+'_'+str(self.ds.PatientID)
        try:
            self.Institution=str(self.ds.InstitutionName)
        except:
            print('Warning: No institution information!')
        else:
            self.ds.InstitutionName='Anonymous'
            #Anonymising
        #todo: add instance number and series number to here
    def check_id(self,id_set):
        #return patient Name and ID dictionary
        if self.AnonymizeName not in id_set:
            content=(str(self.AnonymizeName),str(self.ds.PatientName),str(self.Institution))
            return content
        else:
            return False     
    def anonymize(self):
        self.ds.PatientName=self.AnonymizeName
        '''
        #in get_patient_info function
        try:
            self.ds.InstitutionName='Anonymous'
        except:
            print('Warning: No institution information!')
        else:
            pass
        '''
    def rename(self,s_z,a_z,i_z):
        #s_z,i_z:zero fill series and instance
        #rename file as 
        pass
        tname=self.filename.rpartition('.')
        #remain its original type
        self.filename=('S'+str(self.ds.SeriesNumber).zfill(s_z)+'_'+
                        'A'+str(self.ds.AcquisitionNumber).zfill(a_z)+'_'+
                        str(self.ds.InstanceNumber).zfill(i_z)
                        )
        if tname[2]=='dcm':
            self.filename+=tname[1]+tname[2]
        else:
            pass
    def save_class(self,s_z,a_z):
        #save dcm in new folder with new name
        pass
        s_path=(self.savefolder+'/'+str(self.AnonymizeName)+'/'+
                #str(self.AnonymizeName)+
                '_S'+str(self.ds.SeriesNumber).zfill(s_z)+
                '_A'+str(self.ds.AcquisitionNumber).zfill(a_z)
                )
        '''
        #check Series Description
        try:
            sd_path=s_path+'_'+str(self.ds.SeriesDescription)
        except:
            print('Warning: No Series Description!')
        else:
            pass
        #check whether Series Description is valid for name
        try:
            if not os.path.exists(sd_path):
                os.makedirs(sd_path)
        except:
            print('Warning: Series Description cannot be used as file name!')
            if not os.path.exists(s_path):
                os.makedirs(s_path)
        else:
            s_path=sd_path
        '''
        if not os.path.exists(s_path):
            os.makedirs(s_path)
        #save
        try:
            self.ds.save_as(s_path+'/'+self.filename)
        except:
            print('Error: Save Error!')
            with open('error.pkl','ab') as f:
                pickle.dump('Error5:'+s_path+'/'+self.filename,f)
    def auto_process(self,id_set=set(),s_z=4,a_z=3,i_z=5):
        #s_z,i_z:zero fill series and instance
        #get information
        try:
            self.get_patient_info()
        except:
            print('Error: Cannot get patient information from'+self.filename)
            input('Continue1')
            return 0
        else:
            pass
        #record patient information
        try:
            content=self.check_id(id_set)
        except:
            print('Error: Cannot check id from'+self.filename)
            input('Continue2')
        else:
            pass
        #anonymize
        try:
            self.anonymize()
        except:
            print('Error: Cannot anonymizing from '+self.filename)
            input('Continue3')
            return 0
        else:
            pass
        #rename and save
        try:
            self.rename(s_z,a_z,i_z)
        except:
            print('Error: cannot rename file in '+self.filename)
            input('Continue4')
            return 0
        else:
            pass
        self.save_class(s_z,a_z)
        return content

#===================excute function=======================
def batch_pro(root,savefolder): 
    #DFS for root folder
    global flodername
    image_list=[]
    for lists in os.listdir(root): 
        c_path = os.path.join(root, lists)
        if os.path.isdir(c_path): 
            batch_pro(c_path,savefolder)
        elif imghdr.what(c_path):
            image_list.append(c_path)
        else:
            #m=Medimage_tool(path,savefolder)
            try:
                m=Medimage_tool(c_path,savefolder)
            except:
                pass
                print('Error0: Cannot open as dcm: '+c_path)    
            else:
                #m.auto_process()
                content=m.auto_process(id_set=id_set_g)
                #global var
                set_record(content)
                flodername=m.AnonymizeName
    for images in image_list:
        try:
            shutil.copy(images,savefolder+'/'+flodername)
        except:
            print('Error: Image Copy Error!')
            with open('error.pkl','ab') as f:
                pickle.dump('Error6:'+c_path,f)
        else:
            print('Image has been saved.')
    #print('Anonymization and classifation have done!')
    print('Files in \''+root+'\' have been processed!')
    return 

#import pickle
def split_inputs(output_folder,input_folder=None,l_folder=None):
    #batch process for list folder path
    #and for restarting from stopping point recorded in todo.pkl file
    if l_folder:
        #l_folder.extend(os.listdir(input_folder))
        pass
    else:
        l_folder=os.listdir(input_folder)
    while len(l_folder):
        i=l_folder.pop()
        i_path=os.path.join(input_folder,i)
        if os.path.isdir(i_path):
            batch_pro(i_path,output_folder)
        #l_folder.remove(i)
        f=open('todo.pkl','wb')
        pickle.dump(l_folder,f)
        f.close()

def set_record(content):
    #save PatientID and information
    #global var dict
    '''
    content=m.get_patient_dict(id_set)
    '''
    if content:
        f=open(idset_name,'a')
        f_csv=csv.writer(f,lineterminator='\n')
        #for windows avoiding extra empty rows
        f_csv.writerow(content)
        f.close()
        id_set_g.add(content[0])
    else:
        pass

def get_set(idset_name):
    global id_set_g
    with open(idset_name,'r') as f:
        f_reader=csv.reader(f)
        h=next(f_reader)
        col=[row[0] for row in f_reader]
        id_set_g=set(col)

        
#============================================================
#=======================usage example========================
#============================================================
output_list=['Lung','Colorectal','Breast','Neuroendocrine','Gastric','Gastrointestinal_stromal','Pancreatic']
input_list=['肺癌','结直肠癌','乳腺癌','神经内分泌肿瘤','胃癌','胃肠间质瘤','胰腺癌']
for ii in range(len(input_list)):
    id_set_g=set()
    idset_path='I:/CT_2/'+output_list[ii]
    if not os.path.exists(idset_path):
        os.makedirs(idset_path)
    idset_name=idset_path+'/PatientInformation.csv'
    #write headline
    f=open(idset_name,'w')
    f_csv=csv.writer(f,lineterminator='\n')
    f_csv.writerow(('Data_PatientID','Patient Name','Institution Name'))
    f.close()
    inputs='I:/转移瘤/'+input_list[ii]
    output='I:/CT_2/'+output_list[ii]
    split_inputs(output,input_folder=inputs)
'''
#id record prepare
id_set_g=set()
idset_path='I:/CT_2/Nasopharyngeal'
if not os.path.exists(idset_path):
    os.makedirs(idset_path)
idset_name=idset_path+'/PatientInformation.csv'
#write headline
f=open(idset_name,'w')
f_csv=csv.writer(f,lineterminator='\n')
f_csv.writerow(('Data_PatientID','Patient Name','Institution Name'))
f.close()
'''
'''
idset_path='I:/CT_1/Hepatocellular_carcinoma'
idset_name=idset_path+'/PatientInformation.csv'
get_set(idset_name)
'''
#===========================================================
#process
#inputs='I:/肝细胞癌与胆管细胞癌/胆管细胞癌'
#output='I:/CT_1/Cholangiocarcinoma'

#batch_pro(inputs,output)

#split_inputs(output,input_folder=inputs)
'''
inputs='I:/肝细胞癌与胆管细胞癌/肝细胞癌'
output='I:/CT_1/Hepatocellular_carcinoma'

f=open('todo.pkl','rb')
l_inputs=pickle.load(f)
f.close()
print(l_inputs)
split_inputs(output,input_folder=inputs,l_folder=l_inputs)
'''

'''
inputs='I:/转移瘤/鼻咽癌'
output='I:/CT_2/Nasopharyngeal'
split_inputs(output,input_folder=inputs)
'''

#f_todo=open('todo.pkl','r')
#todo_folder=pickle.load(f_todo)
#f_todo.close()


print('Done! All files have been preocessed!')
#print (os.listdir(inputs))
#print (len(os.listdir(inputs)))