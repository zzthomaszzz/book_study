print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
# this function here print '.' but like '.' + '.' 10 times which just add them together
print("." * 10)  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# what that comma at the end. try removing it to see what happens
# so in print() function if you have end='' at the end the next print you make will connect with each other?
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
# testing
print("Hi mom,", end=' ')
print("It's me")