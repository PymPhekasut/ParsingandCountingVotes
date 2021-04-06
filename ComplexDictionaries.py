units = {
    ('301046','Big Data'): 'MICT',
    ('300581', 'Programming Techniques'): 'BICT',
    ('300144', 'OOA'): 'BICT',
    ('300103', 'Data Structures'): 'BCS',
    ('300147', 'OOP'):'BCS',
    ('300569', 'Computer Security'): 'BIS',
    ('301044', 'Data Science'): 'MICT',
    ('300582', 'TWA'): 'BICT'
}


def display_units(units, keywords):
    listOfUnits = list()
    listOfItems = units.items()
    for item  in listOfItems:
        if item[1] in keywords:
            listOfUnits.append(item[0])
    return  listOfUnits 


listOfUnits = display_units(units, ['MICT'] )

for key  in listOfUnits:
    print(key)



# the function below should display all MICT units
# 301046 Big Data
# 301044 Data Science
display_units(units, 'MICT')
# the function below should display all BCS units
# 300103 Data Structure
# 300147 OOP
display_units(units, 'BCS')
