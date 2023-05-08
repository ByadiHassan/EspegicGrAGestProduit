d={'nom':'MEHREZ','prenom':'Karim','CIN':'X4012222'}
d['Tel']='06651045'
d['Tel']='07651045'
print(d)
d.update({'Adresse':'Khemisset'})
'''
for key in d.keys():
    print(key)
for value in d.values():
    print(value)

for item in d.items():
    print(item)
'''
for key in d.keys():
    print(key + ' '*(15-len(key)),end=' ')
print()
for key in d.keys():
    print (d[key]+' '*(15-len(d[key])),end=' ')
print()
s={10,11,12,13}
print (type(s))
s.add(10)
s[0]=15
print(s)

