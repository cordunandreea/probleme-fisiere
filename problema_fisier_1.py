with open('numere.txt','r') as f:
    a=f.readline()
    b=f.readline()
with open('minim.txt','w') as f:
    if int(a)>int(b):
        f.write(b)
    if int(b)>int(a):
        f.write(a)