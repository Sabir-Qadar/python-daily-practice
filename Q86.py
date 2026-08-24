from collections import deque


class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft() if self.q1 else None

    def top(self):
        return self.q1[0] if self.q1 else None

    def is_empty(self):
        return not self.q1


if __name__ == "__main__":
    s = StackUsingQueues()
    for v in (1, 2, 3):
        s.push(v)
    print(s.pop())  # 3
    print(s.top())  # 2
