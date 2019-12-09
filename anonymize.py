import pydicom
import os

class Medimage_tool():
    def __init__(self,filename,savefolder):
        self.ds=pydicom.dcmread(filename)
        #sname=filename.rpartition('/')
        self.filename=(filename.rpartition('/'))[2]
        self.savefolder=savefolder
    def anonymize(self):
        self.ds.PatientName=m.ds.PatientID+'_'+m.ds.StudyDate
    def rename(self):
        pass
        self.filename='1.dcm'
    def save_class(self):
        pass
        path=self.savefolder+'/'+str(self.ds.PatientName)+'/'+str(self.ds.PatientName)+'_'+str(self.ds.SeriesNumber)
        if not os.path.exists(path):
            os.makedirs(path)
        self.ds.save_as(path+'/'+self.filename)
    def auto_process(self):
        self.anonymize()
        #self.rename()
        self.save_class()


filename='/Users/luxi/Desktop/Tencent-intern/med_image/test/IMG-0001-00001.dcm'
savefolder='/Users/luxi/Desktop/Tencent-intern/med_image/test'
m=Medimage_tool(filename,savefolder)
print(m.ds.PatientName)
m.ds.PatientName=m.ds.PatientID+'_'+m.ds.StudyDate
print(m.ds.PatientName)
print(m.ds.SeriesNumber)
m.auto_process()