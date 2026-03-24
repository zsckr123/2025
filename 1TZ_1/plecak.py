def plecak(nazwy, wagi, wartosci, W):
    n = len(wagi)
    
    dp = [[0]*(W+1) for _ in range(n+1)]

    # budowa tabeli
    for i in range(1, n+1):
        for j in range(W+1):
            if wagi[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i-1][j - wagi[i-1]] + wartosci[i-1]
                )

    # odtwarzanie rozwiązania
    j = W
    wybrane = []

    for i in range(n, 0, -1):
        if dp[i][j] != dp[i-1][j]:
            wybrane.append(nazwy[i-1])
            j -= wagi[i-1]

    wybrane.reverse()
    return dp[n][W], wybrane


nazwy = ["laptop", "książka", "butelka", "kurtka"]
wagi = [2, 3, 4, 5]
wartosci = [3, 4, 5, 6]
W = 5

wynik, przedmioty = plecak(nazwy, wagi, wartosci, W)

print("Maksymalna wartość:", wynik)
print("Spakowane przedmioty:", przedmioty)