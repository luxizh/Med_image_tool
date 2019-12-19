# -*- coding: utf-8 -*-
import pydicom
import os
import pickle
class Medimage_tool():
    def __init__(self,filename,savefolder):
        self.ds=pydicom.dcmread(filename)
        #sname=filename.rpartition('/')
        self.filename=os.path.basename(filename)
        self.savefolder=savefolder
    def anonymize(self):
            self.ds.PatientName='D'+self.ds.StudyDate+'_'+self.ds.PatientID
    def rename(self,s_z,i_z):
        #s_z,i_z:zero fill series and instance
        #rename file as 
        pass
        tname=self.filename.partition('.')
        #remain its original type
        self.filename=('S'+str(self.ds.SeriesNumber).zfill(s_z)+'_'+
                        str(self.ds.InstanceNumber).zfill(i_z)+tname[1]+tname[2]
                        )
    def save_class(self,s_z):
        #save dcm in new folder with new name
        pass
        s_path=(self.savefolder+'/'+str(self.ds.PatientName)+'/'+
                str(self.ds.PatientName)+'_S'+
                str(self.ds.SeriesNumber).zfill(s_z)
                )
        try:
            sd_path=s_path+'_'+str(self.ds.SeriesDescription)
        except:
            pass
        else:
            pass
        try:
            if not os.path.exists(sd_path):
                os.makedirs(sd_path)
        except:
            if not os.path.exists(s_path):
                os.makedirs(s_path)
        else:
            s_path=sd_path
        try:
            self.ds.save_as(s_path+'/'+self.filename)
        except:
            print('save error!')
            with open('error.pkl','ab') as f:
                pickle.dump(s_path+'/'+self.filename,f)
    def auto_process(self,s_z=4,i_z=5):
        #s_z,i_z:zero fill series and instance
        try:
            self.anonymize()
        except:
            print('cannot get information:'+self.filename)
            return 0
        else:
            pass
        try:
            self.rename(s_z,i_z)
        except:
            print('cannot get information:'+self.filename)
            return 0
        else:
            pass
        self.save_class(s_z)



'''
filename='/Users/luxi/Desktop/Tencent-intern/med_image/test/IMG-0001-00012.dcm'
savefolder='/Users/luxi/Desktop/Tencent-intern/med_image/test'

m=Medimage_tool(filename,savefolder)
print(m.ds.InstanceNumber)
#print(m.ds.PatientName)
#m.ds.PatientName=m.ds.PatientID+'_'+m.ds.StudyDate
#print(m.ds.PatientName)
#print(m.ds.SeriesNumber)
#m.auto_process()


'''

def batch_pro(root,savefolder): 
    for lists in os.listdir(root): 
        c_path = os.path.join(root, lists)  
        if os.path.isdir(c_path): 
            batch_pro(c_path,savefolder)
        else:
            #m=Medimage_tool(path,savefolder)
            try:
                m=Medimage_tool(c_path,savefolder)
            except:
                pass
            else:
                m.auto_process()
            #print(path)
    #print('Anonymization and classifation have done!')
    print('Files in \''+root+'\' have been processed!')
    return

#import pickle
def split_inputs(output_folder,input_folder=None,l_folder=None):
    if l_folder:
        #l_folder.extend(os.listdir(input_folder))
        pass
    else:
        l_folder=os.listdir(input_folder)
    for i in l_folder:
        i_path=os.path.join(input_folder,i)
        if os.path.isdir(i_path):
            batch_pro(i_path,output_folder)
        l_folder.remove(i)
        f=open('todo.pkl','wb')
        pickle.dump(l_folder,f)
        f.close()
inputs='/Users/luxi/Desktop/Tencent-intern/med_image/test'
#inputs='H:/Tencen_Med/2016'
inputs='H:/Tencen_Med/2019/05'
output='G:/class_2019'
#batch_pro(inputs,output)

#split_inputs(output,input_folder=inputs)
'''
f=open('todo.pkl','rb')
l_inputs=pickle.load(f)
f.close()
print(l_inputs)
split_inputs(output,input_folder=inputs,l_folder=l_inputs)
'''
inputs='H:/普美显数据-腾讯-拜耳/2019'
l_mon=['06-补','07','08','09','10','11']
for mon_e in l_mon:
    split_inputs(output,input_folder=inputs+'/'+mon_e)
'''
inputs='H:/Tencen_Med/2018'
output='G:/class_2018'
l_mon=['01','02','03','04']
for mon_e in l_mon:
    split_inputs(output,input_folder=inputs+'/'+mon_e)
'''

#f_todo=open('todo.pkl','r')
#todo_folder=pickle.load(f_todo)
#f_todo.close()


print('Done! All files have been preocessed!')
#print (os.listdir(inputs))
#print (len(os.listdir(inputs)))

