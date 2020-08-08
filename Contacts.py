import tkinter as tk
import os
import json

HEIGHT = 600
WIDTH = 800

TitleFont=('Berlin Sans FB Demi',20,'bold')
ButtonFont = ('Impact',15,)
EntryFont = ('Arial', 16)
TextFont= ('Impact',20,)
#-----------------#


# Opening the Json File if it doesnt exist and empty list is used
ContactList=[]
if os.path.isfile("ContactList.json"):
    with open("ContactList.json", 'r') as f:
        ContactList = json.load(f)
#-------------#

#----FUNCTIONS-----#

def GetData(name,numbers,addresses,emails):
    if len(name) >0:
        name= name
        numbers=TakeNumber(numbers)
        addresses =TakeAddress(addresses)
        emails=TakeEmail(emails)
        return (name,numbers,addresses,emails)

def MakeContact(Name,Numbers,Addresses,Emails):
    try:
        name,numbers,addresses,emails = GetData(Name.get(),Numbers.get(),Addresses.get(),Emails.get())
        Name.delete(0, 'end')
        Numbers.delete(0, 'end')
        Addresses.delete(0, 'end')
        Emails.delete(0, 'end')
        node=Create(name,numbers,addresses,emails)
        SaveContact(node)
    except:
        Name.delete(0, 'end')
        Name.insert(0,'Enter a name')
        Numbers.delete(0, 'end')
        Addresses.delete(0, 'end')
        Emails.delete(0, 'end')
        
def ClearEntry():
   pass

def Create(Name,Numbers,Addresses,Emails):
    contact={} 
    contact[Name]={'Number':Numbers,'Address':Addresses,'Email':Emails}
    return(contact)

def TakeNumber(numbers):
    """ Returns a list of numbers"""
    try:
        return [int(number) for number in numbers.split(",")]
    except:
        return [00]

def TakeAddress(addresses):
    """ Returns a list of Addresses"""
    try:
        return [address for address in addresses.split('/')]
    except:
        return ["no address"]

def TakeEmail(emails):
    """ Returns a List of Emails"""
    try:
        return [email for email in emails.split(',')]
    except:
        return ["no email"]

def SaveContact(Contact):
    ContactList.append(Contact)
    with open("ContactList.json", 'w') as f:
        json.dump(ContactList,f)
def OpenNewPage(canvasname,Titlename,NextpageName=None):
    canvasname.destroy()
    Titlename.destroy()
    if NextpageName!= None:
        NextpageName()
#--------------------------------------#


# Screens
def NewContact():
   
    Title= tk.Label(root, text="New Contact",font=TitleFont,pady=10,padx=10,bd=4,relief = 'raised')
    Title.pack(side='top')
    Canvas= tk.Canvas(root, height=HEIGHT, width = WIDTH, bg='#ffff00')
    Canvas.pack()


    NameLabel= tk.Label(Canvas,text="Name:",font=TextFont, bg='#ffff00')
    NameLabel.place(relx=0.02,rely=0.02)

    NumLabel= tk.Label(Canvas,text="Number:",font=TextFont, bg='#ffff00')
    NumLabel.place(relx=0.02,rely=0.22)

    AdLabel= tk.Label(Canvas,text="Address:",font=TextFont, bg='#ffff00')
    AdLabel.place(relx=0.02,rely=0.42)

    ELabel= tk.Label(Canvas,text="Email:",font=TextFont, bg='#ffff00')
    ELabel.place(relx=0.02,rely=0.62)

    Name= tk.Entry(Canvas, width= round(WIDTH*0.04), font=EntryFont )
    Name.place(relx=0.02 , rely=0.1)
    Name.focus_set()

    Number= tk.Entry(Canvas,width= round(WIDTH*0.04), font=EntryFont)
    Number.place(relx=0.02,rely=0.3)
    

    Address= tk.Entry(Canvas,width= round(WIDTH*0.04), font=EntryFont)
    Address.place(relx=0.02,rely=0.5)
    

    Emails= tk.Entry(Canvas,width= round(WIDTH*0.04), font=EntryFont)
    Emails.place(relx=0.02,rely=0.7) 
    
    Submit= tk.Button(Canvas,text="Submit",font=ButtonFont,padx=30,pady=10,bg=None
                        , command= lambda : MakeContact(Name,Number,Address,Emails))
    Submit.place(relx=0.7,rely=0.8)
    
    Back =  tk.Button(Canvas,text="Back",padx=20,font=ButtonFont, command = lambda : OpenNewPage(Canvas,Title,OpenScreen))
    Back.place(relx=0.875,rely=0.01)
        
def OpenScreen():

    Title= tk.Label(root,text="Contacts",font= TitleFont,bd=4,relief = 'raised',pady=10,padx=10)
    Title.pack(side='top')

    canvas1 = tk.Canvas(root, height=HEIGHT, width = WIDTH, bg='#ffff00')
    canvas1.pack()

    
    frame= tk.Frame(canvas1,bg='#b3b3b3',relief='raised',bd=1,)
    frame.place(relx=0.1,rely=0.05,relheight=0.8,relwidth=0.8,)

    New = tk.Button(canvas1,text="Make new Contact", padx =15 , pady=15,
                    font= ButtonFont, command= lambda : OpenNewPage(canvas1,Title,NewContact))
    New.place(relx=0.1125, rely=0.85)

    Edit=  tk.Button(canvas1,text="Edit a Contact", padx =30 , pady=15, 
                    font= ButtonFont, command = lambda :OpenNewPage(canvas1,Title,EditContact))
    Edit.place(relx=0.65, rely=0.85)

    Exit = tk.Button(canvas1,text="Exit", padx =30 , pady=15, font= ButtonFont,command=lambda :root.quit())
    Exit.place(relx=0.4275,rely=0.875)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack( side = 'right', fill = 'y' )
    Appname = tk.Listbox(frame,yscrollcommand = scrollbar.set,font=TextFont,bg='#b3b3b3',)
    for contact in ContactList:
      for name in contact:
            Appname.insert('end',f" {name} : {contact[name]['Number'][0]}")
    Appname.place(relx=0,rely=0,relheight=1,relwidth=1,)

def EditContact():
    Title= tk.Label(root, text="Edit Contact",font=TitleFont,pady=10,padx=10,bd=4,relief = 'raised')
    Title.pack(side='top')

    Canvas= tk.Canvas(root, height=HEIGHT, width = WIDTH, bg='#ffff00')
    Canvas.pack()

    Text= tk.Label(Canvas, text="Which contact do you want to change",font=TextFont, bg='#ffff00')
    Text.place(relx=0.225 , rely=0.4)

    Search= tk.Entry(Canvas, width= round(WIDTH*0.04), font=EntryFont)
    
    Search.place(relx=0.25 , rely=0.5)
    
    SearchButton = tk.Button(text="Edit a Contact", padx =30 , pady=15, 
                    font= ButtonFont,)
    SearchButton.place(relx=0.38,rely=0.6)

if __name__ =='__main__':
    root = tk.Tk()
    root.title("Contacts")
    OpenScreen()

    root.mainloop()