medida = float(input('Uma distância em metros: '))  # lê uma medida em metros
km = medida / 1000  # converte metros para quilômetros
hm = medida / 100  # converte metros para hectômetros
dam = medida / 10  # converte metros para decâmetros
dm = medida * 10  # converte metros para decímetros
cm = medida * 100  # converte metros para centímetros
mm = medida * 1000  # converte metros para milímetros
print("\n {} metro(s) equivale a:".format(medida))  # mostra a medida original
print("   {}  quilômetros  (km)".format(km))  # mostra a conversão para km
print("   {}  hectômetros  (hm)".format(hm))  # mostra a conversão para hm
print("   {}  decâmetros   (dam)".format(dam))  # mostra a conversão para dam
print("   {}  metros       (m)".format(medida))  # mostra o valor original em metros
print("   {}  decímetros   (dm)".format(dm))  # mostra a conversão para dm
print("   {}  centímetros  (cm)".format(cm))  # mostra a conversão para cm
print("   {}  milímetros   (mm)".format(mm))  # mostra a conversão para mm