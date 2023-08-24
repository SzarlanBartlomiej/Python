import os,time 
Pizzas=[]
def price(a,b):
  if a=="s":
    a=1
  elif a=="m":
    a=2.50
  elif a=="l":
    a=5.50
  return a*b
  
try:
  
  f=open("Pizzas.txt","r")
  Pizzas=eval(f.read())
  f.close()
except:
  pass

while True:
  print()
  print(f"{'Welcome to Pizza ordering system':>15}")
  print()
  menu=input(f"{'Do you want to add or view? (a/b): ':>15}").strip().lower()
  if menu=="a":
    print()
    Name=input("What is Your name?: ")
    print()
    Topping=input("What topping would you like?: ")
    print()
    Size=input("What Size of Pizza would you like?: ")
    print()
    try:
      Quantity=int(input("How Many Pizzas would you like?: "))
    except ValueError:
      print("The quantity has to be the whole number!")
      print()
      print("Try again!")
      continue
      
    Price=price(Size,Quantity)
    row=[Name,Topping,Size,Quantity,Price]
    Pizzas.append(row)
  
    f=open("Pizzas.txt","w")
    f.write(str(Pizzas))
    f.close()
  
    print("Your Pizza has been added to the list")
    time.sleep(2)
    os.system("clear")
  elif menu=="v":
    print()  
    print(f"{'This is your list of pizzas':^15}")
    print()
    print(f"{'Name | Topping | Size | Quantity | Price':^15}")
    for row in Pizzas:
      print()
      print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
    print()
    ret=input(f"{'Do you want to return to main menu? (y/n): ' :>20}")
    if ret=="y":
      continue
