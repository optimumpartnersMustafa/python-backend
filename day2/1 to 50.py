def dev():
    for i in range(1, 51):
        if (i % 3 != 0 and i % 5 != 0):
            print(str(i) + " ") 

if __name__ == "__main__":
    dev()