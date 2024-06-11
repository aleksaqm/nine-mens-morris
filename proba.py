from copy import deepcopy
from ssl import ALERT_DESCRIPTION_UNKNOWN_CA
import hashMap

tabla = hashMap.ChainedHashMap()

def start(): 
    tabla["1a"] = "o"
    tabla["1d"] = "o"
    tabla["1g"] = "o"
    tabla["2b"] = "o"
    tabla["2d"] = "o"
    tabla["2f"] = "o"
    tabla["3c"] = "o"
    tabla["3d"] = "o"
    tabla["3e"] = "o"
    tabla["4a"] = "o"
    tabla["4b"] = "o"
    tabla["4c"] = "o"
    tabla["4e"] = "o"
    tabla["4f"] = "o"
    tabla["4g"] = "o"
    tabla["5c"] = "o"
    tabla["5d"] = "o"
    tabla["5e"] = "o"
    tabla["6b"] = "o"
    tabla["6d"] = "o"
    tabla["6f"] = "o"
    tabla["7a"] = "o"
    tabla["7d"] = "o"
    tabla["7g"] = "o"
    draw()


def draw():
    razmak1="------------------------------"
    razmak2="--------------------"
    razmak3="----------"
    print("\n"+"7    "+tabla["7a"]+razmak1+tabla["7d"]+razmak1+tabla["7g"])
    print("     |                              |                              |")
    print("     |                              |                              |")
    print("     |                              |                              |")
    print("     |                              |                              |")
    print("6    |         "+tabla["6b"]+razmak2+tabla["6d"]+razmak2+tabla["6f"]+"         |")
    print("     |         |                    |                    |         |")
    print("     |         |                    |                    |         |")
    print("     |         |                    |                    |         |")
    print("     |         |                    |                    |         |")
    print("5    |         |         "+tabla["5c"]+razmak3+tabla["5d"]+razmak3+tabla["5e"]+"         |         |")
    print("     |         |         |                     |         |         |")
    print("     |         |         |                     |         |         |")
    print("     |         |         |                     |         |         |")
    print("     |         |         |                     |         |         |")
    print("4    "+tabla["4a"]+"---------"+tabla["4b"]+"---------"+tabla["4c"]+"                     "+tabla["4e"]+"---------"+tabla["4f"]+"---------"+tabla["4g"])
    print("     |         |         |                     |         |         |")
    print("     |         |         |                     |         |         |")
    print("     |         |         |                     |         |         |")
    print("     |         |         |                     |         |         |")
    print("3    |         |         "+tabla["3c"]+razmak3+tabla["3d"]+razmak3+tabla["3e"]+"         |         |")
    print("     |         |                    |                    |         |")
    print("     |         |                    |                    |         |")
    print("     |         |                    |                    |         |")
    print("     |         |                    |                    |         |")
    print("2    |         "+tabla["2b"]+razmak2+tabla["2d"]+razmak2+tabla["2f"]+"         |")
    print("     |                              |                              |")
    print("     |                              |                              |")
    print("     |                              |                              |")
    print("     |                              |                              |")
    print("1    "+tabla["1a"]+razmak1+tabla["1d"]+razmak1+tabla["1g"])
    print("\n"+"     a          b         c         d          e         f         g"+"\n")


    # for kljuc in tabla:
        #     if kljuc.startswith(broj) and kljuc != polje and tabla[kljuc]=="o":
        #         pomocna.append(kljuc)
        # vrednostSlova = ord(slovo)
        # if pomocna!=[]:
        #     minRazlika = vrednostSlova - ord(pomocna[0][1])
        #     for kljuc in pomocna:
        #         if vrednostSlova - ord(kljuc[1])<minRazlika:
        #             minRazlika = vrednostSlova - ord(kljuc[1])
        #     for kljuc in pomocna:
        #         if vrednostSlova - ord(kljuc[1]) == minRazlika:
        #             lista.append(kljuc)

        # for kljuc in tabla:
        #     if kljuc.endswith(slovo) and kljuc != polje and tabla[kljuc]=="o":
        #         pomocna.append(kljuc)
        # br = int(broj)
        # if pomocna!=[]:
        #     minRazlika = br - int(pomocna[0][0])
        #     for kljuc in pomocna:
        #         if br - int(kljuc[0])<minRazlika:
        #             minRazlika = br - int(kljuc[0])
        #     for kljuc in pomocna:
        #         if br - int(kljuc[0]) == minRazlika:
        #             lista.append(kljuc)

# def mogucaPolja(polje):
#     lista = []
#     broj = polje[0]
#     slovo = polje[1]

#     if broj == "1" or broj == "7":
#         minRazmak = 3
#     elif broj == "2" or broj=="6":
#         minRazmak = 2
#     elif broj == "3" or broj == "4" or broj == "5":
#         minRazmak=1
    
#     for kljuc in tabla:
#         if kljuc.startswith(broj) and tabla[kljuc]=="o":
#             if abs((ord(slovo)-ord(kljuc[1])))==minRazmak:
#                 lista.append(kljuc)

#     if slovo == "a" or slovo == "g":
#         minRazmak = 3
#     elif slovo == "b" or slovo=="f":
#         minRazmak = 2
#     elif slovo == "c" or slovo == "d" or slovo == "e":
#         minRazmak=1
    
#     for kljuc in tabla:
#         if kljuc.endswith(slovo) and tabla[kljuc]=="o":
#             if abs(int(broj)-int(kljuc[0]))==minRazmak:
#                 lista.append(kljuc)  

#     return lista 


