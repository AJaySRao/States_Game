# States_Game
Well this game is a concept of guess the state name of a country

Andhra Pradesh, Arunachal Pradesh, Assam, Bihar, Chhattisgarh, Delhi, Goa, Gujarat, Haryana, 
Himachal Pradesh, Jammu & Kashmir, Jharkhand, Karnataka, Kerala, Madhya Pradesh, 
Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland, Odisha, Punjab, Rajasthan, Sikkim, 
Tamil Nadu, Telangana, Tripura, Uttar Pradesh, Uttarakhand, West Bengal

Steps:
1. Get .gif format of country map
2. Set it as bg to screen 
3. Create states.csv document with list of state names
   1. Add their co-ordinates 
   ---------------------------------------------------
   #used:
   def get_mouse_click_coor(x, y):
     print(x, y) 
   
   turtle.onscreenclick(get_mouse_click_coor)
   turtle.mainloop()
   ---------------------------------------------------
4. Get answer from player 
   1. Check if the answer is in states list
   2. Reveal the location of the state

5. Add an option to quit the game in middle 
6. On completion or quit, show missed stated in states_to_learn.csv document
