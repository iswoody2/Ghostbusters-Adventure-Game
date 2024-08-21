print('''
**************************************************************
     _               _   _               _                
   __ _| |__   ___  ___| |_| |__  _   _ ___| |_ ___ _ __ ___ 
  / _` | '_ \ / _ \/ __| __| '_ \| | | / __| __/ _ \ '__/ __|
 | (_| | | | | (_) \__ \ |_| |_) | |_| \__ \ ||  __/ |  \__ 
  \__, |_| |_|\___/|___/\__|_.__/ \__,_|___/\__\___|_|  |___/
  |___/                                                      
                       ___               
                    -        --                             
                --( /     \ )XXXXXXXXXXXXX                   
            --XXX(   O   O  )XXXXXXXXXXXXXXX-              
           /XXX(       U     )        XXXXXXX\               
         /XXXXX(              )--   XXXXXXXXXXX\             
        /XXXXX/ (      O     )   XXXXXX   \XXXXX
        XXXXX/   /            XXXXXX   \   \XXXXX----        
        XXXXXX  /          XXXXXX         \  ----  -         
---     XXX  /          XXXXXX      \           ---        
  --  --  /      /\  XXXXXX            /     ---=         
    -        /    XXXXXX              '--- XXXXXX         
      --\/XXX\ XXXXXX                      /XXXXX         
        \XXXXXXXXX                        /XXXXX/
         \XXXXXX                         /XXXXX/         
           \XXXXX--  /                -- XXXX/       
            --XXXXXXX---------------  XXXXX--         
               \XXXXXXXXXXXXXXXXXXXXXXXX-            
                 --XXXXXXXXXXXXXXXXXX-
**************************************************************
''')
print("Welcome to the GhostBusters, New Recruit .")
print("Your first mission as a New Ghostbuster is to find....\n  The ghost in the hotel... \n Enjoy, Don't Die "
      "Recruit !")
name = input("What is your name, Recruit ?")

lobby = input("You reach the lobby of the hotel... \n You can either take the right or left stairs.... \n "
              "Type right or left to choose which direction to go ")
if lobby == "left" or "Left" or "LEFT":
      print("You go up the left stair, \n but there is ghost slime on the rest of the floors above the sixth floor...")
      elevator = input("You reach the sixth floor.... \n You can either take the elevator or a ladder to find the ghost on the ninth floor \n"
                       "Type wait to wait for the elevator or Type climb to climb the ladder")
      if elevator == "climb" or "CLIMB" or "Climb ":
            Door = input("You reach the ninth floor ... \n There are ghost noises everywhere but only three doors \n"
                         "Type red to open the red door, Type yellow to open the yellow door, Type blue to open the blue door")
            if Door == "red" or "RED" or "Red":
                  print(f"Oh no, you just missed the Ghost \n Better luck next time, Ghostbuster{name}")
            elif Door == "blue" or "BLUE" or "Blue":
                  print(f"Oh no, the Ghost ate all the pizza and escaped \n Better luck next time, Ghostbuster {name}")
            elif Door == "Yellow" or "YELLOW" or "yellow":
                  print("You found the Ghost \n You placed down the trap and caught him \n "
                        f"They know, who their going to call now {name} GHOSTBUSTERS!!!! ")
            else:
                  print("Oh no, the Ghost is behind you, \n The Ghost slimes you and escapes")
      else:
           print("You enter the elevator .... \n It starts to shake and suddenly it becomes dark ... \n "
                  f"You fall to the bottom floor, breaking all your toes \n Early retirement for you, Ghostbuster {name} :( ")
else:
      print(f"You take a step onto the right stairs... \n The stairs break, you fall breaking your legs \n "
          f"Early retirement for you, Ghostbuster {name} :( ")
