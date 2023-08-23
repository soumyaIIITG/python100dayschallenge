crushes=["Anushmita","Nishtha","Ria","Sanjana"]
for crush in crushes:
    if (crush=="Nishtha"):
        continue
    print(crush)
print("The next loop starts here")
for crush in crushes:
    if (crush=="Nishtha"):
        break
    print(crush)