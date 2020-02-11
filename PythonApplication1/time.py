print("=========== time =========== ")

import time
# return current time as real number.
# based on 1970-1-1 0:0:0  -->> 1
print (time.time())

print(time.localtime(time.time()));
print(time.asctime(time.localtime(time.time()))) # simpler: print(time.ctime())

# time.strftime('{format}', time.localtime(time.time()))
'''
Time format code

Format 	Desc	e.g
%a	        	Mon
%A	        	Monday
%b	        	Jan
%B	        	January
%c	        	06/01/01 17:22:21
%d	        	[01,31]
%H	        	[00,23]
%I	        	[01,12]
%j	        	[001,366]
%m	        	[01,12]
%M	        	[01,59]
%p	        	AM
%S	        	[00,59]
%U	        	[00,53]
%w	        	[0(Sunday),6]
%W	        	[00,53]
%x	        	06/01/01
%X	        	17:22:21
%Y	        	2001
%Z	        	Standard Time
%%	        	%
%y	        	01 (except century)
'''

print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))

for i in range(10):
    print(i)
    time.sleep(1) # second. It is like Thread.Sleep in C#