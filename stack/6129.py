from collections import deque
import sys

def main():
    q = deque()
    for line in sys.stdin:
        command = line.strip().split()
        if command[0] == "push_back":
            q.append(command[1])
        elif command[0] == "push_front":
            q.appendleft(command[1])
        elif command[0] == "pop_back":
            print(q.pop() if q else "error")
        elif command[0] == "pop_front":
            print(q.popleft() if q else "error")
        elif command[0] == "front":
            print(q[0] if q else "error")
        elif command[0] == "back":
            print(q[-1] if q else "error")
