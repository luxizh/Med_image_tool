import os
import pydicom
import csv

class Series_inf():
    def __init__(self,root):
        self.root=root
        self.PatientName=''
        self.SeriesNumber=''
        self.SeriesDescription=''
        self.SliceThickness=''
        self.SpacingBetweenSlices=''
    def get_inf(self):
        for filename in os.listdir(self.root):
            f_path=os.path.join(self.root,filename)
            try:
                ds=pydicom.dcmread(f_path)
            except:
                pass
            else:
                try:
                    self.PatientName=str(ds.PatientName)
                except:
                    print('ERROR: '+f_path)
                    return False
                else:
                    pass
                try:
                    self.SeriesNumber=str(ds.SeriesNumber)
                except:
                    print('ERROR: '+f_path)
                    return False
                else:
                    pass
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
                #get parameter from one file and then stop init
                #print(1)
                return True
        #print(0)
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
            if not os.path.isfile(i):
                count+=1
        return count
    def get_series(self):
        return self.SeriesNumber
    def auto_write(self,savename):
        number=self.get_number()
        f=open(savename,'a')
        f_csv=csv.writer(f,lineterminator='\n')
        #print([self.PatientName,self.SeriesNumber+self.SeriesDescription,number,
        #                self.SliceThickness,self.SpacingBetweenSlices])
        #f_csv.writerow([self.PatientName,'S'+(self.SeriesNumber).zfill(4)+'_'+self.SeriesDescription,number,
        #                self.SliceThickness,self.SpacingBetweenSlices])
        f_csv.writerow([self.PatientName,os.path.basename(self.root),number,
                        self.SliceThickness])
        f.close()
        print('Summary in \''+self.root+'\' has been recorded!')
        pass


def batch_sum(root,savename):
    #print(root)
    if os.path.isdir(root):
        s_inf=Series_inf(root)
        if (s_inf.get_inf()):
            s_inf.auto_write(savename)
    f_list=os.listdir(root)
    f_list.sort()
    for lists in f_list: 
        c_path = os.path.join(root, lists)
        if os.path.isdir(c_path):
            batch_sum(c_path,savename)
        else:
            pass
            #print(path)
    return

def main():
    root='I:/CT_1'
    root_list=['Nasopharyngeal','Lung','Colorectal','Breast','Neuroendocrine','Gastric','Gastrointestinal_stromal','Pancreatic']
    root_list=['Cholangiocarcinoma','Hepatocellular_carcinoma']
    savefolder='I:/CT_1'
    if not os.path.exists(savefolder):
        os.makefile(savefolder)
    for i in root_list:
        filename='summary_'+i
        savename=savefolder+'/'+filename+'.csv'
        #print(savename)
        #f=open(savename,'w')
        #f.close()
        f=open(savename,'w')
        f_csv=csv.writer(f,lineterminator='\n')
        f_csv.writerow(['Date and Patient','Series and Description','Number of Slices',
                        'Slice Thickness'])
        f.close()
        batch_sum(root+'/'+i,savename)

if __name__ == "__main__":
    main()
