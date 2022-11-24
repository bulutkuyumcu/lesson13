try:
    ders_notu = int(input("not giriniz: "))

    if ders_notu > 100:
        raise OverflowError("ders notu 100'den büyük olamaz")
    print("ders notunuz:",ders_notu)
except OverflowError:
    print("Sayısal bir hata oluştu")
except:
    print("bilinmeyen bir hata oluştu")
finally:
    print("İşleminiz sonlandırılmıştır.")