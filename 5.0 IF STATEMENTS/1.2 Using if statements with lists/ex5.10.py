current_users=["admin","Jacob","Merin","Amir","Karthi","Lori"]
new_users=["admin","Jacob","Merin","Subu","Gayu","Rishi"]
for i in new_users:
    for j in current_users:
        if i==j:
            print(i,"has already been used please enter a new user!!")
            break
        elif i.upper()==j.upper():
            print(i,"has already been used please enter a new user!!")
            break
        elif j==current_users[-1]:
            print(i,"The username is available")
            break
        else:
            continue
