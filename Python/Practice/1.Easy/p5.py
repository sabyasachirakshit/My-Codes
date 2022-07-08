def relation_to_luke(str):
    if str.title() == "Darth Vader":
        return "Luke, I am your father."
    elif str.title() == "Leia":
        return "Luke, I am your sister."
    elif str.title() == "Han":
        return "Luke, I am your brother in law."
    elif str.title() == "R2D2":
        return "Droid"


print(relation_to_luke("Darth Vader"))
print(relation_to_luke("Leia"))
print(relation_to_luke("Han"))
