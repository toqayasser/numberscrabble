#Program Name: Number scrabble game
#Program Description: is played with the list of numbers between 1 and 9. Each player takes
#turns picking a number from the list. Once a number has been picked, it cannot be picked
#again. If a player has picked three numbers that add up to 15, that player wins the game.
#However, if all the numbers are used and no player gets exactly 15, the game is a draw.
#Last Modification Date: 12\3\2022
#by toqa yasser


import sys 
num_list=[1,2,3,4,5,6,7,8,9]
player1_list=[]
player2_list=[]
while len(num_list)!= 0 :
     print("choose number:", num_list)
     x=int(input("player1's turn="))
     if x in num_list:
       num_list.remove(x)
       player1_list.append(x)  
     else:
         while x not in num_list : 
               x=int(input("please choose number from the list "))
         num_list.remove(x)
         player1_list.append(x)  
     for i in range (len(player1_list)):
	     for j in range(i+1,len(player1_list)):
		     for k in range(j+1,len(player1_list)):
			     if player1_list[i]+player1_list[j]+player1_list[k]==15:
				     print("player 1 wins")
                         sys.exit()
y=int(input("player2's turn ="))
     if y in num_list:
         num_list.remove(y)
         player2_list.append(y)  
     else:
          while y not in num_list : 
               y=int(input("please choose number from the list "))
          num_list.remove(2)
          player2_list.append(y)  
     for i in range (len(player2_list)):
	     for j in range(i+1,len(player2_list)):
		     for k in range(j+1,len(player2_list)):
			     if player2_list[i]+player2_list[j]+player2_list[k]==15:
				     print("player 2 wins") 
                         sys.exit()
print("draw")                         

