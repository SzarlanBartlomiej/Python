import time,os

def pprint():
  for row in todolist:
    for item in row:
      print(f"{item:^10}",end=" | ")
    print()
    print()

todolist=[]


while True:
  os.system("clear")
  print(f"{'Welcome to your to do list menu':^50}")
  print()
  print(f"{'Do you want to add task | view | edit | remove task | on the list ? '}")
  print()
  menu=input(":").strip().lower()[0]
  if menu=="a":
    print()
    thing=input("Name what is to do\n: ")
    print()
    when=input("When it is to be done \n:")
    print()
    prio=input("What is the priority? (low, medium, high)\n ")
    row=[thing,when,prio]
    todolist.append(row)
    print()
    print(f"{'Item was added to your to do list':^30}")
    time.sleep(2)
  elif menu=="v":
    os.system("clear")
    print()
    print(f"{'Welcome to to do list viewer. Choose the options below':^50}")
    print()
    view=input("Press 1 to view all\nPress 2 to view tasks by priority\n\n")
    if view=="1":
      os.system("clear")
      print(f"{'These are your all tasks:':^50}")
      print()
      pprint()
      print()
      ret=input("Do you want to return to the main menu? y/n\n").strip().lower()
      if ret=="y":
        continue
      else:
        breakpoint
          
    elif view=="2":
      os.system("clear")
      prio=input(f"{'what tasks do you want to view (low,medium,high)?':^50}\n:")
      print()
      print()
      print(f"{'These are your all'} {prio} {'priority'} {'tasks'}")
      print()
      for row in todolist:
        if row[2]==prio:
            for item in row:
              print(f"{item:^10}",end=" | ")
            print()
            print()
      ret=input("Do you want to return to the main menu? y/n\n").strip().lower()
      if ret=="y":
         continue
  elif menu=="e":
    os.system("clear")
    print(f"{'Welcome to tasks editor!':^50}")
    print()
    which=input("Which task do you want to edit?\n")
    print()
    for row in todolist:
      for item in row:
        if item==which:
          print("Editing task:")
          print()
          for item in row:
            print(f"{item:^10}",end=" | ")
          print()
          print()
          print("Enter new information to the task\n")
          print()
          row[0]=input("Name of the task\n:")
          row[1]=input("When it is to be done\n:")
          row[2]=input("Priority of the task\n:")
          print()
          print(f"{'Succesfully edited the task!':^50}")
          print()
          ret=input("Do you want to return to the main menu? y/n\n").strip().lower()
      if ret=="y":
         continue
  elif menu=="r":
    os.system("clear")
    print(f"{'Tasks remover':^50}")
    print()
    rem=input("Enter the name of the task you want to remove\n")
    print()
    counter=0
    for row in todolist:
      for item in row:
        if item==rem:
          print("Task has been found ")
          ans=input("Are you sure you want to remove the item?:y/n\n")
          if ans=="y":
            todolist.remove(row)
            print()
            print("Task succesfully removed")
            ret=input("Do you want to return to the main menu?:y/n\n").strip().lower()
            if ret=="y":
              continue