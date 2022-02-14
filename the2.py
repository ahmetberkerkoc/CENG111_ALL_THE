txt=input().split("-")
if(txt[0].find("?")==-1 and txt[1].find("?")==-1):
        d1 = int(txt[0][0])
        d2 = int(txt[0][1])
        d3 = int(txt[0][2])
        d4 = int(txt[0][3])

        result= (2*d1+3*d2+5*d3+7*d4) % 11
        if result == 10:
                sresult= "X"
        else:
                sresult = str(result)

        if txt[1]==sresult:
                print("VALID")
        else:
                print("INVALID")

elif txt[1].find("?")!=-1:
        d1 = int(txt[0][0])
        d2 = int(txt[0][1])
        d3 = int(txt[0][2])
        d4 = int(txt[0][3])

        result= (2*d1+3*d2+5*d3+7*d4) % 11

        if result == 10:
                sresult= "X"
        else:
                sresult = str(result)
        print(txt[0]+"-"+sresult)

else:
        i=txt[0].find("?")
        if(txt[1]=="X"):
                ex=10
        else:
                ex=int(txt[1])
        if(i==0):

                d2 = int(txt[0][1])
                d3 = int(txt[0][2])
                d4 = int(txt[0][3])

                result= (3*d2+5*d3+7*d4) % 11
                temp=(11+ex-result) % 11
                inverse = 6 #inverse of  2
                temp = (temp*inverse) % 11

                sresult = str(temp)
                print(sresult+txt[0][1:]+"-"+txt[1])

        elif(i==1):
                d1 = int(txt[0][0])
                d3 = int(txt[0][2])
                d4 = int(txt[0][3])

                result= (2*d1+5*d3+7*d4) % 11
                temp=(11+ex-result)%11
                inverse = 4 #inverse of 3
                temp=(temp*inverse) % 11

                sresult = str(temp)
                print(txt[0][0]+sresult+txt[0][2:]+"-"+txt[1])
               
        elif(i==2):
                d2 = int(txt[0][1])
                d1 = int(txt[0][0])
                d4 = int(txt[0][3])

                result= (3*d2+2*d1+7*d4) % 11
                temp=(11+ex-result) % 11
                inverse = 9 #inverse of 5
                temp=(temp*inverse) % 11
               
                sresult = str(temp)
                print(txt[0][0:2]+sresult+txt[0][3]+"-"+txt[1])
               
        elif(i==3):
                d2 = int(txt[0][1])
                d1 = int(txt[0][0])
                d3 = int(txt[0][2])

                result= (3*d2+2*d1+5*d3) % 11
                temp=11+ex-result
                temp=(11+ex-result) % 11
                inverse = 8 #inverse of  7
                temp = (temp*inverse) % 11
               
                sresult = str(temp)
                print(txt[0][0:3]+sresult+"-"+txt[1])