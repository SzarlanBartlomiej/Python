import random,os,time 
listofcards={}
names=[]
def randint(x):
  number=random.randint(1,x)
  return number 
def genCard():
  while True:
    name=input("The name of the card: ")
    int=randint(100)
    hand=randint(10)
    impact=randint(10)
    break
  listofcards[name]={"int":int,"hand":hand,"impact":impact}
  names.append(name)
def pnames():
  counter=0
  for keys,values in listofcards.items():
    counter+=1
    print(f"{counter}:{keys}")
def stat(x):
  if x=="Intelligence":
    return 'int'
  elif x=="Handsomness":
    return 'hand'
  elif x=="Impact":
    return 'impact'

print (f"{'Welcome to TOP TRUMPS':^50}")
print(f"{'Minimal amount of cards to start a game is 2':^50}")


while True:
  print()
  print (f"{'Enter the number of your choosing: ':^50}")
  print()
  menu=input("1: Add a card to the game\n2: Start the game\n3: Exit game\n\n")




  if menu=="1":
    
    print()
    genCard()
    print()
    print("The card was succesfully added!")
    time.sleep(3)
    os.system("cls")



  
  elif menu=="2":
    round=1
    cpoints=0
    ppoints=0
   
    if len(listofcards)<2:
      print()
      print("There is not enough cards to start the game!")
      print("returning to main menu")
      time.sleep(2)
      os.system("cls")
      continue

    
    else:
      while True:
        os.system("cls")
        print(f"{'Welcome to the game phase! Starting round':^30} {round}")
        print()
        print("This is the list of our cards!")
        print()
        pnames()
        print()
        ccard1=input(f"{'Choose your card!':>30}\n\n")
        ccardp=listofcards[ccard1]
        names.remove(ccard1)
        ccard2=random.choice(names)
        ccardc=listofcards[ccard2]
        print()
        print(f"{'The Card You have chosen is':^30}\n\n{ccard1:^30}")
        print()
        print(f"{'The computer has chosen':^30}\n\n{ccard2:^30}")
        print()
        x=input("Choose the stat you wish to fight with! (Intelligence, Handsomness, Impact) \n\n")
        print ()
        print (f"{ccard1} | {ccardp[stat(x)]}")
        print ()
        print (f"{ccard2} | {ccardc[stat(x)]}")
        print()
        if ccardp[stat(x)] > ccardc[stat(x)]:
          print("You Have won with computer!")
          time.sleep(2)
          ppoints+=1
          round+=1
          names.append(ccard1)
        elif ccardp[stat(x)] < ccardc[stat(x)]:
          print ("The computer has won!")
          time.sleep(2)
          cpoints+=1
          round+=1
          names.append(ccard1)
        elif ccardp[stat(x)] ==ccardc[stat(x)]:
          print("We have the draw!")
          time.sleep(2)
          round+=1
          names.append(ccard1)
        if round==4:
          print()
          print("The game has ended!")
          print()
          if cpoints>ppoints:
            print("The computer has won the whole game!")
            print()
            print("Returning to the main menu!")
            time.sleep(2)
            os.system("cls")
            break
          elif cpoints<ppoints:
            print("You have won!")
            print()
            print("Returning to the main menu!")
            time.sleep(2)
            os.system("cls")
            break
          else:
            print ("The match ended with a draw!")
            print()
            print("Returning to the main menu!")
            time.sleep(2)
            os.system("cls")
            break
  elif menu=="3":
    print()
    print(f"{'Thank you for playing the game!':^20}")
    break 
          
        
        
      
      
    
   
    