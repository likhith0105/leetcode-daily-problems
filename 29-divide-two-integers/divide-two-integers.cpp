#include <climits>

class Solution {
public:
    int divide(int dividend, int divisor) {
        // Edge case: overflow when INT_MIN / -1
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }

        // Determine if result should be positive
        bool isPositive = (dividend > 0) == (divisor > 0);

        // Convert both numbers to negative to avoid abs(INT_MIN) overflow
        dividend = dividend > 0 ? -dividend : dividend;
        divisor = divisor > 0 ? -divisor : divisor;

        int quotient = 0;

        // Perform bit-shifting division
        while (dividend <= divisor) {
            int tempDivisor = divisor;
            int multiple = -1; // Accumulate negatively to prevent overflow on INT_MIN

            // Prevent overflow during bit shifting: tempDivisor >= INT_MIN / 2
            while (tempDivisor >= (INT_MIN >> 1) && dividend <= (tempDivisor << 1)) {
                tempDivisor <<= 1;
                multiple <<= 1;
            }

            dividend -= tempDivisor;
            quotient += multiple; // quotient stays <= 0
        }

        // If the result should be positive, negate the negative quotient;
        // otherwise, return the negative quotient directly.
        return isPositive ? -quotient : quotient;
    }
};