ans = input()
ans2 = ""
count = 0
count2 = 0
i = len(ans) - 1
while i != -1:
    if ans[i] != " ":
        count += 1
    if ans[i] == " " or i == 0:
        while count2 != count:
            if i==0:
                ans2 = ans2 + ans[i + count2]
            else:
                ans2 = ans2 + ans[i + 1 + count2]
            count2 += 1
        count = 0
        count2 = 0
        ans2 = ans2 + " "
    i -= 1
print(ans2)
