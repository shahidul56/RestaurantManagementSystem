# NAME: Suka Cafe & Catering
# DEVELOPER: NyanSniper101

import os 

# MAKING STORAGE FILES  #
f = open("bfmaorder.txt", "w+") #breakfast storage
f.write("")
f.close()

f = open("lunchorder.txt", "w+") #lunch storage
f.write("")
f.close()

f = open("extraserv.txt", "w+") #extras storage
f.write("")
f.close()

# # # # # # # # # # # # #

print(50 * "%")
print("")
print ("SUKA CAFE & CATERING".center(50))
print("")
print(50 * "%")
print ("")

## ORDER MENU DECLERATION ##
ratecounter = 0 # For storing total rate of items
ordername = " " # For storing names of selected items
breakfast=False
lunch=False
extras=False

## ORDER MODULE CODE ##

def goto(linenum):
    global line
    line = linenum

line = 1
while True:
    if line == 1:
      print("B - Order Breakfast")
      print("L - Order Lunch")
      print("E - Extra Services")
      menuaccess = input("\nMake a Selection >> ")
      if menuaccess == "B":
        goto(2)
      elif menuaccess == "L":
        goto(3)
      elif menuaccess == "E":
        goto(4)
      else:
        goto(100)
   
    elif line == 2:
      if menuaccess == "B":
        breakfast=True
        print("\n" + 50 * "*")
        print("BREAKFAST MENU".center(50))
        print(50 * "*")
        print(" ")
      
        partyselect = input("Book A Party? [Y]/[N] >> ")
        while(partyselect!="Y" and partyselect!="N"):
          print("Invalid Character!")
          partyselect = input("Book A Party? [Y]/[N] ")
        print(" ")
        if partyselect == "Y":
          partynumber = int(input("No Of Guests >> "))
        
        print(" ")
        print("1. Nasi Lemak   	RM20")
        print("2. Fried Noodles	RM20")
        print("3. Roti Chanai  	RM20")
        print("4. Pasta        	RM20")
        print("5. Hot Drink    	RM20")
        print("Press any other number to confirm your order")
        
        bfma=int(input("\nSelect an Item Number >> "))
        
        if partyselect == "N":
            sessionrate = 20
        elif partyselect == "Y":
            if partynumber < 10:
            	sessionrate = 20
            elif partynumber >=10 and partynumber <=25:
                sessionrate = 20 - (20*5/100)
            elif partynumber >=26 and partynumber <=50:
                sessionrate = 20 - 20*10/100
            elif partynumber >=51 and partynumber <=100:
                sessionrate = 20 - 20*15/100
            elif partynumber >100:
                sessionrate = 20 - 20*20/100
               
        stringsession = str(sessionrate)
        while(bfma>0 and bfma<6):
          ratecounter += sessionrate
          if bfma == 1:
            ordername = ordername + " | " + "Nasi lemak"
            f = open("bfmaorder.txt","a+")
            f.write("Nasi lemak   \t")
            f.write(stringsession)
            f.write("\n")
            f.close()
          elif bfma == 2:
            ordername = ordername + " | " + "Fried Noodles"
            f = open("bfmaorder.txt","a+")
            f.write("Fried Noodles\t")
            f.write(stringsession)
            f.write("\n")
            f.close()
          elif bfma == 3:
            ordername = ordername + " | " + "Roti Chanai"
            f = open("bfmaorder.txt","a+")
            f.write("Roti Chanai  \t")
            f.write(stringsession)
            f.write("\n")
            f.close()
          elif bfma == 4:
            ordername = ordername + " | " + "Pasta"
            f = open("bfmaorder.txt","a+")
            f.write("Pasta        \t")
            f.write(stringsession)
            f.write("\n")
            f.close()
          elif bfma == 5:
            ordername = ordername + " | " + "Hot Drink"
            f = open("bfmaorder.txt","a+")
            f.write("Hot Drink    \t")
            f.write(stringsession)
            f.write("\n")
            f.close()
          bfma=int(input("Next Item? >> "))

        if (bfma > 5):
            print("INVALID ITEM NUMBER")
            print ("\nSelected Items have been Ordered")
            print("Total Price: ", ratecounter)
            print("Items Selected >" + ordername )
      EndReply=input("\nPress [M] to Return to Main Menu or \nPress [P] to Proceed to Payment Menu >> ")
      while(EndReply!="P" and EndReply!="M"):
      	 EndReply = input("Invalid Input! Try again >>")
      if EndReply=="P":
        goto(20)
      elif EndReply=="M":
        print (" ")
        print(50 * "*" + "\n")
        goto(1)

    elif line == 3:
      if menuaccess == "L":
        lunch=True
        print("\n" + 50 * "*")
        print("LUNCH MENU".center(50))
        print(50 * "*")
        print(" ")
    
        partyselect = input("Book A Party? [Y]/[N] >> ")
        print(" ")
        if partyselect == "Y":
            partynumber = int(input("No Of Guests >> "))
            print(" ")
        
        print("1. Chicken Chop 	RM30")
        print("2. Steamed Fish 	RM30")
        print("3. Salad        	RM30")
        print("4. Fried Rice   	RM30")
        print("5. Soft Drink   	RM30")
        print("Press any other number to confirm your order")
    
        lunchmenuaccess = int(input("\nSelect an Item Number >> "))
    
        if partyselect == "N":
        	sessionrate = 30
        elif partyselect == "Y":
          sessionrate = 30
          if partynumber >10 and partynumber <25:
              sessionrate = 30 - 30*5/100
          if partynumber >26 and partynumber <50:
              sessionrate = 30 - 30*10/100
          if partynumber >51 and partynumber <100:
              sessionrate = 30 - 30*15/100
          if partynumber >100:
              sessionrate = 30 - 30*20/100
                    
        stringsession = str(sessionrate)
        while(lunchmenuaccess>0 and lunchmenuaccess<6):
          ratecounter += sessionrate
          if lunchmenuaccess == 1:
            ordername = ordername + " | " + "Chicken Chop"
            f = open("lunchorder.txt", "a+")
            f.write("Chicken Chop \t")
            f.write(stringsession)
            f.write("\n")
            f.close()
          elif lunchmenuaccess == 2:
            ordername = ordername + " | " + "Steamed Fish"
            f = open("lunchorder.txt", "a+")
            f.write("Steamed Fish \t")
            f.write(stringsession)
            f.write("\n")
            f.close()
          elif lunchmenuaccess == 3:
            ordername = ordername + " | " + "Salad"
            f = open("lunchorder.txt", "a+")
            f.write("Salad   \t")
            f.write(stringsession)
            f.write("\n")
            f.close()
          elif lunchmenuaccess == 4:
            ordername = ordername + " | " + "Fried Rice"
            f = open("lunchorder.txt", "a+")
            f.write("Fried Rice   \t")
            f.write(stringsession)
            f.write("\n")
            f.close()
          elif lunchmenuaccess == 5:
            ordername = ordername + " | " + "Soft Drink"
            f = open("lunchorder.txt", "a+")
            f.write("Soft Drink   \t")
            f.write(stringsession)
            f.write("\n")
            f.close()
          lunchmenuaccess=int(input("Next Item? >> "))

        if (lunchmenuaccess > 5):
          print("INVALID ITEM NUMBER")
          print ("\nSelected Items have been Ordered")
          print("Total Price: ", ratecounter)
          print("Items Selected >" + ordername )
      EndReply=input("\nPress [M] to Return to Main Menu or \nPress [P] to Proceed to Payment Menu >> ")
      while(EndReply!="P" and EndReply!="M"):
      	 EndReply = input("Invalid Input! Try again >>")
      if EndReply=="P":
        goto(20)
      elif EndReply=="M":
        print (" ")
        print(50 * "*" + "\n")
        goto(1)

    elif line == 4:
      if menuaccess == "E":
        partyselect = "Y"
        extras=True
        print("\n" + 50 * "*")
        print("EXTRAS MENU".center(50))
        print(50 * "*")
        
        print(" ")
        print("1. Chairs       	RM2")
        print("2. Chair Sashes 	RM5")
        print("3. Tables       	RM35")
        print("4. Table cloths 	RM25")
        print("Press any other number to confirm your order")
        
        extramenuaccess = int(input("\nSelect An Item[1],[2],[3],[4] >> "))
        extrarate = 0
        while(extramenuaccess>0 and extramenuaccess<5):
          extramenuunits = int(input("Enter Number Of Units >>"))
          if extramenuaccess == 1:
            print("Chairs Ordered")
            extrarate = 2 * extramenuunits
            ratecounter += extrarate
            ordername = ordername + " | " + "Chairs"
            f = open("extraserv.txt", "a+")
            f.write("Chairs       \t")
            f.write(str(extrarate))
            f.write("\n")
            f.close()
          elif extramenuaccess == 2:
            print("Chair Sashes Ordered")
            extrarate = 5 * extramenuunits
            ratecounter += extrarate
            ordername = ordername + " | " + "Chair Sashes"
            f = open("extraserv.txt", "a+")
            f.write("Chair Sashes \t")
            f.write(str(extrarate))
            f.write("\n")
            f.close()
          elif extramenuaccess == 3:
            print("Tables Ordered")
            extrarate = 35 * extramenuunits
            ratecounter += extrarate
            ordername = ordername + " | " + "Tables"
            f = open("extraserv.txt", "a+")
            f.write("Tables       \t")
            f.write(str(extrarate))
            f.write("\n")
            f.close()
          elif extramenuaccess == 4:
            print("Table cloths Ordered")
            extrarate = 25 * extramenuunits
            ratecounter += extrarate
            ordername = ordername + " | " + "Table Cloth"
            f = open("extraserv.txt", "a+")
            f.write("Table Cloth  \t")
            f.write(str(extrarate))
            f.write("\n")
            f.close()
          extramenuaccess = int(input("\nNext Item[1],[2],[3],[4] >> "))
    
        print("INVALID ITEM NUMBER")
        print ("\nSelected Items have been Ordered")
            
        print("\nTotal Price: ", ratecounter)
        print("Items Selected: ", ordername)
      EndReply=input("\nPress [M] to Return to Main Menu or \nPress [P] to Proceed to Payment Menu >> ")
      while(EndReply!="P" and EndReply!="M"):
      	EndReply = input("Invalid Input! Try again >>")
      if EndReply=="P":
        goto(20)
      elif EndReply=="M":
        print (" ")
        print(50 * "*" + "\n")
        goto(1)

    elif line == 20:
        break
    elif line == 100:
        print ("Invalid Input!!!\n")
        goto(1)


