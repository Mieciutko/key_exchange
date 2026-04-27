# Generacja parametrow dziedziny
# wejscie:
#     b - dlugosc charakterystyki ciala p wyrazona w bitach
# wyjscie:
#     p - charakterystyka ciala Fp postaci p = 2n+1
#     g - generator podgrupy cyklicznej w grupie F*p rzedu n
#     n - rzad podgrupy cyklicznej

import random

b=64;

def generacja_parametrow(b):
    flag=1;
    while (flag==1):
        p = random_prime(pow(2,b));
        n = int((p-1)/2);
        if (p > pow(2,b-1)) and (is_prime(n) == True):
            flag = 0;
    F = GF(p)

    flag=1;
    while (flag==1):
        g = F.random_element()
        rg=g.multiplicative_order()
        if (rg==n):  #sprawdzenie czy element g jest generatorem
            flag=0;
            return p,n,g

p,n,g=generacja_parametrow(b)

# Generacja pary kluczy prywatny/publiczny
# wejscie:
#     p - charakterystyka ciala Fp
#     n - rzad podgrupy cyklicznej
#     g - generator podgrupy cyklicznej rzedu n
# wyjscie:
#     kpriv - klucz prywatny bedacy losowa liczba calkowita z przedzialu <1, n-1>
#     kpub - klucz publiczny spelniajacy kpub = g^kpriv (mod p)

def generacja_kluczy(p, n, g):
    kpriv = random.randint(1, n-1)
    kpub = pow(g,kpriv,p)
    return kpriv, kpub


# "3. Realizacja protokolu:"
kprivA, kpubA = generacja_kluczy(p, n, g)
# "        strona A generuje swoje klucze:"
# "                kpubA  =",kpubA;
# "                kprivB  =",kprivA;

kprivB, kpubB = generacja_kluczy(p, n, g)
# "        strona B generuje swoje klucze:"
# "                kpubB  =",kpubB;
# "                kprivB  =",kprivB;

sekretA = pow(kpubB, kprivA, p)
# "        strona A oblicza A = kpubB^kprivA mod p"
# "            tajna liczba strony A: ", sekretA

sekretB = pow(kpubA, kprivB, p)
# "        strona B oblicza B = kpubA^kprivB mod p"
# "            tajna liczba strony B: ", sekretB

# "\n"
# "4.Sprawdzenie poprawnosci"
# "        Porownanie sekretow obu stron - powinny byc identyczne "
# "\n"
print ("{}={}".format(sekretA,sekretB))
if (sekretA == sekretB):
    print ("OK")
else:
    print ("nie zgadza sie")