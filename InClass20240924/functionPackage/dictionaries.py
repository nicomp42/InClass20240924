# dictionaries.py

def demo():
    """
    Demonstrate basic dictionary stuff
    """
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
    
    # Iterate over the dictionary by key (How to step through the keys one at a time)
    for key in myDictionary.keys():
        print(key)
    # Iterate by key/value
    for item in myDictionary.items():
        print(item)
    
    # Iterate by value
    for value in myDictionary.values():
        print(value)
        
    # Add a key/value pair to the dictionary
    myDictionary["Michigan State"] = "Spartans"
    
    print(len(myDictionary)) # Use breakpoint and debuger, and hover over the function to see if it was added
    
    # Cause an exception. Add the try/except logic to gracefully handle this
    try:
        print(myDictionary["Ohio State"])
    except:
        # We end up here if an exception is thrown
        # in the try block
        print("Ohio State is an invalid key")
        
    # Remove Xavier by key and print the entire dictionary
    myDictionary.pop("Xavier")
    print(myDictionary)
    
    # Create another dictionary called newTeams.
    # Add several key/value pairs
    # Combine that with my dictionary and print the results
    newTeams = {"Akron": "Zips",
                "Kentucky": "Wildcats",
                "Michigan": "Wolverines",
                "Minnesota": "Golden Gophers"}
    # Brute force/Inelegant way
        # for key in newTeams.keys():
            # myDictionary[key] = newTeams[key]
    # Better way
    myDictionary.update(newTeams)
    print(myDictionary)
    