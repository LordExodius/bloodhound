code = "1Z234567890"

print(code[2:])
print(code[len(code) - 1])

print()

from codeIdentifier import checkUPS

checkUPS("1Z999AA10123456784")

order = ""
while order != "done":
    order = input("enter order: ")
    print(" ".join(order.lower().split()))