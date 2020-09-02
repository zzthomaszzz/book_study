name = 'Zed A.Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
kilo = round(weight * 0.45359237)

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {kilo} kilo heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + kilo
print(f"If i add {age}, {height}, and {kilo} i get {total}.")