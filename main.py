
mokedex = {}
def prettyPrint():
  print()
  for key,value in mokedex.items():
    print(key, end=": ")
    for subKey,subValue in value.items():
      print(subKey,
            subValue, end=" | ")
      print()

while True :
  name = input("Beast Name: ")
  type = input("Type: ")
  move = input("Special Move: ")
  hp = input("HP: ")
  mp = input("MP: ")
  mokedex[name] = {"Type":type, "Special Move": move, "HP": hp, "MP": mp}
  
  prettyPrint()
  again = input("Again? yes/no ?")
  if again == "no":
    break
  else:
    continue
  #exit
print("I end this game!")
  





  

  




