// 738 monotone-increasing-digits

// it is actually a greedy
class Solution {
public:
    int monotoneIncreasingDigits(int N) {
        string num = to_string(N);
        int idx = 1;
        while (idx < num.size() && num[idx - 1] <= num[idx])
            idx++;

        if (idx < num.size()) {
            int high_idx = 0;
            for (int i = idx - 1; i > 0; i--) {
                if (num[i - 1] < num[i]) {
                    high_idx = i;
                    break;
                }
            }
            num[high_idx] = num[high_idx] - 1;
            for (int i = high_idx + 1; i < num.size(); i++) {
                num[i] = '9';
            }
        }
        return stoi(num);

                    
    }

};

// math
class Solution {
public:
    int monotoneIncreasingDigits(int N) {
        int idx = 1;
        int res = N;
        while (idx <= res / 10) {
            // get the two digits from the end
            int cur = res / idx % 100;
            idx *= 10;
            if (cur / 10 > cur % 10) {
                res = res / idx * idx - 1;
            }
        }
        return res;
    }

};
