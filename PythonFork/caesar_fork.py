# -*- coding: cp1254 -*-
from multiprocessing import Lock, Process, Queue, current_process

import sys
import time
def sifrele(work_queue,done_queue,kaydirma):
    for word in iter(work_queue.get, "STOP"):
        alfabe=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        dict={}
        for i in range(0,len(alfabe)):
            x=(i+kaydirma)%len(alfabe)
            dict[alfabe[x]]=alfabe[i]
        cl.acquire()
        sifrelimetin="";
        for j in word.lower():
            if j in dict:
                j=dict[j]
            sifrelimetin+=j
        f = open("crypted_7_3_5.txt","a")
        f.write(sifrelimetin.upper())
        cl.release()

         
        f.close()
        done_queue.put("%s - %s " % (current_process().name,sifrelimetin.upper()))
        

s=raw_input("Kaydırmayı giriniz:")
n=raw_input("Proceses sayısını giriniz:")
l=raw_input("Okuma miktarını giriniz:")
l=int(l)
n=int(n)
s=int(s)
f = open("metin.txt","r")
myList = []
for line in f.readlines():
    myList.append(line)
print(myList)
f.close()
work_queue = Queue()
done_queue = Queue()
cl=Lock()
count=0

processes = []
dataList=[]

for metin in myList:
    lengmetin=len(metin)
    while count <=(lengmetin/l):
        dataList.append(metin[count*l:(count+1)*l])
        count+=1
    count=0    
print(dataList)   

for data in dataList:
		work_queue.put(data)
 
kaydirma=s
for w in xrange(n):
	
 	   p = Process(target=sifrele, args=(work_queue, done_queue,kaydirma))
 	   p.start()
    	   processes.append(p)
    	   work_queue.put("STOP")



for p in processes:
    p.join()
done_queue.put("STOP")    


for status in iter(done_queue.get, "STOP"):
    print status




            
        
