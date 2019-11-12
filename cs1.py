import sys,re,threading,time,string

dict={}

#Taking files from CMD and inserting into the list
ls=[]
l=[]
for i in range(1,4):
    ls.append(sys.argv[i])
#print("Given Files:",ls)

#File for reading
def file_read():
    for i in range(0,len(ls)):
        x=open(ls[i],'r')
        words=0
        lines=0
        for j in x:
            lines+=1
            words+=sum([k.strip(string.punctuation).isalpha() for k in j.split()]) 
        #print(lines,"lns",words,"wds")
        dict[ls[i]]=(lines,words)
        time.sleep(.3)
        #print("read done",len(dict))
        
def fn_lst():
    for i in range(len(ls)):
        time.sleep(.3)
        x=sorted(dict.items(),key=lambda k1:k1[1])
        if i == len(ls)-1:
            for i in x:
                #print(i)
                l.append(i)
        #print(l)
        
    
        
t=time.time()

t1=threading.Thread(target=file_read)
t2=threading.Thread(target=fn_lst)
        
t1.start()
t2.start()

t1.join()
t2.join()

if threading.current_thread() is threading.main_thread():
    for i in l:
        s1=str(i).replace('(','').replace(')','').replace(',','').replace("'",'')
        print(s1)
      
