# Maybe it will work at Gachon Univ.
#-*- coding: utf-8 -*-
import sys
import io
reload(sys)
sys.setdefaultencoding('utf-8')

fin = io.open("../train_data", encoding='utf-8', mode='r+')

idxStart    = 2
idxEnd      = 4
nameList    = ["_", "_", "gram2.txt", "gram3.txt", "gram4.txt"]
fOutList    = list()
dictWord    = dict()

# open file
for idx in range(0, idxStart):
    print("idx is "+str(idx))
    fOutList.append("_")

for idx in range(idxStart, idxEnd+1):
    fOutList.append( io.open(nameList[idx], encoding='utf-8', mode='w') )

while True:
    line = fin.readline()
    if not line: break
    # idxStart ~ idxEnd for
    # Split with each count (2, 3, 4 ~ same with gram)
    
    try:
        tag = line.split("\t")[2].replace("\n","")
        word = line.split("\t")[1]
        
        if len(tag) > 1 :
            print(line+"[" + tag + "]")
            newTag = tag.split("_")[0]
            print(word)
            
            for gram in range(idxStart+1, idxEnd+2):
                ll = len(word)
                s = "_"+word[0:gram-1]]
                
                fOutList[gram].write(s+unicode("\t"+newTag+"\n"))
                for idx in range(ll):
                    
                    if idx+gram <= ll :
                        fOutList[gram].write(word[idx:idx+gram])
                    else:
                        fOutList[gram].write(unicode("_\t"+newTag+"\n"))
                        
                        break
                    fOutList[gram].write(unicode("\t"+newTag+"\n"))
            fOutList[gram].write(("\n"))

except IndexError:
    pass


# close file
fin.close()

for idx in range(idxStart, idxEnd+1):
    fOutList[idx].close()
