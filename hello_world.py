aliens = 2
passward = "ALIENS"

print()
print("WELCOME TO THE GLOBAL DEVENCE PLATFORM")
print()
print("Aliens are invading")
guiss = input("passward ")
while aliens < 7200000:
  if guiss.upper()!=passward:
    aliens = aliens ** 2 * 3 // 4
    print(f"Incorrect passward. there are { aliens } aliens")
    print("please try again")
    print("HINT: what are attaching us")
    guiss = input("try again ")
  else:
    print("thank you, all is saved")
    break
if aliens > 7200000:
  print("no!!! all is lost")
