f=open("high.score","r")
score=f.read()
score=score.split("\n")
f.close()
highscore=0

for row in score:
  data=row.split()
  if data!=[]:
    if int(data[1]) > highscore:
      highscore=int(data[1])
      name=data[0]
print(f"{name} {highscore}")

