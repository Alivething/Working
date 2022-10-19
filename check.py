def lcs(s1, s2):

    l1 = len(s1)
    l2 = len(s2)

    dp = [[0 for _ in range(l2+1)] for __ in range(l1+1)]
    caught = [[0 for _ in range(l2+1)] for __ in range(l1+1)]

    for i in range(1, l1+1):
        for j in range(1, l2+1):

            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                caught[i][j] = dp[i-1][j-1] + 1

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print("   ", end = "")
    for l in s2:
        print(l, end = "   ")

    print()
    for l in range(len(dp)-1):
        print(s1[l], caught[l+1][1:])

    common = ""
    i = l1
    j = l2
    while i > 0 and j > 0:

        if s1[i-1] == s2[j-1]:
            common += s2[j-1]
            i -= 1
            j -= 1

        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
             
        else:
            j -= 1

    print("Common characters:", common[::-1])
    print("Length of LCS:", dp[l1][l2])

def lis(arr):
    subs = [0]*len(arr)
    inc = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            subs[i] = subs[i-1] + 1
            inc.append(arr[i])
        else:
            subs[i] = subs[i-1]

    print("Increasing sequence:", inc)
    print("Length of LIS:", subs[len(subs)-1]+1)

lcs("ABACDEABA", "BCADCEEABE")
lis([10, 22, 9, 33, 21, 50, 41, 60, 80])