def max_score(N, T, Mi, Pi, Ri):
    # Initialize DP table
    dp = [0] * (T + 1)
    
    # Iterate over each problem
    for i in range(N):
        # Traverse time from T down to Ri[i] in reverse order
        for t in range(T, Ri[i] - 1, -1):
            # Calculate the potential new score if we solve problem i at time t
            solve_time = t - Ri[i]
            if solve_time >= 0:
                potential_score = Mi[i] - solve_time * Pi[i]
                # Ensure the new score is non-negative and update DP table
                if potential_score > 0:
                    dp[t] = max(dp[t], dp[solve_time] + potential_score)
    
    # The answer is the maximum value in the DP table
    return dp

N, T = map(int, input().split())
table = [[0] * (T + 1) for _ in range(N)]

Mi = list(map(int, input().split()))
Pi = list(map(int, input().split()))
Ri = list(map(int, input().split()))

sumofpanelty = []
for i in range(N):
    sumofpanelty.append(Ri[i] * Pi[i])

table[0][Ri[0]] = Mi[0] - Ri[0] * Pi[0]
for i in range(1, N + 1):
    table[i][Ri[i] + Ri[i - 1]] = max(table[i-1][Ri[i-1]], table[i-1][Ri[i-1]] + Mi[i] - sumofpanelty[i]) 

print(max(table))
# print(max_score(N, T, Mi, Pi, Ri))  # Expected output should be 310
