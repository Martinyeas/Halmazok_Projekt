#1
halmaz1 = {'egy', 'kettő', 'három'}
halmaz1.clear()

#2
halmaz2 = {"négy","öt","hat"}
halmaz3 = halmaz2.copy()
print(halmaz3)

#3
halmaz4 = {"hét","nyolc","kilenc"}
halmaz5 = {"tíz","tizenegy","tizenkettő"}
halmaz4.difference(halmaz5)
print(halmaz4)

#4
halmaz6 = {"tizenhárom","tizennégy","tizenőt"}
halmaz7 = {"16","17","18"}
halmaz6.update(halmaz7)
print(halmaz6)

#5
halmaz8 = {"19","20","21"}
halmaz9 = {"22","23","24"}
halmaz8.intersection(halmaz9)
print(halmaz8)

#6
halmaz10 = {"25","26","27"}
halmaz11 = {"28","29","30"}
halmaz10.intersection_update(halmaz11)
print(halmaz10)

#7
halmaz12 = {"31","32","33"}
halmaz13 = {"34","35","36"}
print(halmaz12.isdisjoint(halmaz13))

#8
halmaz14 = {"37","38","39"}
halmaz15 = {"40","41","42"}
print(halmaz14.issubset(halmaz15)," Benen van-e ez a halmaz egy másikba?")

#9
halmaz16 = {"43","44","45"}
halmaz17 = {"46","47","48"}
print(halmaz16.issuperset(halmaz17)," Benen van-e egy másik halmaz ebben?")

#10
halmaz18 = {"49","50","51"}
halmaz19 = {"52","53","54"}
print(halmaz18.symmetric_difference(halmaz19)," Visszadob egy halmazt egy szimmetrikus különbséggel.")

#11
halmaz20 = {"55","56","57"}
halmaz21 = {"58","59","60"}
print(halmaz20.pop())
print(halmaz21.add("61"))
print(halmaz20.union(halmaz21))