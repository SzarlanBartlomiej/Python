print("HIGH SCORE NUMBERS")
print()
while True:
  print()
  name=input("Enter your name: ")
  points=input("Enter your points ")
  f=open("high.score","a+")
  score=f"{name} - {points}\n"
  f.write(score)
  f.close()
  print()
  print("ADDED")
  next=input("Do you wish to add another data? y/n")
  if next=="y":
    continue
  else:
    break
  