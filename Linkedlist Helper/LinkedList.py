class linkedlist:
    def __init__(self,val):
        self.val = val
        self.next = None

class linkedlist_double:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

#singly linked list
def singly_linkedlist(arr):
    for i in range(len(arr)):
        if i==0:
            head = linkedlist(arr[i])
            current = head
        else:
            current.next = linkedlist(arr[i])
            current = current.next
    return head

#circular singly linked list
def circular_singly_linkedlist(arr):
    for i in range(len(arr)):
        if i==0:
            head = linkedlist(arr[i])
            current = head
        else:
            current.next = linkedlist(arr[i])
            current = current.next
        if i==len(arr)-1:
            current.next = head
    return head

#doubly linked list
def doubly_linkedlist(arr):
    for i in range(len(arr)):
        if i==0:
            head = linkedlist_double(arr[i])
            current = head
        else:
            next_current = linkedlist_double(arr[i])
            current.next = next_current
            next_current.prev = current
            current = next_current
    return head

#circular doubly linked list
def circular_doubly_linkedlist(arr):
    for i in range(len(arr)):
        if i==0:
            head = linkedlist_double(arr[i])
            current = head
        else:
            next_current = linkedlist_double(arr[i])
            current.next = next_current
            next_current.prev = current
            current = next_current
        if i==len(arr)-1:
            current.next = head
            head.prev = current
    return head

#displaying a singly and doubly linked lists
def display_linkedlist(head):
    cur = pointer = head
    while pointer.next and cur != pointer.next:
        print(pointer.val, end=" -> ")
        pointer = pointer.next
    print(pointer.val, end=" ")


def lpush(head,input_val,is_circular = False,is_doubly = False):
    if head:
        if not is_doubly:
            ptr = current = head
            while current.next and current.next!=head:
                current = current.next
            if not is_circular:
                current.next = linkedlist(input_val)

            elif is_circular:
                current.next = linkedlist(input_val)
                current.next.next = ptr
        elif is_doubly:
            current = head
            ptr = head
            while current.next and current.next!=head:
                current = current.next

            if not is_circular:
                current.next = linkedlist_double(input_val)
                current.next.prev = current
            elif is_circular:
                current.next = linkedlist_double(input_val)
                current.next.prev = current
                current = current.next
                current.next = ptr
                ptr.prev = current
    else:
        if is_doubly:
            head = linkedlist_double(input_val)
        else:
            head = linkedlist(input_val)

    return head

def lpop(head,input_val,is_circular = False,is_doubly = False):

    if head:
        if not is_doubly:
            current = head
            ptr = head
            while current.next and current.next!=head:
                ptr = current
                current = current.next
            if not is_circular:
                ptr.next = None

            elif is_circular:
                ptr.next = head
                
        elif is_doubly:
            ptr = head
            current = head
            while current.next and current.next!=head:
                ptr = current
                current = current.next

            if not is_circular:
                ptr.next = None
                
            elif is_circular:
                ptr.next = head
                head.prev = ptr
    else:
        print("Element not present in the list")
        return None

#To delete a node by giving a value
def ldelete(head, input_val, is_circular=False, is_doubly=False):
    
    if head is None:
        print("Element not present in the list")
        return None

    if head.val == input_val:
        
        if head.next:
            head.val = head.next.val
            head.next = head.next.next
            if is_circular:
             
                temp = head
                while temp.next != head:
                    temp = temp.next
                temp.next = head.next
                head.next.prev = temp
                head.next = None
            if is_doubly:
                head.prev = None
            return head
        else:
            return None

    current = head
    ptr = head

    while current and current.val != input_val:
        ptr = current
        current = current.next

    if current:

        if not is_doubly and not is_circular:
            if current.next:
                current.val = current.next.val
                if current.next.next:
                    current.next = current.next.next
                else:
                    current.next = None
            else:
                ptr.next = None

        elif is_doubly and not is_circular:
            if current.next:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
            else:
                ptr.next = None

        elif not is_doubly and is_circular:
            ptr.next = current.next

        elif is_doubly and is_circular:
            ptr.next = current.next
            current.next.prev = ptr
            

        return head
    else:
        print("Element not present in the list")
        return None


def lsort(head,is_circular = False,is_doubly = False,is_reverse = False):
    if head:
        lis = []
        current = head
        ptr = head
        typ = type(current.val)
        while current and current.next!=head:
            if typ != type(current.val):
                print("cannot be sorted due to datatype change")
                return -1
            lis.append(current.val)
            current = current.next

        if is_circular and current.next==head:
            lis.append(current.val)

        if is_reverse:
            lis = sorted(lis,reverse = True)
        else:
            lis = sorted(lis)

        if not is_doubly and not is_circular:
            return singly_linkedlist(lis)
        elif not is_doubly and is_circular:
            return circular_singly_linkedlist(lis)
        elif is_doubly and not is_circular:
            return doubly_linkedlist(lis)
        elif is_doubly and is_circular:
            return circular_doubly_linkedlist(lis)
    else:
        print("No elements found")
        return None


    
#reversing a singly, doubly, circular singly and circular doubly linked lists
def lreverse(head,is_circular = False,is_doubly = False):
    
    if not head.next:
        return head

    if not is_doubly:
        temp = None
        current = head
        flag = True
        while current:
            if flag:
                ptr = current
                flag = False
            next_current = current.next
            current.next = temp
            temp = current
            current = next_current

        if is_circular:
            ptr.next = temp.next
            return temp.next
            
    elif is_doubly:
        temp = None
        current = head
        flag = True
        while current:
            if flag:
                ptr = current
                flag = False
            next_node = current.next
            current.next = temp
            current.prev = next_node
            temp = current
            current = next_node
        
        if is_circular:
            temp.next.prev = ptr
            ptr.next = temp.next
            return temp.next

    return temp

    
#To find whether the value is in linked list and return its index else None
def lfind(head,input_val):
    cur = pointer = head
    i = 0
    while pointer.next and cur != pointer.next:
        if pointer.val==input_val:
            return i
        pointer = pointer.next
        i+=1
    if pointer.val==input_val:
        return i

    return None

#to drop the linked list
def ldrop(head):
    return None
