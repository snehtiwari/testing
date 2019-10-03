n = input()
count1=0
count2=0
for i in n:
    if i.isdigit():
        count1=count1+1
    else:
        count2=count2+1
print("numbers:",count1)
print("alphabets",count2)
