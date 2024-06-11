
from ast import Return
from cmath import inf
from copy import deepcopy
import math
import os
import hashMap
from time import time
import os




tabla = hashMap.ChainedHashMap()
moguceTrojke = [["1a","1d","1g"],["2b","2d","2f"],["3c","3d","3e"],["4a","4b","4c"],["4e","4f","4g"],["5c","5d","5e"],["6b","6d","6f"],["7a","7d","7g"],["1a","4a","7a"],["2b","4b","6b"],["3c","4c","5c"],["1d","2d","3d"],["5d","6d","7d"],["3e","4e","5e"],["2f","4f","6f"],["1g","4g","7g"]]
okoline = hashMap.Map()
kontra = hashMap.Map()


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
    okoline["1a"] = ["1d","4a"]
    okoline["1d"] = ["1a","1g","2d"]
    okoline["1g"] = ["1d","4g"]
    okoline["2b"] = ["4b","2d"]
    okoline["2d"] = ["2b","2f","3d","1d"]
    okoline["2f"] = ["4f","2d"]
    okoline["3c"] = ["3d","4c"]
    okoline["3d"] = ["3c","3e","2d"]
    okoline["3e"] = ["3d","4e"]
    okoline["4a"] = ["4b","1a","7a"]
    okoline["4b"] = ["4a","4c","2b","6b"]
    okoline["4c"] = ["4b","5c","3c"]
    okoline["4e"] = ["4f","5e","3e"]
    okoline["4f"] = ["4e","4g","2f","6f"]
    okoline["4g"] = ["4f","1g","7g"]
    okoline["5c"] = ["5d","4c"]
    okoline["5d"] = ["5c","5e","6d"]
    okoline["5e"] = ["5d","4e"]
    okoline["6b"] = ["4b","6d"]
    okoline["6d"] = ["6b","6f","5d","7d"]
    okoline["6f"] = ["4f","6d"]
    okoline["7a"] = ["7d","4a"]
    okoline["7d"] = ["7a","7g","6d"]
    okoline["7g"] = ["7d","4g"]

    kontra["1a"] = "7g"
    kontra["1d"] = "7d"
    kontra["1g"] = "7a"
    kontra["2b"] = "6f"
    kontra["2d"] = "6d"
    kontra["2f"] = "6b"
    kontra["3c"] = "5e"
    kontra["3d"] = "5d"
    kontra["3e"] = "5c"
    kontra["4a"] = "4g"
    kontra["4b"] = "4f"
    kontra["4c"] = "4e"
    kontra["4e"] = "4c"
    kontra["4f"] = "4b"
    kontra["4g"] = "4a"
    kontra["5c"] = "3e"
    kontra["5d"] = "3d"
    kontra["5e"] = "3c"
    kontra["6b"] = "2f"
    kontra["6d"] = "2d"
    kontra["6f"] = "2b"
    kontra["7a"] = "1g"
    kontra["7d"] = "1d"
    kontra["7g"] = "1a"


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)



def draw():
    # os.system('cls' if os.name == 'nt' else 'clear')
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
    print("\n"+"     a         b        c           d          e         f         g"+"\n")



def prvaFaza(igrac):
    x=0
    if igrac == "X":
        while x<9:     
            postavi("X")
            startTime = time()    
            polje = nextMove(tabla,4,"Y",x)
            endTime = time()
            tabla[polje]="Y"
            draw()
            if proveraTriUnizu(tabla,"Y",polje):
                obrisi = brisanje(tabla,"Y")          
                tabla[obrisi]="o"
                draw()
                print("bot je obrisao vase polje : " + obrisi)
            print("\n"+"bot je odigrao na polje "+polje)
            trajanje = endTime-startTime
            print(trajanje)
            
            
            print("\n"+"ostalo je jos "+str(8-x)+" polja da se unese")
            # postavi("Y")
            x+=1
        return
    elif igrac == "Y":
        while x<9:     
            # postavi("X")
            startTime = time()    
            polje = nextMove(tabla,4,"X",x)
            endTime = time()
            tabla[polje]="X"
            draw()
            if proveraTriUnizu(tabla,"X",polje):
                obrisi = brisanje(tabla,"X")
                tabla[obrisi]="o"
                draw()
                print("bot je obrisao vase polje : " + obrisi)
            print(polje)
            trajanje = endTime-startTime
            print(trajanje)
            
            print("\n"+"bot je odigrao")
            print("\n"+"ostalo je jos "+str(8-x)+" polja da se unese")
            postavi("Y")
            x+=1
        return
    
