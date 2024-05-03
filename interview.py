
def list1(a):
    list2=[]
    p="ca"
    for x in a:
       if p in x:
        if x[0:2]==p:
            list2.append(x)
    print(list2)
a=["cat","car","fear","center"]
list1(a)