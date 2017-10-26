print("===== list type example =====")
a = [ ] # empty list: a = list() 로도 생성 할 수 있다.
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is'] # contain any type
e = [1, 2, ['Life', 'is']] # contain another list


print(b[2])

f = [1, 2, 3, ['a', 'b', 'c']]
print(f[-1]) # -1: last index
print(f[3])
print(f[-1][2])

g = [1, 2, ['a', 'b', ['Life', 'is']]]
print(g[2][2][0])

print("===== list slicing =====") # same as string slicing
h = [1,2,3,4,5]
print(h[0:2])

a1  = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a1[2:4])
print(a1[3][:2])

print("===== list operator   =====") # same as string slicing
a2 = [1,2,3]
b2 = [4,5,6]
print(a2 + b2) # + combines two list

print([1,2,3] * 4)

a = [1, 2, 3]
print(str(a[2]) + "hi") # str()은 정수나 실수를 문자열의 형태로 바꾸어 주는 파이썬의 내장 함수이다.

print("===== list update  =====")
 
a = [1,2,3]
a[2] = 4
print(a) 

print(a[1:2])
a[1:2] = ['a', 'b', 'c'] 
# note: it is different from a[1] =  ['a', 'b', 'c']. 리스트를 수정한다는 의미.
# a[1] = ['a', 'b', 'c']로 수정하게 되면 위와는 달리 리스트 a가 [1, ['a', 'b', 'c'], 4]라는 값으로 변하게 된다. 요소를 수정한다는 의미
print(a)

print("===== list delete   =====")
a[1:3] = [] # note: 리스트를 수정한다는 의미.
print(a)

# another way: del() function: del 객체 
del a[1]
print(a)

print("===== list realted function =====")
li = [1,2,3]
li.append(4)
li.append([5,6])
print(li)

li2 = [1,4,3,2]
li2.sort()
print(li2)

li3 = ['c', 'a', 'b']
li3.sort()
print(li3)

li4 = ['a', 'c', 'b']
li4.reverse()
print(li4)

li5  = [1,2,3]
print(li5.index(3))

li5 = [1, 2, 3]
li5.insert(0, 4)
li5.insert(3, 5)
print(li5)

li6 = [1, 2, 3, 1, 2, 3]
li6.remove(3) # 리스트에서 첫 번째로 나오는 x를 삭제하는 함수이다.
print(li6)

li7= [1,2,3]
print(li7.pop()) # LIFO: pop()은 리스트의 맨 마지막 요소를 돌려 주고 그 요소는 삭제하는 함수이다.
print(li7)

li8 = [1,2,3,1]
print(li8.count(1))

li9 = [1,2,3]
li9.extend([4,5]) # list 확장
li9.extend([6,7])
print(li9)


