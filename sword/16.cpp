// when the input might be invalid
// we have to use on of three kinds of way to report the invalid situation
// 1. we return 1 if invalid
// 2. we set a global variable
// 3. we arise error

class Solution {

    const double EPSILON = 1e-6;
    bool g_invalidInput = false;

    bool equal(double val1, double val2) {
        return fabs(val1 - val2) < EPSILON;
    }

    double myPow(double x, int n) {
        g_invalidInput = false;

        if (equal(x, 0.0)) {
            if (n >= 0) {
                // 0 ^ 0 is meaning less
                return 0.0;
            } else {
                g_invalidInput = true;
                return 0.0;
            }
        }

        unsigned int absExponent = n < 0 ? (unsigned int) (-n) : (unsigned int) n;

        double res = Power(x, absExponent);

        return n < 0 ? (1.0 / res) : res;
    }

    double Power(double x, unsigned int exponent) {
        double res = 1.0;
        for (int i = 0; i < exponent; ++i) {
            res *= x;
        }
        
        return res;
    }
};
