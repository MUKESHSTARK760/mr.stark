#f=open("bank.txt","x")
#f=open("bank.txt","w")
#f=open("bank.txt","a")
f.write("/n")
def deposit():
    balance=balance+amount
    print("your balance is",balance)
def withdrawl():
    balance=balance-amount
    print(balance)
balance=9000
choice=input("enter your choice:")
print("a.deposite")
print("b.withdrawl")
print("c.check balance")
if choice=="a":
    print(deposite())
elif choice=="b":
    print("withdrawl")
elif choice=="c":
    print("balance")
else:
    print("thankyou visit again our bank")