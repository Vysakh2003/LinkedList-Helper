from LinkedList import *

print("\n--------------------------------------------")
print("DISPLAYING RESULTS OF \"LinkedList\".py MODULE")
print("--------------------------------------------\n")

print("\nSINGLY LINKED LIST : ",end="")
arr = [1,2,3,4,5]
head = singly_linkedlist(arr)
display_linkedlist(head)
print("\n")

print("\nCIRCULAR SINGLY LINKED LIST : ",end="")
arr = [6,7,8,9,10]
head = circular_singly_linkedlist(arr)
display_circular_linkedlist(head)
print("\n")

print("\nDOUBLY LINKED LIST : ",end="")
arr = [11,12,13,14,15]
head = doubly_linkedlist(arr)
display_linkedlist(head)
print("\n")

print("\nCIRCULAR DOUBLY LINKED LIST : ",end="")
arr = [16,17,18,19,20]
head = circular_doubly_linkedlist(arr)
display_circular_linkedlist(head)
print("\n")
