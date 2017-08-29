"""Restaurant rating lister."""

# Reads the ratings in from the file
# Stores them in a dictionary, and then
# Spits out the ratings in alphabetical order by restaurant
# Hint 1: Using .items() to get a list of your dictionary entries will help with sorting.

# Hint 2: Refer to the python docs on the sorted() function if you need a reminder of how to sort.


# put your code here

restaurant_ratings = {}

def create_rest_dict(filename):
    filename = open(filename)


    for line in filename:
        line = line.rstrip()
        rest_data = line.split(':')
        rest = rest_data[0]

        if rest not in restaurant_ratings:
            restaurant_ratings[rest_data[0]] = rest_data[1]


    rests = restaurant_ratings.items()

    sorted_rests = sorted(rests)

    for i in range(len(sorted_rests)):
        print "%s is rated at %s." % (sorted_rests[i][0], sorted_rests[i][1])

create_rest_dict('scores.txt')


def add_rating():

   # restaurant_ratings = create_rest_dict('scores.txt')

    while True:
        restaurant_name = raw_input('What is the restaurant\'s name?')
        restaurant_rating = int(raw_input('How do you rate this restaurant?'))

        if (restaurant_rating >= 1 and restaurant_rating <= 5):
            restaurant_ratings[restaurant_name] = restaurant_rating
            return False
        else:
            print "Please enter a number between 1 and 5"

add_rating()


def user_pick():
    user_choice = raw_input("Welcome to restaurant ratings. Would you like to: (s)ee all ratings, (a)dd a new rating, or (q)uit?")

    if user_choice == 's':
        return create_rest_dict('scores.txt')
    elif user_choice == 'a':
        return add_rating()
    elif user_choice == 'q':
        return
    else:
        "Please choose a valid input"

user_pick()
