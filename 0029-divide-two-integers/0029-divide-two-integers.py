class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Edge case: overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Convert to positive
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Subtract divisor powers of 2 from dividend
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        # Apply sign
        return sign * quotient

            