from LinkedList import *

a = [1,2,3,4,5,9,7,8,6]

c = singly_linkedlist(a)
b = circular_singly_linkedlist(a)
d = doubly_linkedlist(a)
e = circular_doubly_linkedlist(a)

display_linkedlist(b)
print()
display_linkedlist(c)
print()
display_linkedlist(d)
print()
display_linkedlist(e)
print()
c = lreverse(c)
b = lreverse(b,is_circular = True)
d = lreverse(d)
e = lreverse(e,is_circular = True,is_doubly = True)
print()
display_linkedlist(c)
print()
display_linkedlist(b)
print()
display_linkedlist(d)
print()
display_linkedlist(e)
print()
print()
ind = lfind(c,0)
print(ind)


b = lsort(e,is_circular = True,is_doubly = True)
print()
display_linkedlist(b)
