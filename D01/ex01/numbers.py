def read_file():
    with open('numbers.txt') as f:
        for number in f.read().split(","):
            print(number)
    f.closed
    
if __name__ == '__main__':
    read_file()