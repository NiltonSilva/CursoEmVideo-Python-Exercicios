import math
catOp = float(input('Qual a medida do cateto oposto: '))
catAd = float(input('Qual a medida do cateto adjacente: '))
# hip = math.pow(catOp, 2) + math.pow(catAd, 2)
hip = math.hypot(catOp, catAd)
print('A hipotenusa sera {:.2f}'.format(math.sqrt(hip)))

