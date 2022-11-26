 #inputting all the contacts

contacts= {
"Senim": 9628830855,
"Sagar": 6203076729,
"Ayush": 9718306944,
"Himanshu": 7889246865,
"Vinod": 84288723052
}

#Searches the dictionary and prints the key value pair incase the key isn't present, it adds it to the dict and prints it''

def single_search():
	name=input(">>>Enter the name of the contact you wish to search for: ").upper()
	if name in contacts:
		print(f"\n{name}: {contacts[name]}")
	else:
	   b=input("\nNo such contact found😑\nIf you wish to add one, type 'Yes' else type 'No': ").lower()
	   if b=="yes":
	     new_contact(name)
	     print(f"{name}: {contacts[name]}")
	   elif b=="no":
	     	pass
	   else:
	     print("Enter either yes or no nigga")

#Searches the dictionary and prints multiple key value pair and incase any key isn't present, it adds it to the dict and prints it along with the others.

def multiple_search():
	     result={}
	     s1=[]
	     s=0
	     name1=input(">>>Enter the names of the contacts seperated by commas😮‍💨: ").split(",")
	     for i in name1:
	     			i=i.upper()
	     			if i in contacts:
	     				result[i]=contacts[i]
	     			else:
	     				s1.append(i)
	     				s+=1
	     if s>0:
	     	c=(input(f"\nCouldn't find contacts {s1} 😕. \nDo you wish to add them?😗 Enter Yes or No: ")).lower()
	     	if c=="yes":
	     		for i in s1:
	     			new_contact(i)
	     			if i in contacts:
	     				result[i]=contacts[i]
	     		print()
	     		print(result)
	     	elif c=="no":
	     		print()
	     		if result=={}:
	     			pass
	     	else:
	     		print("\n")
	     else:
	     	print()
	     	print(result)
	     	
#adds new contact every time its called			
	     		
def new_contact(contact_name):
	     print()
	     contact_number=int(input(">>>Enter their contact number👀: "))
	     contacts[contact_name]=contact_number
	     
choice=int(input("Would you like to: \n\n1. Search for a single contact👤 \n2. List all the contacts📜 \n3. Search for multiple contacts👥 \n \n>>>Enter your choice: "))

if choice==1:
	single_search()
	
elif choice==2:
	print()
	print(contacts)
	
elif choice==3:
	multiple_search()

else:
	print("Choose from the given options!")