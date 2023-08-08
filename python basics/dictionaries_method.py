# CLEAR

cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004"

}
cars.clear()
print(cars)

# COPY METHOD

cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004"

}
copy_method = cars.copy()
print(copy_method)

# FROMKEYS

fruits = {
    'mango' , 'apple' , 'banana'
}
rangee = 1
thisdict = dict.fromkeys(fruits , rangee)
print(thisdict)

cities = {
    'lahore' , 'karachi' , 'faislabad' , 'multan'
}
transports = 2
sorting = dict.fromkeys(cities , transports)
print(sorting)

# GET_METHOD

cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004"

}
thisdict = cars.get( 'model') #only one argument
print(thisdict)


cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004"

}
thisdict = cars.get('color' , 'blue' )
print(thisdict)

# ITEMS

cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004"

}
thisdict = cars.items()
print(thisdict)

cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004"

}
thisdict = cars.items()
cars['model'] = 2018
print(thisdict)

# KEYS

cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004"

}
thisdict = cars.keys()
print(thisdict)


cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004"

}
thisdict = cars.keys()
cars['color'] = 'white'  #for adding the keys
print(thisdict)

# POP_METHOD

cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004"

}
cars.pop('model') #takes only one argument
print(cars)

# POP_ITEM removes the last element

cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004" ,
     "brand" : "BMW" ,
     "model" : "any" 

}
cars.popitem() 
print(cars)

# SET-DEFAULT

cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004" 

}
thisdict = cars.setdefault('year')
print (thisdict)


cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004" ,
     'engine': ''
}
thisdict = cars.setdefault('engine'  , '234')
print (thisdict)

# UPDATE

cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004" ,
     'engine': 'none'
}
cars.update({'color' : 'white' , 'speed' : '120perkm'})
print(cars)

# VALUES return the key values 

cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004" ,
     'engine': 'none'
}

thisdict = cars.values()
print(thisdict)

# for updating

cars = {
     "brand" : "BMW" ,
     "model" : "any" ,
     "year"  : "2004" ,
     'engine': 'none'
}

thisdict = cars.values()
cars['year'] = 9473
print(thisdict)

test = 123
print(f"We want to prin {test}")

