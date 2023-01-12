todolist=[]
def ListPrint():
  print()
  for item in todolist:
    print(item)
    print()
logo=("== To do list manager ==")
print("\033[31m",f"{logo:^50}","\033[0m")
print()
while True:
  answer=input("Do you want to add/remove item to the list or do you want to check the list?:")
  if answer=="add":
    print()
    item=input("Name the item You want to add:")
    todolist.append(item)
    print()
    print("Item was added to the list")
    print()
  elif answer=="remove":
    print()
    item=input("Name the item You want to remove:")
    if item in todolist:
      todolist.remove(item)
      print()
      print("Item was removed from the list ")
      print()
    else:
      print("The item is not present in the list. a")
      print()
  elif answer=="check":
    ListPrint()
  else:
    continue