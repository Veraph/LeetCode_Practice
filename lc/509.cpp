class Solution {
public:
    // iteration
    // O(n)
    int fib(int n) {
        if (n < 2) return n;

        int pre = 0, cur = 1;
        for (int i = 2; i <= n; i++) {
            int tmp = cur;
            cur += pre;
            pre = tmp;
        }
        return cur;
    }

    // quick pow
    // O(logn)

    struct matrix
    {
        int a1, a2, b1, b2;
        matrix(int a1, int a2, int b1, int b2) : a1(a1), a2(a2), b1(b1), b2(b2) {}
        matrix operator* (const matrix &y) {
            matrix ans (a1 * y.a1 + a2 * y.b1,
                        a1 * y.a2 + a2 * y.b2,
                        b1 * y.a1 + b2 * y.b1,
                        b1 * y.a2 + b2 * y.b2);
            return ans;
        }
    };

    matrix quickPow(matrix a, int n) {
        matrix base (1, 0, 0 ,1);
        while (n) {
            if (n & 1)
                base = base * a;
            a = a * a;
            n >>= 1;
        }
        return base;
    }

    int fib(int n) {
        if (n < 2) return n;

        matrix init(1, 1, 1, 0);
        matrix ans = quickPow(init, n - 1);
        return ans.a1;
    }
};
