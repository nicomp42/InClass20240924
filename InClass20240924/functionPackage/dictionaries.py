# dictionaries.py
# This was really fun and I will treasure this time together with my peers

from audioop import add
from re import X
from turtle import update


def demo():
    '''

    Demonstrate basic dictionary stuff
    '''

    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)


    # Iterate over the dictionary by key
    for key in myDictionary.keys():
        print(key)


    # Iterate by key/value
    for item in myDictionary.items():
        print(item)


    # iterate by value
    for value in myDictionary.values():
        print(value)


    # Add a key/value pair to the dictionary
    myDictionary['Michigan State'] = 'Spartans'
    print(len(myDictionary))


    # Cause an exception. Add the try/except to handle this
    try:
        print(myDictionary['Ohio State'])
    except:
        # End up here if exception is thrown in the try block
        print('Ohio State is an invalid key')


    # Remove Xavier by key and print the entire dictionary
    myDictionary.pop('Xavier')
    print(myDictionary)


    # Create another dictionary called newTeams
    # Add several key/value pairs 
    # Combien that with myDictionary and print the results
    myDictionary02 =  {"Iowa":"Hawkeyes", "Miami":"Hurricanes", "Florda":"Gators", "USC":"Trojans"}
    myDictionary.update(myDictionary02)
    print (myDictionary)

    '''
    # Brute force
    for key in myDictionary02.keys():
        myDictionary[key] = myDictionary02[key]
    print(myDictionary)
    '''
    
