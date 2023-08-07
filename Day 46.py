import os
beastlist={}
print("Moke Beast")
print()
def pprint():
  print()
  for key,value in beastlist.items():
    print(f"Name of The monster:\n\n {key:>25}")
    for subkey, subvalue in value.items():
      print(f"{subkey} | {subvalue}")
  print()
def addbeast():
  print()
  name=input("The name of the beast: ")
  Type=input("Enter the type of the beast: ")
  SpecialMove=input("Special Move: ")
  Hp=input("Health Points: ")
  Mp=input("Mana Points: ")
  beastlist[name]={"Type":Type,"Special Move":SpecialMove, "HP":Hp,"MP":Mp}


while True:
  os.system("cls")
  print(f"{'Welcome to main menu of MokeBeast!':>25}")
  print()
  menu=input("Do you want to add the beast(1) or print all the added beasts?(2): ")
  if menu=="1":
    addbeast()
  elif menu =="2":
    pprint()
    print()
    ret=input("Enter any key to return to the main menu: ")