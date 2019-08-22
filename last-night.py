#my atm machine code in python practice
print("**************************")
pin=int(input("enter your secret code here:"))
if pin ==0000:
    print("** Welcome To Obed Bank PLC**")
    print("1. withdraw")
    print("2. Transfer")
    print("3. Change Pin")
    print("4. Pay Bills")
    print("5. dBuy Airtime")
    print("6. Others ")
    choice =int("enter choice")
    if choice== 1:
         print("1.Savings")
         print("2.current")
         pr= int(input("please choose your account type :"))
         if pr ==1:
             cash= int(input("Enter cash amount to be withdrawn"))
         elif pr==2:
             cash = int(input("Enter cash to be withdrawn"))
     
    elif choice ==2:
         name =input("enter receiver's name:")
         acc = int(input("enter account number: "))
         if acc ==12345 and name =="oluwabunmi":
             result= (input("input the receiver's contact"))
         elif :
         print("please enter correct account details")h
    elif choice==3:
         newPin=int(input("please enter old pin"))
         if newPin = 8888:
             newPin=(input("your pin has been successfully changed"))
         elif
         print("new number is not valid")
else:
    print("your code aint valid")
    

