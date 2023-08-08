# ADD

maths = {'trignometry' , 'calculus' , 'differentiation' , 'integration'}
maths.add('vectors')
print(maths)

# CLEAR

maths = {'trignometry' , 'calculus' , 'differentiation' , 'integration'}
maths.clear()

#COPY

maths = {'trignometry' , 'calculus' , 'differentiation' , 'integration'}
this_maths = maths.copy()
print(this_maths)

# DIFFERENCE

maths = {'trignometry' , 'calculus' , 'differentiation' , 'integration'}
bscs = { 'calculus' , 'differentiation' , 'discrete' , 'programming'}
differ = bscs.difference(maths)
print(differ)

# DIFFERENCE_UPDATE (remove the item that exists in both sets)

maths = {'trignometry' , 'calculus' , 'differentiation' , 'integration'}
bscs = { 'calculus' , 'differentiation' , 'discrete' , 'programming'}
maths.difference_update(bscs)
print(maths)


#DISCARD

maths = {'trignometry' , 'calculus' , 'differentiation' , 'integration'}
bscs = { 'calculus' , 'differentiation' , 'discrete' , 'programming'}
maths.discard('')
print(maths)

#intersection (elements which are common)

maths = {'trignometry' , 'calculus' , 'differentiation' , 'integration'}
bscs = { 'calculus' , 'differentiation' , 'discrete' , 'programming'}
bscs_degree = maths.intersection(bscs)
print(bscs_degree)

#intersection_update (remove which are not in common)

maths = {'trignometry' , 'calculus' , 'differentiation' , 'integration'}
bscs = { 'calculus' , 'differentiation' , 'discrete' , 'programming'}
bscs.intersection_update(maths)
print(bscs)

#remove (remove a specefic element)

bscs = { 'calculus' , 'differentiation' , 'discrete' , 'programming'}
bscs.remove('calculus')
print(bscs)

# UPDATE (adding all the elements from the other set)

maths = {'trignometry' , 'calculus' , 'differentiation' , 'integration'}
bscs = { 'calculus' , 'differentiation' , 'discrete' , 'programming'}
z=maths.update(bscs)
print(z)

fruits = {'apple', 'banana', 'orange'}
additional_fruits = ['grape', 'kiwi']

fruits.update(additional_fruits)
print(fruits)  # Output: {'apple', 'banana', 'orange', 'grape', 'kiwi'}

# UNION (union all the sets without duplication)