def postavi(igrac):
    while True:
        print(dostupnaPoljaa("o"))
        polje = input("igrac "+igrac+" na koje polje zelis da postavis figuru : ")
        polje = polje.lower()
        for kljuc in tabla:
            if polje == kljuc and tabla[kljuc]=="o":
                tabla[kljuc]=igrac
                if proveraTriUnizu(tabla,igrac,kljuc):
                    draw()
                    izbacivanje(igrac)
                draw()
                return
        print("to polje nije dostupno, probajte ponovo ")
        continue


def proveraTriUnizu(table,igrac,kljuc):
    for trojka in moguceTrojke: 
        if kljuc in trojka:
            ima = True
            for polje in trojka:
                if table[polje]!=igrac:
                    ima = False
            if ima:
                return ima
    return False


def izbacivanje(igrac):
    if igrac == "X":
        protivnik = "Y"
    else:
        protivnik = "X"
    
    print("\n"+"imate 3 u nizu, to vam omogucava da izbacite jednu protivnikovu figuru (ne mozete izbaciti figuru ako vec formira trojku)")
    while True:
        polje = input("koje protivnikovo polje bi da izbacite : ")
        polje = polje.lower()
        NeMoze = True
        for kljuc in tabla:
            if polje == kljuc and tabla[kljuc]==protivnik and not proveraTriUnizu(tabla,protivnik,kljuc):
                tabla[kljuc]="o"
                draw()
                return
            
            if tabla[kljuc]==protivnik and not proveraTriUnizu(tabla,protivnik,kljuc):
                NeMoze = False

        if NeMoze == True:
            if tabla[polje]==protivnik:
                tabla[polje]="o"
                draw()
                return      

        print("ne mozete izbaciti sa tog polja ")
        continue
            

def drugaFaza(igrac):
    a = True
    b = True
    if igrac == "X":
        while(a==True and b== True):
            a = odigraj("X")
            if a == False:
                break
            draw()
            dubina = 5
            if kraj(tabla,"X"):
                break
            t1 = time()

            if kraj(tabla,"Y"):
                b=False
                break

            polje1,polje2 = nextMove2(tabla,dubina,"Y")

            while polje1 == None or polje2 == None:
                polje1,polje2 = nextMove2(tabla,dubina-1,"Y")
                dubina-=1

            t2 = time()
            tabla[polje1]="o"
            tabla[polje2] = "Y"
            
            
            draw()
            trajanje = t2-t1
            print(trajanje)
            print("bot je odigrao ")
            print(t2-t1)
            print("bot je stavio figuru sa polja "+polje1)
            print("na polje "+polje2)
            if proveraTriUnizu(tabla,"Y",polje2):
                obrisi = brisanje2(tabla,"Y")
                
                tabla[obrisi]="o"
                draw()
                print("bot je obrisao vase polje "+obrisi)
                print("bot je stavio figuru sa polja "+polje1)
                print("na polje "+polje2)
            
            # b = odigraj("Y")
            # if b == False:
            #     break
            # draw()
    elif igrac == "Y":
        while(a==True and b== True):
            # a = odigraj("X")
            # if a == False:
            #     break
            # draw()
            dubina = 5
            if kraj(tabla,"X"):
                a=False
                break
            t1 = time()
            polje1,polje2 = nextMove2(tabla,dubina,"X")

            while polje1 == None or polje2 == None:
                polje1,polje2 = nextMove2(tabla,dubina-1,"X")
                dubina-=1

            t2 = time()
            tabla[polje1]="o"
            tabla[polje2] = "X"
            trajanje = t2-t1
            
            draw()
            print("bot je odigrao ")
            print(trajanje)
            print("bot je stavio figuru sa polja "+polje1)
            print("na polje "+polje2)
            if proveraTriUnizu(tabla,"X",polje2):
                obrisi = brisanje2(tabla,"X")
                
                tabla[obrisi]="o"
                draw()
                print("bot je obrisao vase polje "+obrisi)
                print("bot je stavio figuru sa polja "+polje1)
                print("na polje "+polje2)
            
            b = odigraj("Y")
            if b == False:
                break
            draw()


        
    print("\n"+"===================================================================")
    print("kraj igre ")
    if a== False:
        print("pobednik je igrac Y ")
    else:
        print("pobednik je igrac X") 
    
