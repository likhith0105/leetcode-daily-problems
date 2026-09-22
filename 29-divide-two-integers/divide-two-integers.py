class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer bounds
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Edge case: overflow when INT_MIN / -1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine if the result should be positive
        is_positive = (dividend > 0) == (divisor > 0)

        # Convert both numbers to negative to avoid abs(INT_MIN) overflow
        dividend = -dividend if dividend > 0 else dividend
        divisor = -divisor if divisor > 0 else divisor

        quotient = 0

        # Perform bit-shifting division
        while dividend <= divisor:
            temp_divisor = divisor
            multiple = -1  # Accumulate negatively to prevent overflow

            # Prevent overflow during bit shifting
            while temp_divisor >= (INT_MIN >> 1) and dividend <= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            dividend -= temp_divisor
            quotient += multiple  # quotient remains <= 0

        # Return positive or negative based on initial signs
        return -quotient if is_positive else quotient