import time, os 

items=[]
itemsread=[]
try:
  f=open("items.txt","r")
  items=eval(f.read())
  f.close()
except:
  pass

def add():
  name=input(f"{'Name of the item: '}").strip().capitalize()
  items.append(name)
  print()
  print("Item succesfully added!")

  f=open("items.txt","w")
  f.write(str(items))
  f.close()
def rem():
  while True:
    del_item=input(f"{'Enter the name of the item You want to delete: ':>20}").strip().capitalize()
    if del_item in items:
      items.remove(del_item)
      print()
      print(f"{'Item has been succesfully deleted':>20}")
     

      f=open("items.txt","w")
      f.write(str(items))
      f.close()
      
      break
    

  
    elif del_item not in items:
      print()
      ret=input(f"{'Item not on the list try again or return to main menu? (a/r):'>20}")
      if ret=="a":
        continue
      elif ret=="r":
        break
      
def view():
  print(f"{'Item name':^15} | {'Item Count':^15}")
  print()
  for index in range(len(items)):
    if items[index] not in itemsread:
      print(f"{items[index]:^15} | {items.count(items[index]):^15}")
      itemsread.append(items[index])
  print()
  while True:
    ret=input("Do you want to return to the main menu? (y/n): ")
    if ret=="y":
      break
    else:
      continue

while True:
  time.sleep(2)
  os.system("cls")
  print("INVENTORY")
  print()
  menu=input("Enter the correct number to go to the submenu:\n\n 1:Add Item\n 2:View Items\n 3:Remove Item\n\n: ")
  if menu=="1":
    print()
    add()
  elif menu=="2":
    print()
    view()
    itemsread=[]
  elif menu=="3":
    print()
    rem()
  