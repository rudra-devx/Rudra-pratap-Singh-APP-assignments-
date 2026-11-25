def knapsack_bottom_up(weights, values, capacity):

    n = len(weights)

    # DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:

                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Input
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

result = knapsack_bottom_up(weights, values, capacity)

print("Maximum value:", result)

def knapsack_top_down(weights, values, capacity):

    n = len(weights)

    memo = {}

    def solve(i, capacity):

        if i == 0 or capacity == 0:
            return 0

        if (i, capacity) in memo:
            return memo[(i, capacity)]

        if weights[i - 1] <= capacity:

            include = values[i - 1] + solve(
                i - 1,
                capacity - weights[i - 1]
            )

            exclude = solve(i - 1, capacity)

            memo[(i, capacity)] = max(include, exclude)

        else:
            memo[(i, capacity)] = solve(i - 1, capacity)

        return memo[(i, capacity)]

    return solve(n, capacity)


# Input
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

result = knapsack_top_down(weights, values, capacity)

print("Maximum value:", result)
