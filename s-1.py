def asalsayi_mi(sayi):
    if sayi < 2:
        print(f'{sayi} bu sayı bir asal sayı değildir.')
    elif sayi == 2:
        print(f'{sayi} bu sayı bir asal sayıdır.')
    else:
        for i in range(2, sayi):
            if (sayi % i == 0):
                print(f'{sayi} bu sayı bir asal sayı değildir.')
                break
            else:
                print(f'{sayi} bu sayı bir asal sayıdır.')
                break
asalsayi_mi(19)
asalsayi_mi(24)    
asalsayi_mi(2) 