# def brojTrojki(igrac):
#     trojke=0
#     for br in range(1,8):
#         brojac=0
#         brojac4a=0
#         brojac4b=0
#         for kljuc in tabla:
#             if br == 4:
#                 if kljuc.startswith(str(br)) and tabla[kljuc]==igrac and kljuc[1] in ["a","b","c"]:
#                     brojac4a+=1
#                 elif kljuc.startswith(str(br)) and tabla[kljuc]==igrac and kljuc[1] in ["e","f","g"]:
#                     brojac4b+=1

#             elif kljuc.startswith(str(br)) and tabla[kljuc]==igrac:
#                 brojac+=1
            
#             if brojac==3:
#                 trojke+=1
#                 brojac=0
#             if brojac4a==3:
#                 trojke+=1
#                 brojac4a=0
#             if brojac4b==3:
#                 trojke+=1
#                 brojac4b=0
    
#     for br in range(97,104):
#         brojac=0
#         brojac4a=0
#         brojac4b=0
#         for kljuc in tabla:
#             if br == 100:
#                 if kljuc.endswith(chr(br)) and tabla[kljuc]==igrac and kljuc[0] in ["1","2","3"]:
#                     brojac4a+=1
#                 elif kljuc.endswith(chr(br)) and tabla[kljuc]==igrac and kljuc[0] in ["5","6","7"]:
#                     brojac4b+=1

#             elif kljuc.endswith(chr(br)) and tabla[kljuc]==igrac:
#                 brojac+=1
            
#             if brojac==3:
#                 trojke+=1
#             if brojac4a==3:
#                 trojke+=1
#             if brojac4b==3:
#                 trojke+=1
    
#     return trojke




# def daLiMozeTrece(polje1,polje2,igrac):
#     broj1=polje1[0]
#     broj2=polje2[0]
#     slovo1=polje1[1]
#     slovo2=polje2[1]
#     if broj1==broj2:
#         for kljuc in tabla:

#             if broj1 == "4":
#                 niz = ["a","b","c"]
#                 if slovo1 in niz:
#                     niz.remove(slovo1)
#                     niz.remove(slovo2)
#                     if tabla[broj1+niz[0]]=="o":
#                         return True 
#                 else:
#                     niz = ["e","f","g"]
#                     niz.remove(slovo1)
#                     niz.remove(slovo2)
#                     if tabla[broj1+niz[0]]=="o":
#                         return True  

#             if kljuc.startswith(broj1) and kljuc != polje1 and kljuc != polje2:
#                 if tabla[kljuc] == "o":
#                     return True
#         return False
#     if slovo1==slovo2:
#         for kljuc in tabla:
#             if slovo1 == "d":
#                 niz = ["1","2","3"]
#                 if broj1 in niz:
#                     niz.remove(broj1)
#                     niz.remove(broj1)
#                     if tabla[niz[0]+slovo1]=="o":
#                         return True   
#                 else:
#                     niz = ["5","6","7"]
#                     niz.remove(broj1)
#                     niz.remove(broj1)
#                     if tabla[niz[0]+slovo1]=="o":
#                         return True       

#             if kljuc.endswith(slovo1) and kljuc != polje1 and kljuc != polje2:
#                 if tabla[kljuc] == "o":
#                     return True
#         return False




# def proveraDvaNiz(polje, igrac):
#     lista = okolo(polje,igrac)
#     if lista !=[]:
#         for li in lista:
#             if daLiMozeTrece(polje,li,igrac):
#                 return 50
#             else:
#                 return -20
#     else:
#         return 5





#def proveraTriNiz(igrac,kljuc):
#     broj = kljuc[0]
#     slovo=kljuc[1]
#     ima = True

#     if broj == "4":
#         if slovo in "abc":
#             if tabla["4a"]==igrac and tabla["4b"]==igrac and tabla["4c"]==igrac:
#                 return True
#         elif tabla["4e"]==igrac and tabla["4f"]==igrac and tabla["4g"]==igrac:
#             return True
    
#     if slovo == "d":
#         if broj in "123":
#             if tabla["1d"]==igrac and tabla["2d"]==igrac and tabla["3d"]==igrac:
#                 return True
#         elif tabla["5d"]==igrac and tabla["6d"]==igrac and tabla["7d"]==igrac:
#             return True
    
#     for kljuc in tabla:
#         if kljuc.startswith(broj) and tabla[kljuc] !=igrac:
#             ima = False
    
#     if ima==True:
#         return True

#     ima = True
#     for kljuc in tabla:   
#         if kljuc.endswith(slovo) and tabla[kljuc]!=igrac:
#             ima = False
        
#     return ima




# def okolo(polje,sta):
#     lista = []
#     broj = polje[0]
#     slovo = polje[1]

#     if broj == "1" or broj == "7":
#         minRazmak = 3
#     elif broj == "2" or broj=="6":
#         minRazmak = 2
#     elif broj == "3" or broj == "4" or broj == "5":
#         minRazmak=1
    
#     for kljuc in tabla:
#         if kljuc.startswith(broj) and tabla[kljuc]==sta:
#             if abs((ord(slovo)-ord(kljuc[1])))==minRazmak:
#                 lista.append(kljuc)

#     if slovo == "a" or slovo == "g":
#         minRazmak = 3
#     elif slovo == "b" or slovo=="f":
#         minRazmak = 2
#     elif slovo == "c" or slovo == "d" or slovo == "e":
#         minRazmak=1
    
#     for kljuc in tabla:
#         if kljuc.endswith(slovo) and tabla[kljuc]==sta:
#             if abs(int(broj)-int(kljuc[0]))==minRazmak:
#                 lista.append(kljuc)  

#     return lista

# def moguciPoteziFaza2(table):
#     lista = []
#     for polje in table:
#         if table[polje] and okolina(polje,"o")!=[]:
#             lista.append(polje)
#     return lista


def main():
    s = "aleksa"
    print(tabla["a"])    
    
    
        
        

if __name__=="__main__":
    main()