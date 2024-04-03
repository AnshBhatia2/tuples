#creating tuples (packing)
address = (7465, "Rosewood dr", "Addison", "AL", 35540)

print(address)
print(address[0], address[1], address[2], address[3], address[4])

#applying for loop on tuple
for i in address:
    print(i,end = " ")

#unpacking
housenumber,street,city,state,zipcode = address
print(housenumber,street,city,state,zipcode)
