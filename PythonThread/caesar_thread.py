# -*- coding: cp1254 -*-
import threading
import time
import Queue
import sys
exitFlag = 0
class  crThread(threading.Thread):
    def __init__(self,threadID,name,que):
        threading.Thread.__init__(self)
        self.threadID =threadID
        self.name=name
        self.que=que
    def run(self):
        print "Starting " + self.name
        sifrele(self.name,self.que,s)
        print "Exiting " + self.name
        


def sifrele(nameThread,que,kaydirma):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            word=que.get()
            
            alfabe=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            dict={}
            for i in range(0,len(alfabe)):
                x=(i+kaydirma)%len(alfabe)
                dict[alfabe[x]]=alfabe[i]
            
            sifrelimetin="";
            for j in word.lower():
                if j in dict:
                    j=dict[j]
                sifrelimetin+=j
            f = open("crypted_7_3_5.txt","a")
            f.write(sifrelimetin.upper())
            f.close()
            queueLock.release()
            
            print(nameThread+":"+sifrelimetin.upper())
            
                
        else:
            
           queueLock.release()
           
        time.sleep(1)    






f = open("metin.txt","r")
myList = []
for line in f.readlines():
    myList.append(line)
print(myList)
f.close()


s=raw_input("Kaydırmayı giriniz:")
n=raw_input("Thread sayısını giriniz:")
l=raw_input("Okuma miktarını giriniz:")
l=int(l)
n=int(n)
s=int(s)

count=0
threadList=[]
dataList=[]
for d in range(n):
    threadList.append("Thread"+str(d))
for metin in myList:
    lengmetin=len(metin)
    while  count <=(lengmetin/l):
        dataList.append(metin[count*l:(count+1)*l])
        count+=1
    count=0    
print(dataList)   

queueLock = threading.Lock()    
workQueue = Queue.Queue(len(dataList))
threads = []
threadID = 1
print(threadList)
for tName in threadList:
    thread=crThread(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID +=1
    
queueLock.acquire()
for data in dataList:
    workQueue.put(data)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1
for t in threads:
    t.join()
print ("Exiting Main Thread")    

            
        
