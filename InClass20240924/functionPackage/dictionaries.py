# dictionaries.py

# This was really fun and I will treasure this time together
# with my peers 

def demo():
    """
    Demonstrate basic dictionary stuff
    """
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)

    # Iterate over the dictionary by key
    for key in myDictionary.keys(): # keys() is a method from the dictionary class, returns the key without quotations
        print(key)

    # Iterate by value
    for item in myDictionary.items(): # items() is a method from the dictionary class, returns the items with parenthesis and single quotes
        print(item)

    # Iterate by value
    for value in myDictionary.values(): # values() is a method from the dictionary class, returns the values without quotes
        print(value)

    # Add a key/value pair to the dictionary
    myDictionary["Michigan State"] = "Spartans"

    print(len(myDictionary))

    # Cause an exception. Add try/ except logic to
    # gracefully handle this
    try: 
        print(myDictionary["Ohio State"])
    except:
        # We end up here if an exception is thrown
        # in the try block
        print("**** Ohio State is an invalid key ****")
    
    # Remove Xavier by key and print the entire dictionary
    myDictionary.pop("Xavier")
    print(myDictionary)

    # Create another dictionary called newTeams
    # Add several key/value pair
    # Comvibine that with myDictionary and print the results
    newTeams = {"Michigan State":"Spartans", 
                "UCLA":"Bruins", 
                "Purdue":"Boilermakers", 
                "Dayton":"Flyers", 
                "Korea University":"Tigers"}
    #myDictionary.update(newTeams) # Will not include duplicate Michigan State key/value
    # Other ways:
    # combined_dict = newTeams | my Dictionary
    # combined_dict = (**newTeams, **myDictionary)

    #Brute force combination // Inelegant :( Avoid
    for key in newTeams.keys():
        myDictionary[key] = newTeams[key]
    print(myDictionary)


