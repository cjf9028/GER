#-*- coding: utf-8 -*-
import sys
import io
#from imp import reload
#reload(sys)
#sys.setdefaultencoding('utf-8')
#hello

fin = io.open("../train_data", encoding='utf-8', mode='r+')

idxStart    = 2
idxEnd      = 4
nameList    = ["_", "_", "gram2.txt", "gram3.txt", "gram4.txt"]
fOutList    = list()
dictWord    = dict()

# fileOpen
for idx in range(0, idxStart):
    print("idx is "+str(idx))
    fOutList.append("_")

for idx in range(idxStart, idxEnd+1):
    fOutList.append( io.open(nameList[idx], encoding='utf-8', mode='w') )

while True:
    line = fin.readline()
    if not line: break
    # idxStart ~ idxEnd for
    # Split with each count (2, 3, 4)
    
    try:
        tag = line.split("\t")[2].replace("\n","")
        word = line.split("\t")[1]
        
        if len(tag) > 1 :
            newTag = tag.split("_")[0]

            for gram in range(idxStart, idxEnd+1): # change to idxEnd+1
                ll = len(word)
                s = "_"+word[0:gram-1] # count dict
                
                fOutList[gram].write(s+"\t"+newTag+"\n")
                for idx in range(ll):
                   
                    if idx+gram <= ll :
                        fOutList[gram].write(word[idx:idx+gram]) # count dict #
                    else:
                        remain = idx+gram-ll
                        
                        # if (length of word) is more than (gram-1),
                        if len(word) < gram-1:
                            fOutList[gram].write(word)
                        else:
                            fOutList[gram].write(word[idx:ll-remain+1])
                        
                        fOutList[gram].write(("_\t"+newTag+"\n"))
                    
                        break
                    fOutList[gram].write(("\t"+newTag+"\n"))
                fOutList[gram].write(("\n"))

    except IndexError:
        pass


# close file
fin.close()

for idx in range(idxStart, idxEnd+1):
    fOutList[idx].close()


#def addWordToDict(val, type) :
#    #    val:   넘길 text
#    #    type:  1=시작&진행중, -1=종료
#
#    if type is 1:
#        if val in dictWord.keys():
#            dictWord[word] = dictWord[word] + 1
#        else:
#            dictWord[word] = 0
#
#    if type is -1:
#        if val+"_"


