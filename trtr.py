s = 0
k = 0
o = input
while o != "стоп":
    o = input("ведите оценку Доминика!")
    k = k + 1
    if o == "стоп":
        print("годовая оценка Доминика ",k / s)
        break
    s = s + int(o)

    