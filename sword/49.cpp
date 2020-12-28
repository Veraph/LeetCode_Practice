class Solution {
public:
    // method 1
    // space O(1) but calculate every number
    int nthUglyNumber(int n) {
        int i = 1, num = 1;
        while (i < n) {
            if (isUgly(++num)) {
                i++;
            }
        }
        return num;
    }

    bool isUgly(int num) {
        while (!(num % 2)) num /= 2;
        while (!(num % 3)) num /= 3;
        while (!(num % 5)) num /= 5;

        return num == 1 ? true : false;
    }

    // method 2
    // space O(n), but only calculate ugly numbers
    int nthUglyNumber(int n) {
        if (n <= 0) return 0;

        vector<int> aux(n);
        aux[0] = 1;
        int idx = 1;
        int mul2 = 0, mul3 = 0, mul5 = 0;
        while (idx < n) {
            int min = threeMin(aux[mul2] * 2, aux[mul3] * 3, aux[mul5] * 5);
            aux[idx] = min;

            while (aux[mul2] * 2 <= min) mul2++;
            while (aux[mul3] * 3 <= min) mul3++;
            while (aux[mul5] * 5 <= min) mul5++;
            
            idx++;
        }
        return aux[n - 1];
    }

    int threeMin(int a, int b, int c) {
        int min = a >= b ? b : a;
        return min >= c ? c : min;
    }
};
