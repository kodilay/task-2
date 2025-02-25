def calculator(sayi1, sayi2, islem):
    if islem == '+':
        print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
    elif islem == '-':
        print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
    elif islem == '*':
        print(f"{sayi1} * {sayi2} = {sayi1 * sayi2}")
    elif islem == '/':
        if sayi2 == 0:
            print("Bölme işlemi için ikinci sayı 0 olamaz!")
        else:
            print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")
    else:
        print("Geçersiz işlem yapıldı lütfen geçerli işlem girin!")


calculator(7, 3, '+')  
calculator(50, 2, '/') 
calculator(913, 0, '/')   
calculator(100, 5, '%')   
