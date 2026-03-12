medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print("\n {} metro(s) equivale a:".format(medida))
print("   {}  quilômetros  (km)".format(km))
print("   {}  hectômetros  (hm)".format(hm))
print("   {}  decâmetros   (dam)".format(dam))
print("   {}  metros       (m)".format(medida))
print("   {}  decímetros   (dm)".format(dm))
print("   {}  centímetros  (cm)".format(cm))
print("   {}  milímetros   (mm)".format(mm))

