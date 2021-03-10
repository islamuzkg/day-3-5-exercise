# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

fnames = name1 + name2
u_sh = fnames.upper()
T = u_sh.count("T")
R = u_sh.count("R")
U = u_sh.count("U")
E = u_sh.count("E")

L = u_sh.count("L")
O = u_sh.count("O")
V = u_sh.count("V")
E = u_sh.count("E")


TRUE_C = int(T) + int(R) + int(U) + int(E)
LOVE_C = int(L) + int(O) + int(V) + int(E)
score = int(str(TRUE_C) + str(LOVE_C))
#print(score)
if (score <= 10) or (score >= 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")