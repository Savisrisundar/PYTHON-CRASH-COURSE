guest=input("Enter ur guests:").split(",")
for i in guest:
    print(i,", we are glad to invite u for the dinner fest we r planning to arrange...")
    
print(guest[1],"can't show up for the dinner!!:(")

guest[1]="Loki"
for i in guest:
    print(i,", we are glad to invite u for the dinner fest we r planning to arrange...")
