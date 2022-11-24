print (" ")
print ( "Welcome to the Day Trip Generator! Where our services take all the stress away from planning an unforgettable vacation! ")
print ( " ")

# destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists. 

import random

destination_list= ['New York' , 'Seattle' , 'California']
ran_des= random.choice(destination_list)

# print(random.choice(destination_list))
print("We have chosen", random.choice(destination_list),"for your destination!","Does this sound good?")



restaurants_list= ["Lombardi's", 'The Pink Door', "Mastro's"]
ran_res= random.choice(restaurants_list)
print ("We have chosen", random.choice(restaurants_list),"for your restaurant!","Does this sound good?")





transportation_list= ['rental car', 'Uber', 'train']
ran_trans= random.choice(transportation_list)
print ("We have chosen", random.choice(transportation_list),"for your transportation!","Does this sound good?")





entertainment_list= ['Rockefeller Center', 'Space Needle', 'Universal Studios']
ran_enter= random.choice(entertainment_list)
print("We have chosen", random.choice(entertainment_list),"for your entertainment!","Does this sound good?") 