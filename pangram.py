w=[]
z=[]
n=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
x=list(input("enter:"))
for i in x:
    z.append(i)
    print(z)
for j in z:
    if j not in w and j!=" ":
        w.append(j)
        print(w)
if w==n:
    print("pangram")
else:
    print("not")
