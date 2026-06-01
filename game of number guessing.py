import  random
secret=random.randint(1,100)
chances=6
while chances>0:
   guess=int(input("guess a number(1-100):"))
   if guess==secret:
        print("🎉correct guess🎉 ",secret)
        break
   elif guess<secret:
        print("⬇️ Too low ⬇️")
   else:
        print ("⬆️ Too high ⬆️")  
   chances-=1
   print("chances left:",chances)
if chances==0:
    print("game over")
    print("correct number was:", secret ) 
  