import random



def Gen(s):
    d=round(s/2)

    if(s%2 == 0):
        d1=d
        d2=d
    else:
        d1=d
        d2=d-1

    p=random_prime(2^d1-1, False, 2^(d1-1))
    q=random_prime(2^d2-1, False, 2^(d2-1))

    while (p==q):
        p=random_prime(2^d1-1, False, 2^(d1-1))
        q=random_prime(2^d2-1, False, 2^(d2-1))

    n=p*q
    fi_n=(p-1)*(q-1)
    e = randint(2, fi_n-1)
    while gcd(fi_n, e) != 1:
        e = randint(2, fi_n-1)
    d = power_mod(e, -1, fi_n)
    return  (d,e,n)

d,e,n = Gen(64)

print("Para kluczy Podpisujacego(B):\n")
print("klucz prywatny (d,n) =","(",d,",",n,")")
print("klucz publiczny (e,n) =","(",e,",",n,")")

M=random.getrandbits(10)
print("wiadomosc", M)

k=randint(1, n)
print("Uzytkownik A wybiera losowo z przedzialu (1,n) liczbe k = ",k)

t=M*power_mod(k,e,n)%n
print("Uzytkownik A zaciemnia m obliczajac t = (m(k^e))%n = ",t)
print("Nastepnie przesyla t do uzytkownika B")

r=power_mod(t,d,n)
print("Uzytkownik B podpisuje t obliczajac r = (t^d)%n = ",r)
print("Przesyla wynik do uzytkownika A")




s=(r/k)%n
print("Uzytkownik A usuwa zaciemnienie obliczajac s = (r/k)%n =" ,s)
print("Sprawdzanie poprawnosci poprzez porownanie wartosci (s^e)%n = ",power_mod(s,e,n)," i wiadomosci M")
if(power_mod(s,e,n)==M):
    print("Zgadza sie")
else:
    print("nie zgadza sie")