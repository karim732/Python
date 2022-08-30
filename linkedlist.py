class node:

    def __init__(self,data):
        self.data=data
        self.next=None

'''class link:

    def __init__(self):
         self.head=None

    # Code execution starts here


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = link()

    llist.head = node(1)
    second = node(2)
    third = node(3)

    llist.head.next = second
    second.next = third

    p = llist.head
    while p != None:
        print(p.data)
        p = p.next'''






head = node(1)

second= node(5)
third = node(7)
four = node(6)
five = node(4)
six = node(3)
seven = node(2)


head.next=second
second.next=third
third.next=four
four.next=five
five.next=six
six.next=seven

#Add an Element at End

'''nele = int(input("enter element to add at end"))

new = node(nele)

n=head
while True:
    if n.next == None:
        n.next = new
        break
    n=n.next


p=head
while p!=None:
    print(p.data)
    p=p.next '''

#Add an Element at middle

'''nele = int(input("enter element to add "))
pos = int(input("enter position "))

s=1

new = node(nele)

n=head
while True:
    s = s + 1
    if s == pos:
        new.next = n.next
        n.next = new

        break
    n=n.next




p=head
while p!=None:
    print(p.data)
    p=p.next '''

# Add an element at Begining

'''nele = int(input("enter element to add at start "))


new = node(nele)

new.next = head

head =new


p=head
while p!=None:
    print(p.data)
    p=p.next'''

#Count Number of Elements

'''s=0

p=head

while p!=None:
    s=s+1
    p=p.next

print("number of elements : ",s )'''

# search an element

'''fele = int(input("enter element to find"))

p=head
s=0

while p!=None:
    s=s+1
    if p.data == fele:
        break
    p=p.next

print(fele," element found at : ",s," position")'''


# Delete an end element

'''print("deletion of an element")

p=head

while p.next.next != None:
    p=p.next
p.next = None


p=head
while p!=None:
    print(p.data)
    p=p.next'''

p=head
while p!=None:
    print(p.data)
    p=p.next

# Sorting the list

'''f,t = head,head
while f!=None:
    t=f.next
    while t!=None:
        if f.data > t.data:
            f.data,t.data = t.data,f.data

        t=t.next

    f= f.next


p=head
while p!=None:
    print(p.data)
    p=p.next'''



p=head
while p!=None:
    print(p.data)
    p=p.next










