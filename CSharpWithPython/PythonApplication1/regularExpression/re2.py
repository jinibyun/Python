import re

# |
p = re.compile('Crow|Servo')
m = p.match('CrowHello')

print(m)


# ^: start of character
# compare result
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))

# $: end of character
# compare result
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))

# \A similar to ^. But it does not care re.MULTILINE
# \Z similar to $. But it does not care re.MULTILINE

print("===========Word Boundary============")
# \b: Word boundary (separated by white space): check whether left or right side of word is space or not
# compare
# NOTE: \b means backspace without r (raw data)
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))  
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))

print ("========= Opposite of word boundary ========")
# \B: opposite of \b
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))  
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))

print ("========= Grouping ========") # check wheter it has repeating characters
# grouping: ( )
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group())


p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m)


print ("========= Grouping Index ========")
# group(index)
# group(0)	matched whole string
# group(1)	first matched string
# group(2)	second matched string
# group(n)	n matched string

# if want to get only name
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3))

print ("========= Grouping: Back Reference ========")
# \1 refer to group 1: fo find same repeating word. IF want to second group, use \2
p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())

print ("========= Grouping: naming ========")
# naming to grouping index
# (?P<name>\w+)\s+((\d+)[-]\d+[-]\d+): (\w+) --> (?P<name>\w+)
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print(p.search('Paris in the the spring').group())

# Lookahead Assertions
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

# to exclude :
# (?=...)  and (?!...)   ... can be replaced with characters
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())


p = re.compile(".*[.].*$") # foo.bar, autoexec.bat, sendmail.cf would be match
# to exclude .bat or .exe
p = re.compile(".*[.](?!bat$|exe$).*$")
m = p.search("autoexec.bat")
print(m)
m = p.search("autoexec.exe")
print(m)
m = p.search("autoexec.asp")
print(m)

# replace string
p = re.compile('(blue|white|red)')
m = p.sub('colour', 'blue socks and red shoes')
print(m)

p = re.compile('(blue|white|red)')
m = p.subn( 'colour', 'blue socks and red shoes')
print(m) # return tuple


p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234")) # \g<group name>


#
def hexrepl(match):
    # "Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
m = p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
print(m)

# greedy vs non-greedy
s = '<html><head><title>Title</title>'
print(len(s))

print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group()) #greedy
print(re.match('<.*?>', s).group()) #non -greedy (limit usage of *)