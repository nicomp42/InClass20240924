# dictionaries.py
# this was real fun and i will treasure this time together with my peers

def demo():
    """
    Demonstrate basic dicitionary  stuff
    """
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
    
    # iterate over the dicitionary by key
    for key in myDictionary.keys():
        print(key)

    # iterate by key/value
    for item in myDictionary.items():
        print(item)
        
    # iterate by value
    for value in myDictionary.values():
        print(value)
        
    # add a key/value pair to the dictionary
    myDictionary["Michigan State"] = "Spartans"    
    print(len(myDictionary))
    
    # casue an exception.add a try/ expect logic to
    # gracefuly handle this
    try:
        print(myDictionary["Ohio State"])
    except :
        # we end up here if an excpetion is throuwn
        # in the try block
        print("Ohio State is an invalid key")
        
    # remove Xavier by key and print the entrie dictionary
    myDictionary.pop("Xavier")
    print(myDictionary)
    
    # create another dictionary 
    # add sevreal key/value pairs
    # combine that mith mydictionary and print the results 
    
    newTeams = {"Indiana" :"Hoosiers", "Hillsdale":" Chargers", "Teledo":"Rockets"}
    
    """
    # Brute force
    for key in newTeams.key():
        myDictionary[key] = newTeams[key]
        print(myDictionary)
    """
    
    myDictionary.update(newTeams)
    print(myDictionary)