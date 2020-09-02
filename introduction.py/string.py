#anything you want to be treated as text

"Hello Strings"
'hello'

# can have double or single quotes

 'Don't do that
  File "<string>", line 1
    'Don't do that
         ^
SyntaxError: invalid syntax
# the system will freak out because it doesnt know what to do 

she said " i want this "
  File "<string>", line 1
    she said " i want this "
           ^
SyntaxError: invalid syntax

# the system will freak out again because it doesnt know how to treat the quotations

"she said " i want this"
  File "<string>", line 1
    "she said " i want this"
                ^
SyntaxError: invalid syntax

'She said "I want this"'
'She said "I want this"'
# this is the right syntax because there are quotes for both the quotation and the "she said"


'She said "Don't put that there"'
  File "<string>", line 1
    'She said "Don't put that there"'
                   ^
SyntaxError: invalid syntax
# Doesnt know what to do with the last few characters

print('She said "Don\'t Do that"')
She said "Don't Do that"
#printed out as a character