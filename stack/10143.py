from collections import deque

def throwing_cards(n):
    deck = deque(range(1, n + 1))
    discarded = []
    while len(deck) > 1:
        discarded.append(deck.popleft())
        deck.append(deck.popleft())
    return discarded + [deck[0]]

def main():
    n = int(input())
    result = throwing_cards(n)
    print(*result)

if __name__ == "__main__":
    main()
