# dictionaries.py
# This was really fun and I will treasure this time together with my peers.

from os import remove


def demo():
    """
    Demonstrate basi disctionary stuff
    """
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
    
    # Iterate over the dictionary by key
    for key in myDictionary.keys():
        print(key)
    
    # Iternate by value
    for item in myDictionary.items():
        print(item)
        
    #Iternate by value
    for value in myDictionary.values():
        print(value)
        
    # Add a key/alue vpair to the dictionary
    myDictionary['Michigan State'] = "Spartans"    

    print(len(myDictionary))

    # Cause an exception.
    # gracefully handle this
    try:
        print(myDictionary["Ohio State"])
    except:
        # We end up here if an exception is thrown in the try block
        print("Ohio State is an invalid key")
    
    # Remove Xavier by key and print the entire dictionary
    myDictionary.pop('Xavier')
    print(myDictionary)
    
    # Create another dictionary called newTeams.
    # Add several key/value pairs
    # Combine that with myDictionary and print the results
    newTeams = {"McLaren":"Norris", "Red Bull":"Verstappen", "Ferrari":"Leclerc"}
    myDictionary.update(newTeams)
    print(myDictionary)