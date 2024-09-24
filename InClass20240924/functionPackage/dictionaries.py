# dictionaries.py


def demo():
    """
    demonstrate basic disctionary stuff
    """
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)

    #iterate over the dictionary by key
    for key in myDictionary.keys():
        print(key)

    #iterate by key/value
    for item in myDictionary.items():
        print(item)
    
    for value in myDictionary.values():
        print(value)

    #add a key/value pair
    myDictionary["Michigan State"] = "Spartans"
    print(len(myDictionary))

    #Cause an exception add try except logic to
    #Gracefully handle this
    try:
        print(myDictionary["Ohio State"])
    except:
        print("Ohio State is an invalid key")

    #remove xavier by key and print the entire dictionary

    myDictionary.pop("Xavier")

    print(myDictionary)

    # Create another dictionary called newTeams
    #Add several key value pairs
    #combine that with myDictionary and print results
    newTeams = {"Ohio State":"Buckeyes", "Indiana":"Hoosiers", "Purdue":"Boilermakers","Cincinnati":"Bearcats"}
    myDictionary.update(newTeams)
    print(myDictionary)
