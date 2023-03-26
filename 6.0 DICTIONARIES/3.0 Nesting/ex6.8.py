d1={"pet":"dog","owner":"q"}
d2={"pet":"cat","owner":"a"}
d3={"pet":"fish","owner":"z"}
l=[d1,d2,d3]
for i in l:
    a,b=i.items()
    print(a,":",b)
    