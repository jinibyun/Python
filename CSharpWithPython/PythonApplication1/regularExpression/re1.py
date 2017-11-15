import re 


# []: character class. Any character (NOT all characters)
# [a-zA-Z] : any alphabet char
# [0-9] : any number
# ^ inside [] : it means NOT
# [^0-9] : only alphabet (any)

# short cut
# \d - number. same as [0-9]
# \D - same as [^0-9]
# \s - whitespace [ \t\n\r\f\v] " " means sapce
# \S - same as [^ \t\n\r\f\v]
# \w - same as [a-zA-Z0-9]
# \W - same as [^a-zA-Z0-9]


data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))


print("---------- match method ------------")
p = re.compile('[a-z]+')
m = p.match("python")
print(m)

m = p.match("3 python")
print(m)

# print in more detail
m = p.match('string goes here')
if m:
    print('Match found: ', m.group())
else:
    print('No match')

print("---------- search method ------------")
m = p.search("python")
print(m)

m = p.search("3 python") # different from match. It search any string of all string.
print(m)

print("---------- findall method ------------")
result = p.findall("life is too short")
print(result) # return type of list

print("---------- finditer method ------------")
result = p.finditer("life is too short")
print(result)
for r in result: print(r) # similar to findall. return type of iterable object. Each objec is match object



print("---------- More Detail: Match Object in the resulf of some of above ------------")
m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

# p = re.compile('[a-z]+')
# m = p.match("python")
# -->> m = re.match('[a-z]+', "python")

print("----- compile option -----")
p = re.compile('a.b', re.DOTALL) # . means all chars except \n. But if we include re.DOTALL then it will include all chars with \n
m = p.match('a\nb')
print(m)


p = re.compile('[a-z]', re.I) # case-insensitive
m = p.match('PYTHON')
print(m)


p = re.compile("^python\s\w+") # ^ means start of string. \s means space \w word
data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
p = re.compile("^python\s\w+", re.MULTILINE) # ^ should be recognized line by line.
print(p.findall(data))


print("------------------ VERBOSE, X -----------------")
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

# -->> same expression: more redable
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE) # or re.X option

print("------------------ raw string -----------------")
# p = re.compile('\\\\section') should be passed to python engine, it will understand \\section. Then regular expression will work as expected.
# too complicated. Therefore 
p = re.compile(r'\\section') # r means raw string