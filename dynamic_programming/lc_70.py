

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    dp = {}
    res = climbStairsHelper(n, dp)
    print(dp)
    return res

def climbStairsHelper(n, dp):
    if n == 1 or n == 2:
        dp[n] = n
        return n
    if n in dp:
        return dp[n]
    dp[n] = climbStairsHelper(n-1,dp) + climbStairsHelper(n-2,dp)
    return dp[n]