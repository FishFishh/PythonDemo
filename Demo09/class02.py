import random

code_list = []
for i in range(2):
    first_kind = random.randint(65, 90)
    random_uppercase = chr(first_kind)
    code_list.append(random_uppercase)
for i in range(2):
    second_kinds = random.randint(97, 122)
    random_lowercase = chr(second_kinds)
    code_list.append(random_lowercase)
for i in range(2):
    third_kinds = random.randint(0, 9)
    code_list.append(str(third_kinds))
code = "".join(code_list)
print(code)
