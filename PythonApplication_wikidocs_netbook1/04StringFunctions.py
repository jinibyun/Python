# count for some character
a = "HobbY"
print(a.count('b'))

# find: case sensitve
print(a.find('Y'))
print(a.find('x'))
print(a.index('Y'))
# print(a.index('x')) # difference between find and IndexError


# join
j = ","
print(j.join('abce'))

#split. It returns list which is same as array
sp = "Life is too short"
print(sp.split()) # default: by space

sp1 = "a:b:c:d"
print(sp1.split(':'))

# upper, lower
print("hi".upper())
print("HI".lower())

#strip
print("    strip".lstrip())
print("strip    ".rstrip())
print("    strip    ".strip())

#replace
re = "Life is too short"
print(re.replace("Life", "Your leg"))

#format :using format() is better than %...
print("I eat {0} apples".format(4))
print("I eat {0} apples".format("four"))
print("I ate {0} apples. so I was sick for {1} days".format(1, 5))
print("I ate {number} apples. so I was sick for {day} days".format(number = 1, day = 5))

# align
print("{0:<10}".format("hisdfsdfsdfsdfsdf")) #: :< left alignment
print("{0:>10}".format("hi")) # :> right alignment
print("{0:^10}".format("hi")) #: ^ middle alignment

# fill space
print("{0:=^10}".format("hi")) # 채워 넣을 문자 값은 정렬 문자인 <, >, ^ 바로 앞에 넣어야 한다.
print("{0:!<10}".format("hi")) # 왼쪽(<)으로 정렬하고 빈 공간을 !문자로 채웠다.

#precision
print("{0:0.4f}".format(3.42134234)) # format 함수를 이용해 소수점을 4자리까지만 표현
print("{0:10.4f}".format(3.42134234))

#{}
print("{{ and }}".format())