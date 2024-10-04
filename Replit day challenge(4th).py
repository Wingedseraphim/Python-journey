print("=== Your adventure simulator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
story with YOU as the star! 🤩""")
print( )
name = input("Your name: ")
enemy = input("Your worst enemy's name: ")
superPower = input("Your superPower: ")
print( )
print("our story begins as our hero", name, "approaches a foreboding castle...")
print("suddenly a bolt of lightning striked the ground at the feet of",name)
print("\033[31", "our final battle begins!", "\033[0m", "'shouts the evil", enemy,"clearly missing the fact that",name, "has the power of"
      ,"\033[35m",superPower,"\033[0m", "which means they'll win quite easily")
