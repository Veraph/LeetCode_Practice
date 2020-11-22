// the more time efficient method of 16.cpp

class Solution {
public:
    const double EPSILON = 1e-6;
    bool g_invalidInput = false;

    bool equal(double val1, double val2) {
        return fabs(val1 - val2) < EPSILON;
    }

    double myPow(double x, int n) {
        // there is a trap that INT_MIN can not be
        // present as -INT_MAX
        long n_l = n;
        g_invalidInput = false;
        if (equal(x, 0.0)) {
            if (n >= 0) {
                // include the meaningless situation of 0^0
                return 0.0;
            } else {
                g_invalidInput = true;
                return 0.0;
            }
        }

        unsigned long absN = n_l < 0 ? (unsigned long) (-n_l) : (unsigned long) n_l;
        double res = Power(x, absN);

        return n < 0 ? (1.0 / res) : res;
    }

    double Power(double base, unsigned long exponent) {
        if (exponent == 0) {
            return 1.0;
        }
        if (exponent == 1) {
            return base;
        }

        // use right shift to replace / 2 to optimize
        double res = Power(base, exponent >> 1);
        res *= res;
        // use & 0x1 to check whether it is odd or even
        if (exponent & 0x1) 
            res *= base;
        return res;
    }

    double Power_interate(double base, unsigned long exponent) {
        double res = 1.0;
        while (exponent) {
            if (exponent & 0x1)
                res *= base;
            base *= base;
            exponent >>= 1;
        }
        return res;
    }

};





    }
