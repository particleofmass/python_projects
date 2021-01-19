toop = ('a', 'e', 'i', 'o', 'u')
'''ae, bee, sea, dee = toop - gives an error as there aren't as many variables
on the left side as there are on the left side.'''
ae, bee, sea, dee, ew = toop
print(ae, bee, sea, dee, ew, ' - did not discard any values')
#The above statement would work due to same number of values and variables
one, _, three, _, five = toop
print(one, three, five, ' - discarded some values')
'''This can be used if you want to throw away some values with some throw away
variables'''


