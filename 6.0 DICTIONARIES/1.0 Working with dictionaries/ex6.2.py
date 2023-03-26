d={"1stname":"Sripriya","2ndname":"Sundaresan","age":39,"city":"Chennai"}
for i in d:
    print(i,":",d.get(i))
 
ask=input("Enter the first name to be changed:")
shi=input("Enter the age to be changed:")
d["1stname"]=ask
d["age"]=shi
for i in d:
    print(i,":",d.get(i))
