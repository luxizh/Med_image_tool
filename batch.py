import os
import pydicom

class Series_inf():
    def __init__(self,root):
        self.root=root
        self.PatientName=''
        self.SeriesNumber=''
        self.SeriesDescription=''
        self.SliceThickness=''
        self.SpacingBetweenSlices=''
    def get_inf():
        for filename in os.listdir(self.root): 
            try:
                ds=pydicom.dcmread(filename)
            except:
                pass
            else:
                self.PatientName=str(ds.PatientName)
                self.SeriesNumber=str(ds.SeriesNumber)
                #series description
                try:
                    self.SeriesDescription=str(ds.SeriesDescription)
                except:
                    self.SeriesDescription=''
                else:
                    pass
                #slice thickness
                try:
                    self.SliceThickness=str(ds.SliceThickness)
                except:
                    self.SliceThickness=''
                else:
                    pass
                #Spacing Between Slices
                try:
                    self.SpacingBetweenSlices=str(ds.SpacingBetweenSlices)
                except:
                    self.SpacingBetweenSlices=''
                else:
                    pass
                #get parameter from one file and then stop init
                return True
        return False
        #no files or cannot read any of them
    def get_number(self):
        l=os.listdir(self.root)
        #remove file from mac
        while '.DS_Store' in l:
            l.remove('.DS_Store')
        #count file number
        count=0
        for i in l:
            if os.isfile(i):
                count+=1
        return count
    def get_series(self):
        return self.SeriesNumber
    def auto_write(self,savename):
        pass


def batch_pro(root,savefolder): 
    for lists in os.listdir(root): 
        c_path = os.path.join(root, lists)  
        if os.path.isdir(c_path):
            s_inf=Series_inf(c_path)
            if (s_inf.get_inf()):
                s_inf.auto_write(savename)
                #lack savename
            batch_pro(c_path,savefolder)
        else:
            pass
            #print(path)
    return

inputs='/Users/luxi/Desktop/Tencent-intern/med_image/test'
inputs='/Users/luxi/Desktop/Tencent-intern/med_image/HU ZHEN XIU/DICOM'
output='/Users/luxi/Desktop/Tencent-intern/med_image/test1'
batch_pro(inputs,output)
