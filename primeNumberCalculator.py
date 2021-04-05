sayi1 = 0
sayi2 = int(input("Bir sayı giriniz: "))

if sayi2>1:

    for i in range(2,sayi2):
        if(sayi2 % i)==0:
            print(sayi2,"asal bir sayı değildir.")
            break
    else:
        print(sayi2,"asal bir sayıdır.")
else:
    print(sayi2,"asal bir sayı değildir.")


print(sayi2,"sayısının içindeki asal sayılar: ")
for sayi in range(sayi1, sayi2):
    if sayi > 1:
        for j in range(2, sayi):
            if (sayi % j) == 0:
                break
        else:
            print(sayi)