def dostupnaPoljaa(sta):
    lista = []
    for kljuc in tabla:
        if tabla[kljuc]==sta:
            lista.append(kljuc)
    return lista

def odigraj(igrac):

    if kraj(tabla,igrac)==True:
        return False

    while True:
        polje = input("igracu "+igrac+" sa kojom bi ste figurom da igrate : ")
        if tabla[polje] != igrac:
            print("ne mozete odigrati sa tom figurom, pokusajte opet ")
            continue
        lista = okolina(polje,"o")

        s= ""
        for i in lista:
            s+=i
            s+=" , "
        if s.endswith(", "):
            s= s[:-2]

        print("tu figuru mozete staviti na sledeca polja : "+s)
        print(lista)

        
        nazad = False
        while True:
            polje2 = input("na koje od tih polja bi ste da pomerite vasu figuru : (unesite x za povratak nazad) ")
            if polje2=="x":
                nazad = True
                break
            if polje2 not in lista:
                print("to nije jedno od ponudjenih polja, probajte opet ")
                continue
            pomeri(polje,polje2,igrac)
            print(drugaFazaHeuristika(tabla,igrac,polje2))
            return True
        if nazad == True:
            continue
        

def okolina(polje,sta):
    lista=[]
    sve = okoline[polje]
    for i in sve:
        if tabla[i]==sta:
            lista.append(i)
    return lista




def pomeri(polje1,polje2,igrac):
    tabla[polje2]=tabla[polje1]
    tabla[polje1]="o"

    if proveraTriUnizu(tabla,igrac,polje2):
        draw()
        izbacivanje(igrac)

    return

        
def kraj(table,igrac):
    brojac = 0
    mozeDaMrda=False
    for kljuc in table:
        if table[kljuc]==igrac:
            if okolina(kljuc,"o")!=[]:
                mozeDaMrda=True
            brojac+=1
    if brojac<=2 or mozeDaMrda==False:
        return True
    else:
        return False 
    




def brTrojki(table,igrac):
    brojac = 0
    for trojka in moguceTrojke:
        ima = True
        for kljuc in trojka:
            if table[kljuc]!=igrac:
                ima = False
        if ima == True:
            brojac+=1
    return brojac


def brBlokiranih(table,igrac):
    brojac = 0
    for kljuc in tabla:
        if table[kljuc]==igrac and okolina(kljuc,"o")==[]:
            brojac +=1
    return brojac

def brFigura(table,igrac):
    brojac=0
    for kljuc in tabla:
        if table[kljuc] == igrac:
            brojac+=1
    return brojac


def brDvojki(table,igrac):
    brojac = 0
    for trojka in moguceTrojke:
        ima = True
        a=0
        b=0
        for kljuc in trojka:
            if table[kljuc]==igrac:
                a+=1
            elif table[kljuc]=="o":
                b+=1
        if a==2 and b==1:
            brojac+=1
    return brojac

