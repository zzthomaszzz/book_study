# 10 is stored in this variable
types_of_people = 10
# This variable formatted the one above it and put it in its string
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# the 2 variables above containing a string each are put inside this string below
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
# Variable x and y are both string and are both put inside these two strings below
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
# this function worked because False was formatted into a string and added to the joke
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# this function adding worked because W and E are both strings
print(w + e)