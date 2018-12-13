import io

nameInList  = ["gram1.txt","gram2.txt", "gram3.txt", "gram4.txt"]
nameOutList = list()
cntIn       = 1 # how many input file
fInList     = list()
fOutList    = list()
dictWord    = dict()

#make Out file (use input file name)
for idx in range(cntIn):
    s = nameInList[idx].split(".")[0]+"_count.txt"
    nameOutList.append(s)
    fOutList.append(io.open(nameOutList[idx], encoding='utf-8', mode='w'))

# fileOpen
for idx in range(cntIn):
    fInList.append (io.open(nameInList[idx], encoding='utf-8', mode='r+'))

# read each file
for each in range(cntIn):
    dictWord = dict() # re-initialize at each file (gram2.txt, gram3.txt ...)
    while True:
        line = fInList[each].readline()
        if not line: break
        line = line.replace("\n", "")

        if len(line) > 1 :
#            print(line)
            if line in dictWord.keys():
                dictWord[line] = dictWord[line]+1
            else:
                dictWord[line] = 1

# Write on each out file
    for key, value in dictWord.items():
#        print(key+", "+str(value))
        fOutList[each].write(key+"\t"+str(value)+"\n")

