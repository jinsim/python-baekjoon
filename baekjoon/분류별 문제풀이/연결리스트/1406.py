# 연결 리스트로 풀지 말자...
"""
리스트와 덱을 섞어서 사용한 풀이가 제일 편했다. 
커서를 기준으로 left, right를 나누고,
명령에 따라 옮기거나 빼준 후 마지막에 합치면 된다.
"""
# 연결 리스트를 이용한 풀이 
import sys
input = sys.stdin.readline

class ListNode:
    prev = next = None

    def __init__(self, val):
        self.val = val

class LinkedList:
    def __init__(self, node):
        self.head = self.cur = node

    def print_all(self):
        self.cur = self.head
        res = ''
        while self.cur:
            res += self.cur.val
            self.cur = self.cur.next
        print(res)

    def left(self):
        if self.cur:
            self.cur = self.cur.prev

    def right(self):
        if not self.cur:
            self.cur = self.head
        elif self.cur.next:
            self.cur = self.cur.next

    def insert(self, node):
        if self.cur:
            node.next = self.cur.next
            node.prev = self.cur
            if node.next:
                node.next.prev = node
            self.cur.next = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.cur = node

    def delete(self):
        if self.cur:
            if self.cur.next:
                self.cur.next.prev = self.cur.prev
            if self.cur.prev:
                self.cur.prev.next = self.cur.next
            else:
                self.head = self.cur.next
            self.cur = self.cur.prev

n = input().rstrip()
l = LinkedList(ListNode(n[0]))
for i in n[1:]:
    l.insert(ListNode(i))

for _ in range(int(input())):
    cmd = input().rstrip()
    if cmd == 'L':
        l.left()
    elif cmd == 'D':
        l.right()
    elif cmd == 'B':
        l.delete()
    elif cmd[0] == 'P':
        node = ListNode(cmd[-1])
        l.insert(node)

l.print_all()


# 리스트와 덱을 사용한 풀이
import sys
from collections import deque
input = sys.stdin.readline

left = deque(input().rstrip())
right = deque()

for _ in range(int(input())):
    cmd=input().rstrip()
    if cmd=="L":
        if left:
            right.appendleft(left.pop())
    elif cmd=="D":
        if right:
            left.append(right.popleft())
    elif cmd=="B":
        if left:
            left.pop()
    elif cmd[0] == 'P' :
        left.append(cmd[-1])

left.extend(right)
print(''.join(left))