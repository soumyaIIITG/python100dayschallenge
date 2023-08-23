letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Soumya"

print(letter.format(name,country))
print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")
price = 49.099999
txt = f"For only {price} dollars"
print(txt)
txt = f"For only {price:.3f} dollars"
print(txt)
print(f"{2*30}")
