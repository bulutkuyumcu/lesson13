try:
    sıcaklık = int(input("Sıcaklık giriniz: "))

    assert sıcaklık < 100
    print("hava sıcaklığı: ",sıcaklık)
except AssertionError:
    print("hava sıcaklığında bir sorun olabilir.")
except:
    print("bilinmeyen bir hata oluştu")
finally:
    print("işleminiz sonlandırılmışıtır")