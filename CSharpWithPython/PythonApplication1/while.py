treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("%d hit" % treeHit)
    if treeHit == 10:
        print("tree is fallen")


prompt = """
    1. Add
    2. Del
    3. List
    4. Quit

    Enter number: """

number =0
while number !=4:
    print(prompt)
    number = int(input())

# break
coffee = 10
money = 300
while money:
    print("Coffee for you")
    coffee = coffee - 1
    print("There is %d cup of coffee left" % coffee)
    if not coffee:
        print("No coffee any more")
        break