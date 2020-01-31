# pickle: keeping "object" itself, save and read to and from a file

import pickle

# 1. save
f= open("test.txt", 'wb')
data = {1: "python", 2: "you need"}

pickle.dump(data ,f)
f.close()

# 2. retrieve
f = open("test.txt", "rb")
data = pickle.load(f)
f.close()

print(data)