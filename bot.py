from cmath import inf
import imp
import math
import hashMap


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
        if table[kljuc]==igrac and okolo(kljuc,"o")==[]:
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



def prvaFazaHeuristika(table,igrac):
    # ti postavljas to polje i onda racunas kakva je situacija na tabli 
    poeni = 0
    igrac = "X"
    protivnik = "Y"


    br2 = brTrojki(table,igrac)-brTrojki(table,protivnik)
    br3 = brBlokiranih(table,igrac)-brBlokiranih(table,protivnik)
    br4 = brFigura(table,igrac) - brFigura(table,protivnik)
    br5 = brDvojki(table,igrac) - brFigura(table,protivnik)
    br6 = multiDvojke(table,igrac) - multiDvojke(table,protivnik)
    br7 = multiTrojke(table,igrac) - multiTrojke(table,protivnik)

    poeni = 26*br2 + 1*br3 + 9*br4 + 10*br5 + 7*br6
    return poeni

def moguciPoteziFaza1(table):
    lista = []
    for kljuc in tabla:
        if table[kljuc]=="o":
            lista.append(kljuc)
    return lista


def nextMove(table,dubina,igrac):
    bestMove = None
    alfa = -math.inf
    for potez in moguciPoteziFaza1(table):
        table[potez]=igrac
        rezultat = minScore(table,dubina-1,alfa,math.inf,igrac)
        if rezultat > alfa:
            alfa = rezultat
            bestMove = potez
        # if alfa >= maximalniMoguciSkor:                           nisam siguran
        #     break

    return bestMove



def minScore(table,dubina,alfa,beta,igrac):
    if dubina<=0:
        return prvaFazaHeuristika(table,igrac)
    for potez in moguciPoteziFaza1(table):
        table[potez]=igrac
        rezultat = maxScore(table,dubina-1,alfa,beta)
        beta = min(beta,rezultat)
        if alfa>=beta:
            return alfa

    return beta


def maxScore(table,dubina,alfa,beta,igrac):
    if dubina<=0:
        return prvaFazaHeuristika(table,igrac)
    for potez in moguciPoteziFaza1(table,igrac):
        table[potez]=igrac
        rezultat = minScore(table,dubina-1,alfa,beta)
        alfa = max(alfa,rezultat)
        if alfa >= beta:
            return beta
    
    return alfa




def main():
    pass

if __name__ == '__main__':
    main()




