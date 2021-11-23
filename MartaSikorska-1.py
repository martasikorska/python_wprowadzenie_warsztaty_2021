#Zad. 1 (2p)
#Zmienna A ma wartość 5. Zmienna B ma wartość 10. Zrób tak, aby wartość  zmiennej A była równa wartości zmiennej B (10),
# a wartość zmiennej B była równa wartości zmiennej A(5).

A = 5
B = 10

A1 = A
A = B
B = A1

print(A)
print(B)

#Zad. 2 (4p)
#Napisz program, który ma pomóc osobie używającej systemu imperialnego (lbs, ft) uzyskać podstawowe dane
# o jej wadze i wzroście w systemie metrycznym(kg,m) oraz jej BMI. Na początku użytkownik (metodą input())
# podaje swoje imię, wagę w funtach (lbs) oraz wzrost w stopach (ft). Wynikiem działania programu ma być
# spersonalizowana wiadomość dla użytkownika (metoda f-string), witająca go po imieniu i informująca go
# o jego wzroście w m, wadze w kg oraz jego wskaźniku BMI. Dodatkowo, te cztery podstawowe informacje mają być
# zapisane w liście w osobnych komórkach -  imię jako string, wzrost, waga i BMI jako float.

#Potrzebne wzory:
#1 lbs = ok. 0,453 kg
#1 ft = 0,3048 m
#BMI = waga(w kg)/wzrost2(w m)

print("Proszę podaj swoje imię: ")
imie = input( );
a = float(input("Proszę podać swoją wagę (lbs) : "))
b = float(input("Proszę podać swój wzrost (ft): "))

lbs = 0.453
ft = 0.3048

wzrost = b * ft
waga = a * lbs

wzrost2 = wzrost * wzrost

BMI = waga // wzrost2

zdanie = f" Witaj {imie} ! Twój wzrost to {wzrost} m, Twoja waga to {waga} kg, Twój wskaźnik BMI wynosi {BMI} "
print(zdanie)

lista = [imie, wzrost, waga, BMI]
print(lista)

#Zad. 3 (4p)
#Proszę zadeklarować zmienne, w których użytkownik (metoda input()) poda swoje imię, nazwisko, wiek, wypisane
# po przecinku znana mu języki programowania (to znaczy takie, z którymi miał styczność) oraz języki obce,
# które zna w stopniu biegłym, również po przecinku. Każda zmienna ma być zadeklarowana osobno. Program ma
# printować string, w którym będą owe zmienne, zawarte w zdaniu (np. Nazywam się [imię i nazwisko])
# Na końcu program ma wyświetlić, ile języków programowania zna użytkownik, a także ile zna języków obcych

#Podpowiedź: co do ostatniego polecenia - nie bez powodu podane było wcześniej "po przecinku"

imie = input("Podaj imie : ")
nazwisko = input("Podaj nazwisko : ")
wiek = int(input("Podaj wiek : "))
progr = input("Podaj znane Ci języki programowania (po przecinku) : ")
obc = input("Podaj znane Ci języki obce (po przecinku) : ")

progr = progr.split(',')
obc = obc.split(',')

print(f"Nazywam się {imie} {nazwisko}. Mam {wiek} lat. Znam {len(progr)} języków programowania oraz {len(obc)} języków obcych.")
