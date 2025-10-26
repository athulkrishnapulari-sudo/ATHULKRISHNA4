def add_new_contact():
    def namefn():
        name=input("ENTER THE NAME OF THE CONTACT : ")
        return name   
    def numbers():
        number=input("ENTER THE CONTACT NUMBER : ")
        if number.isdigit()==True:
            a=len(number)
            if a==10:
                pass
            else:
                print("INVALID CONTACT NUMBER, IT SHOULD BE 10 DIGITS , YOU ENTERED ",a,"DIGITS.")
                numbers()
        else:
            print("INVALID CONTACT NUMBER ,IT SHOULD CONTAIN ONLY DIGITS.")
            numbers()
        return number  
    def emails():
        email=input("ENTER THE EMAIL ADDRESS : ")
        if ('@' not in email)==True or ("." not in email)==True:
            print("INVALID EMAIL ADDRESS.")
            emails()
        return email
    name=namefn()
    number=numbers()
    email=emails()
    contact={'NAME':name,'PHONE_NO':number,'EMAIL':email}
    import json
    f=open('contacts.json','r')
    try:
        contacts=json.load(f)       
    except Exception:
        contacts=[]  
    found=0
    for i in contacts:
        if i['PHONE_NO']==number:
            found=1          
    if found==1:
        print("THE PHONE NUMBER IS ALREADY ASSOCIATED WITH A CONTACT")
        print("="*45)
        print("")
        print("CONTACT_NAME : ",i['NAME'])
        print("CONTACT_NUMBER : ",i['PHONE_NO'])
        print("CONTACT_EMAIL : ",i['EMAIL'])
        print("")
        print("="*45)
    else:
        contacts.append(contact)
        with open('contacts.json','w')as f:
            json.dump(contacts,f,indent=4)
        print("!!!CONTACT SAVED SUCCESSFULLY!!!")



def view_all_contacts():
    import json
    f=open('contacts.json','r')
    try:
        contacts=json.load(f)
    except Exception:
        contacts=[]
        print("YOUR CONTACT LIST IS EMPTY!!!")
    print("="*45)
    print("                CONTACT BOOK                 ")
    print("="*45)    
    for i in contacts:       
        print("="*45)
        print("CONTACT_NAME : ",i['NAME'])
        print("CONTACT_NUMBER : ",i['PHONE_NO'])
        print("CONTACT_EMAIL : ",i['EMAIL'])
        print("="*45)


def search_contact():
    name=input("ENTER THE NAME OF THE CONTACT YOU WANT TO SEARCH : ")
    import json
    f=open('contacts.json','r')
    try:
        contacts=json.load(f)
    except Exception:
        contacts=[]
    found=0
    for i in contacts:
        if i['NAME']==name:
            print("="*45)
            print("CONTACT_NAME : ",i['NAME'])
            print("CONTACT_NUMBER : ",i['PHONE_NO'])
            print("CONTACT_EMAIL : ",i['EMAIL'])
            print("="*45)
            found=1
    if found!=1:
        print("CONTACT NOT FOUND")

        


def delete_contact():
    name=input("ENTER THE NAME OF THE CONTACT YOU WANT TO DELETE : ")
    import json
    f=open('contacts.json','r')
    try:
        contacts=json.load(f)       
    except Exception:
        contacts=[]
    found=0    
    for i in contacts:
        if i['NAME']==name:
            contacts.remove(i)
            found=1
            break
    if found==1:
        print("CONTACT REMOVED SUCCESSFULLY!!!")
        with open('contacts.json','w')as f:
            json.dump(contacts,f,indent=4)
    else:
        print("CONTACT NOT FOUND")



def menu():
    while True:
        print("="*45)
        print("                MAIN MENU                 ")
        print("="*45)
        print("1.ADD A NEW CONTACT")
        print("2.VIEW ALL CONTACTS")
        print("3.SEARCH A CONTACT")
        print("4.DELETE A CONTACT")
        print("5.EXIT")
        print("="*45)
        choice=int(input("ENTER YOUR CHOICE : "))
        if choice == 1:
            add_new_contact()
        elif choice == 2:
            view_all_contacts()
        elif choice==3:
            search_contact()
        elif choice==4:
            delete_contact()
        elif choice == 5:
            break
        else:
            print("!!!INVALID CHOICE , PLEASE TRY AGAIN.")


menu()