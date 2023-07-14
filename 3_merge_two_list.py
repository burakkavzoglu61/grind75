from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_node(node, val):
    new_node = ListNode(val)

    if node == None:
        return new_node

    cur = node
    while cur.next != None:
        cur = cur.next
    cur.next = new_node
    return node


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]):
    result = None

    while list1 != None or list2 != None:
        if not list1:
            result = add_node(result, list2.val)
            list2 = list2.next
        elif not list2:
            result = add_node(result, list1.val)
            list1 = list1.next
        else:
            if list1.val < list2.val:
                result = add_node(result, list1.val)
                list1 = list1.next
            else:
                result = add_node(result, list2.val)
                list2 = list2.next

    return result


# testing
first = ListNode(3)
first.next = ListNode(5)
first.next.next = ListNode(8)

second = ListNode(4)
second.next = ListNode(6)
second.next.next = ListNode(7)

result = mergeTwoLists(first, second)

while result !=None:
    print(result.val)
    result = result.next
