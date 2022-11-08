class student:
    #this is provide data
    college='acet'
    def __init__(self,name,age):#constructor
        self.__name=name#'__' indicates private class
        self.age=age
    def setdata(self,new):#to change private data
        self.__name=new
    def getdata(self):
        print(self.__name,self.age)

s1=student('viart',33)
s1.getdata()#prints virat 33
s1.setdata('kohli')#changes virat to kohli
s1.getdata()#prints kohli 33
        
    
