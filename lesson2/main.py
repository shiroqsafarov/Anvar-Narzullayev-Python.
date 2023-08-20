import math


# matnni konsolga chiqarish
print("\"Nexia\", \"Tico\", 'Damas' ko'rganlar qilar havas.")

# 5 ning 4 chi darajasini topish
print(5**4)

# 22 ni 4 ga bo'lgandagi qoldiqni topish
print(22 % 4)

# Tomoni 125 ga teng bo'lgan kvadratni yuzasini topish
print(125 * 125)

# Tomoni 125 ga teng bo'lgan kvadratni perenetrini topish
print(125 * 4)

# Doirani yuzasini topish
diametr = 10
radius = diametr / 2  # radiusni topish uchun diametrni 2 ga bo'lamiz
PI = 3.14
S = PI  * radius ** 2
print(f"Doiraning yuzasi: {S} ga teng.")

# Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning).
a = 6
b = 7
c = a ** 2 + b ** 2 # katetlari kvadratlari yig'indisi gipotenuza kvadratiga teng.
print(math.sqrt(c))

