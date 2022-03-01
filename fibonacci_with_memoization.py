class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        
        def recurr_fib(n):
            if n in cache:
                res = cache[n]

            if n < 2:
                res = n
            else:
                res = recurr_fib(n-1) + recurr_fib(n-2)
            
            cache[n] = res

            return res
        
        return recurr_fib(n)