wr = open("./11.14/file.txt","w")

wr.write("Halmaz (set):\n"
    "- rendezetlen (elemeknek nincs indexe)\n"
   " - egy elem csak egyszer szerepelhet\n"
    "- többféle típust tárolhat egyszerre is\n"
    "- a halmaz eleme maga nem változtatható meg\n")
wr.write("halmaz létrehozása\n")
reggeli = {'tea', 'vaj', 'piritós'}


wr.write("üres halmaz létrehozása\n"
        "ebed = {}  <- SZÓTÁRT hoz létre!!!\n")
ebed = set()
wr.write("bejárható gyűjteményből, pl. listából\n")
ebed = set(['halászlé', 'kenyér', True])
wr.write("egy elem hozzáadása\n")
reggeli.add('lekvár')

wr.write(f"{str(reggeli)}\n")
wr.write("egy nem meghatározott elem eltávolítása")
reggeli.pop()

#reggeli.remove("sajt")
wr.write("egy bizonyos elem eltávolítása\n"
    "ha nincs ilyen elem, akkor hibát eredményez\n")
reggeli.discard('sajt')


reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'víz', 'halászlé', 'kenyér'}
print(reggeli & ebed)
print(reggeli | ebed)
print(reggeli - ebed)
print(reggeli ^ ebed)
wr.write("metszet\n")
wr.write(f"{str(reggeli & ebed)}\n")
wr.write("unio\n")
wr.write(f"{str(reggeli | ebed)}\n")
wr.write("különbség\n")
wr.write(f"{str(reggeli - ebed)}\n")
wr.write("csak az egyikben, vagy csak a másikban/n")
wr.write(f"{str(reggeli ^ ebed)}\n")

wr.close()