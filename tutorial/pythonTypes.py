def add(firstName: str | None,lastName:str=None):
    if (firstName!=None):
        firstName.capitalize()

    return firstName+" "+lastName
first=None
last="Gates"
print(add(first,last))