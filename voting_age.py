def start():
    age = int(input("Enter your age\n")) #\n is used to change line before printing another line 
    name = input("Enter your name")
    print(f"\n {name} {vote_ornot(age)} vote.")

def vote_ornot(age):
    if age>=18:
        return "Can"
    elif age<=18:
        return "can not"
start()
    