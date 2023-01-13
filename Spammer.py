import os, time 
def cprint(c):
  if c=="red":
    return ("\033[31m")
  elif c=="yellow":
    return ("\033[33m")
  elif c=="blue":
    return ("\033[32m")
  elif c=="white":
    return ("\033[0m")
def pprint():
  os.system("cls")
  print(f"{cprint('red')}Current list of emails:"f"{cprint('white')}")
  print()
  for index in range(len(listofemails)):
    print(f"{index}:{listofemails[index]}")
  print()
  menu=input("Back to main menu? (y/n)\n>>>")
  if menu=="y":
    os.system("clear")
  else:
    pprint()
listofemails=[]
while True:
  print("Spammer.inc","\n","Press a corresponding number in order to choose options from the menu:",sep="")
  print()
  mainmenu=f"{cprint('red')}1:Add Email\n"f"{cprint('yellow')}2:Delete Email\n"f"{cprint('blue')}3:Print Emails\n"f"{cprint('white')}4:Send Mails"
  print(f"{mainmenu}")
  print()
  menu=input(">>>")
  if menu=="1":
    print()
    print("Email you wish to add:\n")
    email=input(">>>")
    if email in listofemails:
      print("Email is already in database")
    else:
      listofemails.append(email)
  elif menu=="2":
    print()
    print("Email you wish to delete:\n")
    email=input(">>")
    if email in listofemails:
      listofemails.remove(email)
    else:
      print("Email is not yet added into database")
  elif menu=="3":
    pprint()
  else:
    print()
    print("Wrong command")
  time.sleep(1)
  os.system("cls")