a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

curr = a[0]
ans = a[0]

for ele in a[1:]:
    # print(ele, curr)
    curr = max(ele, curr + ele)
    ans = max(curr, ans)

print(ans)


## ans variable stores the maximum some obtained overall in the array.
## curr variable stores the maximum some obtained until that element that we are on.
## if at any point curr exceeds ans, we update ans.

