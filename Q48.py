class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def build_list(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out


def reverse_list(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    print(to_list(head))               # [1,2,3,4,5]
    print(to_list(reverse_list(head)))  # [5,4,3,2,1]
