import random

random.random() # between 0.0 and 1.0

random.randint(1, 10) # between 1 and 9

def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

# same as above
def random_pop2(data):
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__": # when this module is executed from outside (python xxx.py), it gets true, but when this module is reference (import xxx), then it gets false
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))


# shuffle
data = [1,3,5,7,9]
random.shuffle(data)
print(data)