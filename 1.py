string = input()
string1 = ""
count = 0
l = len(string)
for i in range(0, l):
    if string[i] != " ":
        string1 = string1 + string[i]
l = len(string1)
while l != len(string1) // 2:
    if string1[l - 1] != string1[len(string1) - l]:
        count = count + 1
    l = l - 1
if count == 0:
    print(1)
else:
    print(0)
