class ListNode(object):
    def __init__(self, val=0):
        self.val = val

list = ListNode()
print(list.val)

list.value = list.val if list == None else 1
print(list.value)

list.value = 2
print(list.value)