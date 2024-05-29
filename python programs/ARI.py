from sys import argv

script,filename=argv
txt=open(filename)
data=txt.read()

WORD_COUNT=len(data.split())
print (WORD_COUNT)

CHAR_COUNT=len(data)
print(CHAR_COUNT)

SENT_COUNT=data.count('.')+data.count('?')+data.count('!')
print(SENT_COUNT)

ARI=int(4.71 * (CHAR_COUNT/WORD_COUNT) + 0.5 * (WORD_COUNT/SENT_COUNT) - 21.43)
print(ARI)

if (ARI==0):
    print("Group:Kinder Garden")
elif (ARI==1):
    print("Group:Kinder Garden")
elif (ARI==2):
    print("Group:First Grade")
elif (ARI==3):
    print("Group:Second Grade")
elif (ARI==4):
    print("Group:Third Grade")
elif(ARI==5):    
    print("Group:Fourth Grade")
elif (ARI==6):
    print("Group:Fifth Grade")
elif (ARI==7):
    print("Group:Sixth Grade")
elif (ARI==8):
    print("Group:Seventh Grade")
elif(ARI==9):    
    print("Group:Eighth Grade")
elif(ARI==10):    
    print("Group:Ninth Grade")
elif (ARI==11):
    print("Group:Tenth Grade")
elif (ARI==12):
    print("Group:Eleventh Grade")
elif (ARI==13):
    print("Group:Twelth Grade")
elif(ARI==14):    
    print("Group:College Students")

