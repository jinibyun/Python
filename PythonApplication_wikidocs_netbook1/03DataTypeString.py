food = "Python's favorite food is perl...."

print(food)

print("===== how to include \" (double quotation) =====")
a = '"Python is veray easy" he says...'
print(a)

print("===== using escape code =====")
b = "Python\'s favorite food is perl..."
print(b)
    
print("===== multiline 1 =====")
multiline = "Life is too short\nYou need python"
print(multiline)

# multiline 2: neater that multiline 1
multiline2 = """
    dfssdfsdf
    fs
    tghjhghggfjgfj
    """
print(multiline2)    

print("===== Concatenation =====")
head = "Python"
tail = " is fun"
print(head + tail)

print("=====string multiply =====")
s1 = "python"
print(s1 * 2)

print("===== indexing =====")
index1 = "Life is too short, You need Python"
print(index1[0] + index1[1] + index1[2] + index1[3])
print(index1[-1] + index1[-2] + index1[-3] + index1[-4])

print("===== slicing =====")
slicing1 = "Life is too short, You need Python"
print(slicing1[0:4])
print(slicing1[19:]) # don't forget :
print(slicing1[:17]) # don't forget :
print(slicing1[19:-7]) # - can be used
print(slicing1[8:11])
# slicing 2
slicing2 = "20010331Rainy"
date = slicing2[:8]
weather = slicing2[8:]
print(date + " " + weather)

print("===== formatting =====")
format1 = "I eat %d apples." % 3
print(format1)

format2= "I eat %s apples." % "five"
print(format2)

format3 = "I ate %d apples so I was sick for %s days." %(3, "six")
print(format3)

# %s 는 어떤 형태의 코드도 허용

# note: %를 표시할 때는 % 를 두번 적어준다.
format4= "Error is %d%%" %98
print(format4)

# formating with number: more useful
print("%10s" % "hi") # 10 spaces and align right
print("%0.4f" % 3.42123234 ) # float precision up to 4
print("%10.4f" % 3.42123234) #  float precision up to 4 and change string and 10 spaces and align right
