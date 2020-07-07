import datetime
import json
class findmissing:
    def getnextdate(self,date,lastdate):
        current=(int(date[8] +date[9]))  
        lastday=(int(lastdate[8] +lastdate[9]))  
        if(lastday>current):
            return lastday-current
    def getvalues(self,value1,value2,num):
        return (value2-value1)/num
    def solution(self,dictionary):
        dict={}
        key=list(dictionary.keys())
        value=list(dictionary.values())
        dict[key[0]]=value[0]
        for i in range(0,int(len(key)-1)):
            if(key[0][:8]==key[1][:8]):
                if(len(key)==2):
                    noofday=self.getnextdate(key[0],key[len(key)-1])
                    valuedif=self.getvalues(value[0],value[1],noofday)
                    val=int(value[0])
                    for i in range(0,noofday):
                        val=val+valuedif
                        if(int(key[0][8]+key[0][9])<10):
                            dict[(key[0][:9])+str(int(key[0][9])+i+1)]=int(val)
                        else:
                            dict[(key[0][:8])+str(int(key[0][8]+key[0][9])+i+1)]=int(val)
                else:
                    for i in range(0,int(len(key)-1)):
                        if(int(key[i+1][8]+key[i+1][9])!=int(key[i][8]+key[i][9])+1):
                            dict[key[i]]=value[i]
                            noofday=self.getnextdate(key[i],key[i+1])
                            valuedif=self.getvalues(value[i],value[i+1],noofday)   
                            val=int(value[i])
                            for j in range(0,noofday):
                                val=val+valuedif
                                if(int(key[i][8]+key[i][9])+j+1>=10):
                                    date=key[i][:8]+str(int(key[i][8]+key[i][9])+j+1)
                                else:
                                    date=key[i][:9]+str(int(key[i][8]+key[i][9])+j+1)
                                dict[date]=int(val)
                
        print('Output -D = ',dict)

f=findmissing()
# inp={"2019-05-02":100,"2019-05-04":40,"2019-05-09":100,"2019-05-17":10}
inp=input('Input D = ')
res = json.loads(inp)
f.solution(res)
