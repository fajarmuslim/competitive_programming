class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        list_digit = []
        while n != 0:
            list_digit.append(n % 10)
            n = n // 10

        multiplication = 1

        for item in list_digit:
            multiplication *= item

        return multiplication - sum(list_digit)