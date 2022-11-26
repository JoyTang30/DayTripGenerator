print (" ")
print ( "Welcome to the Day Trip Generator! Where our services take all the stress away from planning an unforgettable vacation! ")
print ( " ")

# destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists. 

import random

user_response= "no"

while user_response != "yes":
    def ran_des ():
        destination_list= ['New York' , 'Seattle' , 'California']
        return random.choice(destination_list)
    ran_de= ran_des()

    user_response= input(f'We have chosen {ran_de} for your destination! Does this sound good? yes or no?')


    
user_response2= "no"
    
while user_response2 != "yes":
    def ran_res():
        restaurants_list= ["Lombardi's", 'The Pink Door', "Mastro's"]
        return random.choice(restaurants_list)
    ran_re= ran_res()
    user_response2= input(f'We have chosen  {ran_re} for your restaurant! Does this sound good? yes or no?')


user_response3= "no"
    
while user_response3 != "yes":
    def ran_trans():
        transportation_list= ['rental car', 'Uber', 'train']
        return random.choice(transportation_list)
    ran_tran = ran_trans()
    user_response3= input(f'We have chosen {ran_tran} for your transportation! Does this sound good? yes or no?')



user_response4= "no"

while user_response4 != "yes":
    def ran_enter():
        entertainment_list= ['Rockefeller Center', 'Space Needle', 'Universal Studios']
        return random.choice(entertainment_list)
    ran_ente= ran_enter()
    user_response4= input(f'We have chosen {ran_ente} for your entertainment! Does this sound good? yes or no?') 




overall_satisfaction= input(f' We have chosen for you {ran_de} as your destination, {ran_re} as your restaurant, {ran_tran} as your transportation, and {ran_ente} as your entertainment. Are you happy with this trip? yes or no?')
if overall_satisfaction == "yes":
    print("Great! Your trip is complete")
else: 
    print( "Try again!")