def multiDvojke(table,igrac):
    lista=[]
    brojac = 0
    for trojka in moguceTrojke:
        ima = True
        a=0
        b=0
        for kljuc in trojka:
            if table[kljuc]==igrac:
                a+=1
            elif table[kljuc]=="o":
                b+=1
        if a==2 and b==1:
            for t in trojka:
                if table[t]!="o":
                    lista.append(t)
    for kljuc in table:
        if lista.count(kljuc)==2:
            brojac+=1
    
    return brojac

def multiTrojke(table,igrac):
    lista = []
    brojac = 0
    for trojka in moguceTrojke:
        ima = True
        for kljuc in trojka:
            if table[kljuc]!=igrac:
                ima = False
        if ima == True: 
            for kljuc in trojka:
                lista.append(kljuc)
    
    for kljuc in table:
        if lista.count(kljuc)==2:
            brojac+=1
    
    return brojac



def prvaFazaHeuristika(table,igrac,polje):
    poeni = 0
    if igrac == "X":
        protivnik = "Y"
    else:
        protivnik = "X"
    
    if proveraTriUnizu(table,igrac,polje):
        br1 = 1
    else:
        br1 = 0

    br2 = brTrojki(table,igrac)-brTrojki(table,protivnik)
    br3 = brBlokiranih(table,igrac)-brBlokiranih(table,protivnik)
    br4 = brFigura(table,igrac) - brFigura(table,protivnik)
    br5 = brDvojki(table,igrac) - brDvojki(table,protivnik)
    br6 = multiDvojke(table,igrac) - multiDvojke(table,protivnik)
    # br7 = multiTrojke(table,igrac) - multiTrojke(table,protivnik)

    poeni =50*br1 + 26*br2 + 1*br3 + 9*br4 + 10*br5 + 7*br6
    return poeni

def moguciPoteziFaza1(table):
    lista = []
    for kljuc in tabla:
        if table[kljuc]=="o":
            lista.append(kljuc)
    return lista


def prviPotez(table,igrac):
    if igrac == "X":
        return "1a"
    else:
        for polje in table:
            if table[polje] == "X":
                return kontra[polje]
        


def nextMove(table,dubina,igrac,x):
    if x == 0:
        potez = prviPotez(table,igrac)
        return potez             
    table=deepcopy(table)                               
    bestMove = None
    alfa = -math.inf
    if igrac == "X":
            protivnik = "Y"
    else:
        protivnik = "X"
    for potez in moguciPoteziFaza1(table):
        table[potez]=igrac
        
        if proveraTriUnizu(table,igrac,potez):
            return potez
        rezultat = minScore(table,dubina-1,alfa,math.inf,protivnik,potez)
        if rezultat > alfa:
            alfa = rezultat
            bestMove = potez
        if alfa >= -20 and x<2:                           
            break
        table[potez]="o"
    return bestMove



def minScore(table,dubina,alfa,beta,igrac,potez1):              
    if dubina<=0:
        return prvaFazaHeuristika(table,igrac,potez1)
    if igrac == "X":
            protivnik = "Y"
    else:
        protivnik = "X"
    for potez in moguciPoteziFaza1(table):
        table[potez]=igrac
        
        if proveraTriUnizu(table,igrac,potez) and dubina ==3:              
            return -150
        rezultat = maxScore(table,dubina-1,alfa,beta,protivnik,potez)
        beta = min(beta,rezultat)
        table[potez]="o"
        if alfa>=beta:
            return alfa
        
    return beta

def maxScore(table,dubina,alfa,beta,igrac,potez1):
    if dubina<=0:
        return prvaFazaHeuristika(table,igrac,potez1)
    if igrac == "X":
            protivnik = "Y"
    else:
        protivnik = "X"
    for potez in moguciPoteziFaza1(table):
        table[potez]=igrac
        
        # if proveraTriUnizu(table,igrac,potez):
        #     return -150
        rezultat = minScore(table,dubina-1,alfa,beta,protivnik,potez)
        alfa = max(alfa,rezultat)
        table[potez]="o"
        if alfa >= beta:
            return beta
    
    return alfa


