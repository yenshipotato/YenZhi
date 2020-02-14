#顏值app-------------------------------------------------------------------------------------------------------------------
inf = ["class",0,0]
yen = {"name" : inf}
yarr = [yen]

fp = open("Yen.txt","r",encoding="utf-8")

#--------------------------------------------------------------------------------------------------------------------------
while True:
    line = fp.readline()

    if not line:
        break

    ltemp = line.split()
    inf[1] = float(ltemp[1])

    if len(ltemp) > 3 :
        inf[2]=int((ltemp[3])[1])

    if inf[1]>=9601:
        clss="S.L.U.T"
    elif inf[1]>=1000:
        clss="sub-S.L.U.T"
    elif inf[1]>=70:
        clss="beef"
    elif inf[1]>=36:
        clss="middle class"
    elif inf[1]>10:
        clss="REM"
    else :
        clss="untouchable"

    inf[0] = clss
    yen = {ltemp[0] : inf}
    yarr.append(yen)

    inf = ["class",0,0]
    yen = {"name" : inf}
yarr.pop(0)
#--------------------------------------------------------------------------------------------------------------------------
while True :
    ind = int(input("input an index. (0 for list , 1 for search , 2 for edit , 3 for append , 4 for exit) : "))
    if ind == 4:
        break

    elif ind ==1:
        n = input("input name : ")

        for b in yarr :
            if(b.__contains__(n)):
                print(b)


    elif ind ==0:
        for b in yarr:
            print(b)

    elif ind == 3:
        name= input("input name : ")
        inf[1] = float(input("input value : "))
        inf[2] = int(input("input # of girlfriend : "))

    r=1+(10/(inf[1]-100))
    a=10*r
    sum1=0
    for i in range(0,inf[2]):
        sum1=sum1+10*(r**i)
    inf[1]=inf[1]+sum1
    yen={name : inf}    
    
    yarr.append(yen)
    yarr.sort(key = lambda s:(list(s.values()))[0][1],reverse = True)
#---------------------------------------------------------------------------------------------------------------------------