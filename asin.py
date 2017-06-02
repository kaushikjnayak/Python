from math import asin,sqrt, pi
AB = int(input())
BC = int(input())
degree_sign= u'\N{DEGREE SIGN}'
print (  str(round(180/pi * asin ( ( sqrt( AB ** 2 + BC ** 2 )) / ( 2 * BC) ))) + degree_sign)