def otvoriZatvori(table,igrac):
    trojke = []
    if igrac == "X":
        protivnik = "Y"
    else:
        protivnik = "X"
    for trojka in moguceTrojke:
        ima = True
        for kljuc in trojka:
            if table[kljuc]!=igrac:
                ima = False
        if ima == True:
            trojke.append(trojka)
    for kljuc in trojka:
        ima = True
        if okolina(kljuc,"o")!=[]:
            for polje in okolina(kljuc,"o"):
                if table[polje]==protivnik:
                    ima = False
    return ima


def drugaFazaHeuristika(table,igrac,polje):
    poeni = 0
    if igrac == "X":
        protivnik = "Y"
    else:
        protivnik = "X"
    
    if proveraTriUnizu(table,igrac,polje):
        br1 = 1
    else:
        br1 = 0
    
    if kraj(table,igrac)==True:
        br8 = -1
    elif kraj(table,protivnik)==True:
        br8=1
    else:
        br8 = 0

    if otvoriZatvori(table,igrac):
        br9 = 1
    else:
        br9=0
    
    if otvoriZatvori(table,protivnik) == False:
        br10 = 1
    else:
        br10 = -1

    br2 = brTrojki(table,igrac)-brTrojki(table,protivnik)
    br3 = brBlokiranih(table,igrac)-brBlokiranih(table,protivnik)
    br4 = brFigura(table,igrac) - brFigura(table,protivnik)
    # br5 = brDvojki(table,igrac) - brDvojki(table,protivnik)
    # br6 = multiDvojke(table,igrac) - multiDvojke(table,protivnik)
    br7 = multiTrojke(table,igrac) - multiTrojke(table,protivnik)

    poeni = 20*br1 +43 * br2 + 10*br3 + 11*br4 + 8*br7 + 1086 * br8 + 60*br9 + 30*br10
    return poeni



def nextMove2(table,dubina,igrac):
    table=deepcopy(table)
    bestMove1 = None
    bestMove2 = None
    alfa = -math.inf
    if igrac == "X":
        protivnik = "Y"
    else:
        protivnik = "X"
    
    for potez in table:
        lista = okolina(potez,"o")
        if table[potez]!=igrac or lista==[]:
            continue
        for potez2 in lista:
            table[potez2] = igrac
            table[potez] = "o"
            if proveraTriUnizu(table,igrac,potez2):
                return potez,potez2
            rezultat = minScore2(table,dubina-1,alfa,math.inf,protivnik,potez2)
            # print(rezultat)

            if rezultat>alfa:
                alfa = rezultat
                bestMove1 = potez
                bestMove2 = potez2

            table[potez] = igrac
            table[potez2] = "o"
    return bestMove1,bestMove2


def minScore2(table,dubina,alfa,beta,igrac,potez1):
    if dubina <= 0:
        return drugaFazaHeuristika(table,igrac,potez1)

    if igrac == "X":
        protivnik = "Y"
    else:
        protivnik = "X"

    for potez in table:
        lista = okolina(potez,"o")
        if table[potez]!=igrac or lista==[]:
            continue
        for potez2 in lista:
            table[potez2] = igrac
            table[potez] = "o"
            if proveraTriUnizu(table,igrac,potez2):    
                return -2000
            rezultat = maxScore2(table,dubina-1,alfa,beta,protivnik,potez2)
            beta = min(beta,rezultat)

            table[potez] = igrac
            table[potez2] = "o"

            if alfa>=beta:
                return alfa
            
    return beta

def maxScore2(table,dubina,alfa,beta,igrac,potez1):
    if dubina <= 0:
        return drugaFazaHeuristika(table,igrac,potez1)

    if igrac == "X":
        protivnik = "Y"
    else:
        protivnik = "X"

    for potez in table:
        lista = okolina(potez,"o")
        if table[potez]!=igrac or lista==[]:
            continue
        for potez2 in lista:
            table[potez2] = igrac
            table[potez] = "o"

            # if proveraTriUnizu(table,igrac,potez2):
            #     if dubina == 3 or dubina ==1:
            #         return 200
            
            rezultat = minScore2(table,dubina-1,alfa,beta,protivnik,potez2)
            alfa = max(alfa,rezultat)
            
            table[potez] = igrac
            table[potez2] = "o"

            if alfa>=beta:
                return beta

    return alfa
    




