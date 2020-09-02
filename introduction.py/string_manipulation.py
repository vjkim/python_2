# Concatenation ==> glues strings together

"Hello, " + "Nick"
'Hello, Nick'
# adds hello, and nick together.


 "This costs " + 6 "bucks"
  File "<string>", line 1
    "This costs " + 6 "bucks"
                            ^
SyntaxError: invalid syntax
# This is incorrect because it doesnt know what to do with the bucks and the quotation


"This costs " + str(6) + "dollars"
'This costs 6dollars'
# This is the correct way to word this

"This costs " + str(6 + 5) + " dollars"
'This costs 11 dollars'
#Converts the numbers into strings then adds it


"Hello:Nick"
'Hello:Nick'


"Hello:Nick".split(":")
['Hello', 'Nick']

#Splitting strings apart into two items in the array

"My name is " + "Hello:Nick:World".split(":")[1]
'My name is Nick'

# splits them into arrays, programming starts at 0, not 1


