import pydicom
import os

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
            s_path=s_path+'_'+str(self.ds.SeriesDescription)
        except:
            pass
        else:
            pass
        if not os.path.exists(s_path):
            os.makedirs(s_path)
        self.ds.save_as(s_path+'/'+self.filename)
    def auto_process(self,s_z=4,i_z=5):
        #s_z,i_z:zero fill series and instance
        try:
            self.anonymize()
        except:
            print('cannot get information:'self.filename)
            return 0
        else:
            pass
        try:
            self.rename(s_z,i_z)
        except:
            print('cannot get information:'self.filename)
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
    print('Anonymization and classifation have done!')
    return

inputs='/Users/luxi/Desktop/Tencent-intern/med_image/test'
inputs='/Users/luxi/Desktop/Tencent-intern/med_image/HU ZHEN XIU'
output='/Users/luxi/Desktop/Tencent-intern/med_image/test1'
batch_pro(inputs,output)
#print (os.listdir(inputs))
#print (len(os.listdir(inputs)))

 