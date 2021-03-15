def solve_recursion(m, w, v, n):
    if m == 0 or n == 0:
        return 0
    if w[n-1] > m:
        return solve_recursion(m, w, v, n-1)
    else:
        included = v[n-1] + solve_recursion(m - w[n-1], w, v, n-1)
        excluded = solve_recursion(m, w, v, n-1)

        return max(included, excluded)

w = [4, 2, 3]
v = [10, 4, 7]

print(solve_recursion(5, w, v, 3))