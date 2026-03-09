#guest code
'''a="likhith"
b=input("enter the name:")
if a==b:
    print("welcome likhith")
else:
    print("welcome guest")'''


#for multiple users
b=["likhith","mani","ram","yaseer","siva"]
names=input("enter the name:")
if names in b:
    print("welcome ", names)
else:
    print("welcome guest")
