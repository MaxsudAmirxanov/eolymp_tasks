def burn_time(message):
    important_part = message.find('!')
    if important_part == -1:
        return -1
    return important_part + 1

def main():
    message = input().strip()
    print(burn_time(message))

if __name__ == "__main__":
    main()
