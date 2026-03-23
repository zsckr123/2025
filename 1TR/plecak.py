'''
Masz:

n przedmiotów
każdy ma:
wagę w
wartość v
plecak o pojemności W

👉 każdy przedmiot możesz wziąć albo nie (0/1)

🎯 Cel: maksymalizować wartość

'''

def plecak(wagi, wartosci, W):
    n = len(wagi)
    
    # tablica DP
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(W+1):
            if wagi[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(
                    dp[i-1][j],  # nie bierzemy
                    dp[i-1][j - wagi[i-1]] + wartosci[i-1]  # bierzemy
                )

    return dp[n][W]

wagi = [2, 3, 4, 5]
wartosci = [3, 4, 5, 6]
W = 5

print(plecak(wagi, wartosci, W))