"""Restaurant rating lister."""

# Reads the ratings in from the file
# Stores them in a dictionary, and then
# Spits out the ratings in alphabetical order by restaurant
# Hint 1: Using .items() to get a list of your dictionary entries will help with sorting.

# Hint 2: Refer to the python docs on the sorted() function if you need a reminder of how to sort.


# put your code here
filename = open('scores.txt')

restaurant_ratings = {}

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


def add_rating():

    while True:
        restaurant_name = raw_input('What is the restaurant\'s name?')
        restaurant_rating = int(raw_input('How do you rate this restaurant?'))

        if (restaurant_rating >= 1 and restaurant_rating <= 5):
            restaurant_ratings[restaurant_name] = restaurant_rating
            return False
        else:
            print "Please enter a number between 1 and 5"


add_rating()
