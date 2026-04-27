import hashlib
import hmac
import binascii
import random

K="1234567890ABCDEF"

def HMACprotocol(K):
    print("-----------1.ZALOZENIA:----------- \n")
    d = hashlib.sha256()
    print("Wspolny klucz stron A i B: ",K)
    Khex=binascii.unhexlify(K)
    print("Wartosc klucza w hexstr :",Khex)
    A=random.getrandbits(64)
    B=random.getrandbits(64)
    print("Identyfikator A: ",A)
    print("Identyfikator B: ",B)
    #unikalne identyfikatory stron
    print("\n")


    print("-----------2.KROKI PROTOKOLU:----------- \n")
    print("---2.1 Strona A wybiera liczbe losowa RandA i wysyla ja stronie B---")
    RandA=random.getrandbits(64)
    print("Losowa liczba A: ",RandA)
    print("\n")
    #losowe liczby  wybierane przez strony

    print("---2.2 Strona B oblicza swoja liczba losowa RandB i wysyla do strony A wraz z wynikiem HMACB(RandA||RandB||B)---")
    RandB=random.getrandbits(64)
    print("Losowa liczba B: ",RandB)
    msg=(RandA^RandB^B)

    HMACB= hmac.new(Khex,str(msg).encode(),hashlib.sha256)
    HMACBhex = HMACB.hexdigest()
    print("Wartosc HMACB:", HMACBhex)
    print("\n")

    print("---2.3 Strona A oblicza HMACA(RandA||RandB||B) wykorzystujac przeslany identyfikator strony B")
    HMACA=hmac.new(Khex,str(msg).encode(),hashlib.sha256)
    HMACAhex = HMACA.hexdigest()
    print("Porownuje swoj wynik: ", HMACAhex  ,  " z przeslanym przez strone B:")
    if(HMACBhex==HMACAhex):
        print("zgadza sie - strona A ma pewnosc ze komunikuje sie ze strona B")
    else:
        print("nie zgadza sie, strona A przerywa protokol")


    msg2=(RandB^A)
    HA=hmac.new(Khex,str(msg2).encode(),hashlib.sha256)

    #Jesli jak w pdf ma byc tylko skrot w tym miejscu - tylko wtedy sie nie zgadza
    #d.update(str(msg2).encode())
    #HAhex = d.hexdigest()

    HAhex=HA.hexdigest()
    print("Nastepnie strona A wysyla do strony B wartosc HA(RandB||A)",HAhex)
    print("\n")
    #strona A sprawdza czy komunikuje sie z B


    msg3=(RandB^A)
    HB=hmac.new(Khex,str(msg3).encode(),hashlib.sha256)
    HBhex = HB.hexdigest()
    print("---2.4 Strona B oblicza HB(RandB||A) = " ,HBhex, " i porownuje wynik z tym przeslanym przez A: \n")
    if(HAhex==HBhex):
        print("zgadza sie - strona B ma pewnosc ze komunikuje sie ze strona A")
    else:
        print("nie zgadza sie, strona B przerywa protokol")
    #strona B sprawdza czy komunikuje sie z A


HMACprotocol(K)