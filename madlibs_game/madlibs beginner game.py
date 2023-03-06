# Bulding Madlibs Game (beginner level using just the Cmd)

print("Welcome to Bammy madlibs game (Beginner Level")
user_name = input("Enter your Name: " )
print("Nice having you here " + user_name + "")

#Writing the game codes
print(user_name + " input all the require details")

#collecting the datas
animals = input("Enter an animal: ")
professions = input("Enter Profession: ")
cloth = input("Enter Cloth: ")
things = input("Enter a things: ")
name = input("Enter a name: ")
place = input("Enter place:")
verb = input("Enter a verb: ")
food = input("Enter food of your choice ")

#Now the answer begins

print("say " + food + " the photographer said as the camera flashed \n" + name + " and i had gone to " + place +
      " to get our photos taken on my birthday.\nThe first photo we really wanted was a picture of us dressed"
      " as " + animals + " \npretending to be a " + professions + " When we saw the second photo it was exactly\n"
      "what i wanted we both look like " + things + " wearing " + cloth + " and " + verb + "\nexactly what i had "
      "in mind")
