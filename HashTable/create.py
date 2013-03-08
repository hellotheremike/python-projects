from collection import animal, HashTable
a = animal("Max", "dog")
hs = HashTable()
hs.add("8759358962", a)
hs.add("8808789852", 123)
hs.add("8909233598", "String data")
hs.add("9101082575", [1,2,3,4])

hs.add("qweqwe", "Denna kommer kollidera")


print hs.get("8759358962")
print hs.get("8808789852")
print hs.get("8909233598")
print hs.get("9101082575")
print hs.get("qweqwe")
