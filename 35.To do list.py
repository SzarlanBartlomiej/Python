import os,time
def cprint(c):
  if c=="red":
    return ("\033[31m")
  elif c=="yellow":
    return ("\033[33m")
  elif c=="blue":
    return ("\033[32m")
  elif c=="white":
    return ("\033[0m")     
def lprint():
  os.system("cls")
  print(f"{cprint('yellow')}","Items included in the list:",f"{cprint('white')}")
  print()
  for index in range(len(todolist)):
    print(f"{index+1}:{todolist[index]}")
  print()
  menu=input("Do you want to go back to the main menu? (y/n)\n>")
  if menu=="y":
    os.system("cls")
  else:
    lprint()
todolist=[]
head="Welcome - This is Your new to do list manager"
print(f"{cprint('red')}"f"{head:^60}")
print()
while True:
  main="Do you want to add, remove, edit or view the items on the list?"
  print(f"{cprint('white')}"f"{main}")
  print()
  answer=input("")
  if answer=="add":
    print()
    item=input("Name the item you want to add to the list:\n\n")
    if item in todolist:
      print()
      print(f"{cprint('red')}","The item is already on the list",sep="")
      print()
    else:
      todolist.append(item)
      print()
      print(f"{cprint('yellow')}","Item was added to your list",sep="")
      print()
  elif answer=="remove":
    print()
    item=input("Name the item you want to remove from the list:\n\n")
    if item in todolist:
      print()
      print(f"{cprint('yellow')}","Are you absolutely sure you want to remove this item? y/n",f"{cprint('white')}",sep="")
      answer=input(">")
      if answer =="y":
        todolist.remove(item)
        print()
        print(f"{cprint('red')}","Item was succesfuly removed from the list.")
        print()
      elif answer=="n":
        print()
        print("Deletion cancelled")
        print()
      else:
        print()
        print("wrong command")
    else:
      print()
      print(f"{cprint('red')}","The item doesnt't exist")
  elif answer=="edit":
    print()
    itemtochange=input("Name the item you wish to edit\n >")
    print()
    if itemtochange in todolist:
      itemchangeto=input("Enter a corrected record:\n")
      print()
      index=todolist.index(itemtochange)
      todolist[index]=itemchangeto
      print(f"{cprint('yellow')} The item was succesfully edited")
    else:
        print(f"{cprint('red')} Item is not included in the list.")
  elif answer=="view":
    lprint()
  else:
    print(f"{cprint('red')} Wrong command - Try again")
  time.sleep(3)
  os.system("cls")