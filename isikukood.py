from module1 import *


for x in range(0,5,1)
print (x,end=", ")

ikood="" 
arvud=[]
ikoodid=[] 

while True:
    ikood=input("Sisesta isikukood -> ")
    if ikood=="0":break
    if pikkus(ikood)==False:
        print("Liiga pikk või lühike isikukood")
    else:
        s=sugu(ikood)
        if s=="viga":
            print("Esimene täht ei ole õige")
        else:
            print(s)
            if sunnipaev(ikood)=="viga":
                print("2-7 tähed on valesti sisestatud")
            else:
                print(sunnipaev(ikood)) 
                if sunnikoht(ikood)=="viga":
                    print("viga")
                else:
                    print(lause(ikood))
                    if kontrollnr(ikood)==int(ikood[-1]):
                        print("OK")
                        ikoodid.append(ikood)
                    else:
                        print("!!!")
print()
ikoodid=naised_mehed(ikoodid)
print(ikoodid) 
arvud=arvud_sorted(arvud) 
print(arvud) 