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
    # print sorted_rests[i][0]
    # print sorted_rests[i][1]
    print "%s is rated at %s." % (sorted_rests[i][0], sorted_rests[i][1])
