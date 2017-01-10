#Open file and parse data

def make_dict(filename):

    rest_file = open(filename)
    rest_data = {}

    for line in rest_file:
        restaurant, rating = line.rstrip().split(":")
        rest_data[restaurant] = rating

    return rest_data



def rate_rest(filename):

    """Parse data from file, return dictionary with restaurant name and corresponding rating


"""

rest_data = make_dict(filename)



#User choice
    print "Choose your own adventure!"
    print "You have 3 choices:"
    print "1. View all ratings"
    print "2. Add your own ratings"
    print "3. Quit and say goodbye!"

    user_input = ""
    
    while user_input != "3":
        user_input = raw_input("Enter option 1, 2, or 3: ")
        if user_input == "1":
#print dictionary
            for restaurant, rating in sorted(rest_data.items()):
                print "%s is rated at %s" % (restaurant, rating)
            # continue
        elif user_input == "2":
#rate restaurant
            user_rest = (raw_input("Enter Restaurant Name: ")).capitalize()
            user_rating = int(raw_input("Enter rating 1 to 5: "))

            rest_data[user_rest] = user_rating
        elif user_input == "3":
            print "Thanks for rating!"
            break      
        else:
            print "I'm sorry, I didn't understand that. Try again."


    rest_file.close()

      

rate_rest("scores.txt")


         