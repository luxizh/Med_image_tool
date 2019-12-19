import csv
class Pro_csv():
    def __init__(self,filename):
        self.filename=filename
        with open(self.filename,'r') as f:
            f_reader=csv.reader(f)
            self.h=next(f_reader)
            self.rows=[row for row in f_reader]
    def sort_index(self,ind=0):
        self.rows.sort(key=lambda elem: elem[ind])
        print(self.rows)
        with open(self.filename,'w') as f:
            f_writer=csv.writer(f)
            f_writer.writerow(self.h)
            f_writer.writerows(self.rows)
    def count_Patient(self,write=False):
        #write whether write value in original csv file
        patient=set([row[0] for row in self.rows])
        if write:
            with open(self.filename,'a') as f:
                f_writer=csv.writer(f)
                f_writer.writerow([len(patient)])
        return len(patient)
    def auto_p(self):
        self.sort_index()
        self.count_Patient(write=True)

def main():
    savefolder='/Users/luxi/Desktop/Tencent-intern/med_image/test1'
    filename='summary'
    savename=savefolder+'/'+filename+'.csv'
    try:
        p_c=Pro_csv(savename)
    except:
        print("no such csv file!")
    else:
        p_c.auto_p()
        p_c.count_Patient(write=True)
    #print(savename)
    #f=open(savename,'w')
    #f.close()

if __name__ == "__main__":
    main()