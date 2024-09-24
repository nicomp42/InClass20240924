# dictionaries.py
# This was really fun and I will treasure this time to together
# with my peers.

def demo():
    """
    Demostrate vasic dictionary stuff
    """
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)

    # Iterate over the dictionary by key
    for key in myDictionary.keys():
        print(key)
    # Iterate by key/value
    for item in myDictionary.items():
        print(item)

        # Iterate by value
    for value in myDictionary.values():
        print(value)

    # add a key/value pair to the dictionary
    myDictionary["Michigan State"] = "Spartans"

    print(len(myDictionary))
    
    # Cause an exception. Add try/except logic
    # gracefully handle this
    
    try:
        print(myDictionary["Ohio State"])
    except:
        print("Ohio State is an invalid key")
         # remove XAvier by key and print the entire dictionary
    myDictionary.pop("Xavier")
    print(myDictionary)

    # Create another dictory called newTeams
    # Add several key/Value pairs
    # Combine that with myDictonary and print the results

    newTeams = {"Indiana":"Hoosiers", "Hillsdale":"Chargers", "Toledo":"Rockets"}

    # Brute fource
   #for key in newTeams.keys():
       # myDictionary[key]= newTeams[key]
    
    myDictionary.update(newTeams)
    print(myDictionary)
   
  