def brisanje(table,igrac):
    table=deepcopy(table)
    if igrac == "X":
        protivnik = "Y"
    else:
        protivnik = "X"

    best = None
    bestHeur = -math.inf
    NeMoze=True
    for kljuc in table:
        if table[kljuc] == protivnik and not proveraTriUnizu(table,protivnik,kljuc):
            table[kljuc] = "o"
            heur = prvaFazaHeuristika(table,igrac,None)
            if heur>bestHeur:
                bestHeur = heur
                best = kljuc

            if tabla[kljuc]==protivnik and not proveraTriUnizu(tabla,protivnik,kljuc):
                NeMoze = False

            table[kljuc]=protivnik
    
    if NeMoze == True:
         for kljuc in table:
            if table[kljuc] == protivnik:
                table[kljuc] = "o"
                heur = prvaFazaHeuristika(table,igrac,None)
                if heur>bestHeur:
                    bestHeur = heur
                    best = kljuc

    return best

def brisanje2(table,igrac):
    table=deepcopy(table)
    if igrac == "X":
        protivnik = "Y"
    else:
        protivnik = "X"

    best = None
    bestHeur = -math.inf
    NeMoze = True
    for kljuc in table:
        if table[kljuc] == protivnik and not proveraTriUnizu(table,protivnik,kljuc):
            table[kljuc] = "o"
            heur = drugafazaHeur2(table,igrac)
            if heur>bestHeur:
                bestHeur = heur
                best = kljuc
            
            if tabla[kljuc]==protivnik and not proveraTriUnizu(tabla,protivnik,kljuc):
                NeMoze = False

            table[kljuc]=protivnik
    
    if NeMoze == True:
         for kljuc in table:
            if table[kljuc] == protivnik:
                table[kljuc] = "o"
                heur = drugafazaHeur2(table,igrac)
                if heur>bestHeur:
                    bestHeur = heur
                    best = kljuc

    return best

def drugafazaHeur2(table,igrac):
    poeni = 0
    if igrac == "X":
        protivnik = "Y"
    else:
        protivnik = "X"
    
    if kraj(table,igrac)==True:
        br8 = -1
    elif kraj(table,protivnik)==True:
        br8=1
    else:
        br8 = 0

    if otvoriZatvori(table,igrac):
        br9 = 1
    else:
        br9=0

    br2 = brTrojki(table,igrac)-brTrojki(table,protivnik)
    br3 = brBlokiranih(table,igrac)-brBlokiranih(table,protivnik)
    br4 = brFigura(table,igrac) - brFigura(table,protivnik)
    br5 = brDvojki(table,igrac) - brDvojki(table,protivnik)
    # br6 = multiDvojke(table,igrac) - multiDvojke(table,protivnik)
    br7 = multiTrojke(table,igrac) - multiTrojke(table,protivnik)

    poeni = 20*br5 +43 * br2 + 10*br3 + 11*br4 + 8*br7 + 1086 * br8 + 30*br9
    return poeni



def main():
    start()
    
    while True:
        koji = input("hocete li da igrate prvi ili drugi (unesite 1 za prvi 2 za drugi)")
        if koji == "1":
            igrac = "X"
            break
        elif koji == "2":
            igrac = "Y"
            break
        else:
            print("lose ste uneli probajte ponovo ")
            continue
    prvaFaza(igrac)
    print("\n"+"=================================================="+"\n"+"kraj prve faze, idemo na glavnu igru "+"\n"+"====================================================")
    drugaFaza(igrac)
    
    
        
        

if __name__=="__main__":
    main()