print("\n")

# PAYMENT MENU#

print(50 * "*")
print("PAYMENT MENU".center(50))
print(50 * "*")
print(" ")

# TOTAL PAYABLE #
print("All Selected Items: ", ordername)
print("Total Due: RM", ratecounter)

print(" ")

amountpaid = int(input("Enter the Amount Paid >> "))
print("\n")

# REPORT MENU #

print(50 * "*")
print("REPORT MENU".center(50))
print(50 * "*")
print(" ")

# BREAKFAST PRINTING #
if breakfast==True:
    print(30 * "=")
    print("Breakfast Order")
    print(30 * "=")
    
    f = open("bfmaorder.txt", "r")
    for line in f:
        print (line)
    f.close()
    print(30 * "-")
    print("\n")

# LUNCH PRINTING #
if lunch==True:
    print(30 * "=")
    print("Lunch Order")
    print(30 * "=")
    
    f = open("lunchorder.txt", "r")
    for line in f:
        print (line)
    f.close()
    print(30 * "-")
    print("\n")
    
# EXTRAS PRINTING #
if extras==True:
    print(30 * "=")
    print("Extras Services Order")
    print(30 * "=")
    
    f = open("extraserv.txt", "r")
    for line in f:
    	print(line)
    f.close()
    print(30 * "-")
    print("\n")

# END OF PRINTINGS #

dueamount = ratecounter - amountpaid
print("Total Due: RM", ratecounter)
print("Amount Paid: RM", amountpaid)

if (partyselect == "Y" and (breakfast==True or lunch==True)) :
  print("Discount: RM", sessionrate)
  if dueamount>0:
    print("Customer Paid: RM",dueamount)
  elif dueamount<0:
    print("Amount Returned to Customer: RM",-1*dueamount,"to customer")
else:
  if dueamount>0:
    print("Customer Paid: RM", dueamount)
  elif dueamount<0:
    print("Amount Returned to Customer: RM", -1*dueamount, "to customer")

print("Thanks for Visiting! Please Come Again! :-)")

###############     END OF PROGRAM    ###############   