import random,os,time
def cp(c,t):
  if c=="y":
    print(f"\033[1;33m,{t},\033[0m")
def addidea():
  print(f"{'Hello, here you can add your idea!':^20}\n")
  print("\033[1;33m")
  idea=input("Your Idea: \n\033[0m")
  f=open("my.ideas","a+")
  f.write(f"{idea}\n")
  f.close()
  print()
  print(f"{'Your idea has been added!':^20}")
  time.sleep(2)
  os.system("clear")
  
def randidea():
  f=open("my.ideas","r")
  list=f.read().split("\n")
  list.remove('')
  max=(len(list))-1
  index=random.randint(0,max)
  print("This is your random task:")
  print()
  print(list[index])
  time.sleep(2)
  os.system("clear")
  


while True:
  print(f"{'Ideas searching tool!':^20}")
  menu=input("Do you want to add new ide or see a random idea a/r ?: ").lower().strip()[0]
  if menu=="a":
    addidea()
  elif menu=="r":
    randidea()
