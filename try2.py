try:
    sayi1 = float(input("birinci sayıyı giriniz:"))
    sayi2 = float(input("ikinci sayıyı giriniz:"))

    sonuc = sayi1/sayi2
    print("işlem sonucunuz: ",sonuc)
except ZeroDivisionError:
    print("sıfıra bölüm yapılamaz")
except ValueError:
    print("yanlış tipte veri girdiniz")
except:
    print("bilinmeyen bir hata oluştu")