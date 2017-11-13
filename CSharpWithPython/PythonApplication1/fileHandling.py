print ("-----Create, open and write -------")
f = open("C:/Jini/pythonTest.txt", "w")
for i in range(1, 11):
    data = "%d th line \n" % i
    f.write(data)

f.close()

# 1
print ("-------1----------")
f = open("C:/Jini/pythonTest.txt", 'r')

while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 2
print ("-------2----------")
f = open("C:/Jini/pythonTest.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

print ("-------3----------")
f = open("C:/Jini/pythonTest.txt", 'r')
data = f.read()
print(data)
f.close()

print ("----- Append text to file -------")
f = open("C:/Jini/pythonTest.txt",'a') # NOTE: do not open file w mode.
for i in range(11, 20):
    data = "%d line.\n" % i
    f.write(data)
f.close()


print ("---- automatic open and close file -----") # with keyword
with open("C:/Jini/pythonTest2.txt", "w") as f:
    f.write("Life is too short, you need python")