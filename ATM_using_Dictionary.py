
#######   ********************** ATM machine
#pin : balance
from datetime import datetime
now=datetime.now()

Dict_atm={1234:8800,4567:9500,7892:7300,7418:5000,1478:3000,6985:1200,9874:7500,9632:7000,6565:4500,2021:6000} # Large data can be in Dictionary , Perfectly Run 

#print(Dict_atm['4567'])
print(75*"=")
print("\nWELCOME TO CODERS BANK OF INDIA")
print(75*"=")
print("\n")
print(" Withdraw Cash       :   A")
print(" Balance Enquiry     :   B")
print(" Pin Change          :   C")
print(" Other Banking       :   D\n")
user_op=input("Choose Option A|B|C|D : ")

if user_op.casefold()=='a':
    user_pin=int(input("Please Enter your Pin - "))
    # amt=int(input("Enter Amount : "))
    if user_pin in Dict_atm.keys():
        var= Dict_atm.get(user_pin)
        amt=int(input("Enter Amount : "))
        bal=var-amt     
        Dict_atm['user_pin']=bal
        print("Last Transaction Completed ! \nAvailable Balance : ",Dict_atm['user_pin'])
        print("\n")
    else:
        print("You have entered a Wrong Pin")
        print("\n")

elif user_op.casefold()=='b':
    user_pin=int(input("Please Enter your Pin to get Mini Satement- "))
    print("Available Balance : ",Dict_atm.get(user_pin,"Not showing, You have entered a Wrong Pin"))
    print("Last Transaction is at - ",now.strftime(" %H:%M:%S "))
    print("\n")

elif user_op.casefold()=='c':
    user_pin=int(input("Please Enter your old Pin - "))
    user_newpin=int(input("Enter New pin Here: "))
    old_bal=Dict_atm.get(user_pin)
    Dict_atm.pop(user_pin)
    Dict_atm[user_newpin]=old_bal
    #Dict_atm.update(user_newpin=old_bal)
    
    #Dict_atm['user_pin']=user_newpin   // value change in this
    print("\nYour Pin has been Updated Succesfully.\n")
    #print("Updated pin is - ",Dict_atm[user_newpin])
    # print(Dict_atm,"\n")

    #----------------------   OPTION D STARTS -------------------------------#
	 #----------------------   INDIDE 'D' TWO SUB OPTION-------------------------------#
elif user_op.casefold()=='d':
    print("\tOTHER BANKING\n")
    print("\n **** PLEASE SELECT AN OPTION ****")
    print("\n Deposit Cash - PRESS 1")
    print(" Accounts - PRESS 2\n")
    user_ob_op=input("Choose Option 1/2 - ")

    if user_ob_op=='1':
        user_pin=int(input("Please Enter your Pin - "))
        if user_pin in Dict_atm.keys():
            var= Dict_atm.get(user_pin)
            amt=int(input("Enter Amount to deposit: "))
            print("Please put cash and press proceed ")
            bal=var+amt     
            Dict_atm['user_pin']=bal
            print("Last Transaction Completed ! \nAvailable Balance : ",Dict_atm['user_pin'])
            print("Take the Transaction Receipt ")
            print("\n")
        else:
            print("Wrong pass")
            print("\n")

    elif user_ob_op=='2':
        user_ip=input("\nTo get Account Details Please Enter your password - \n")
        if user_ip=='1234':
            print("PLease wait , while your request is being processed ....\n")
            listrehan=['Rehan Mondal','A/C No.:542019241256','Bank- SBI','Branch-Mahamayatala','Branch code:101634']
                                # print(listrehan,end=" - ")
            for i in listrehan:
                print(i)
            print("\n")


        elif user_ip=='4567':
            print("PLease wait , while your request is being processed ....\n")
            listnishat=['Nishat Mallick','A/C No.:956519241256','SBI','Branch-Mahamayatala','Branch code:101634']
            for i in listnishat:
                print(i)
            print("\n")

        elif user_ip=='7892':
            print("PLease wait , while your request is being processed ....\n")
            listchiki=['Ishrat Tasneem','A/C No.:1005319241256','HDFC','Branch-Brahmapur','Branch code:HDFC634']
            for i in listchiki:
                print(i)
            print("\n")
else:
    print("You have not Choose any correct option \n")


