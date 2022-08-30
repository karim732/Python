class node:
    def __init__(self,data):
        self.pre=None
        self.data = data
        self.next = None


head = node(1)
second = node(2)
third = node(3)

head.pre=third
head.next = second
second.pre = head
second.next = third
third.pre = second
third.next = head


print(head.pre)
print(head.data)
print(head.next)
print(second.pre)
print(second.data)
print(second.next)
print(third.pre)
print(third.data)
print(third.next)







