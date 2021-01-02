class Solution {
public:
    // loop linked list simulation
    // TLE
    int lastRemaining(int n, int m) {
        unsigned int i = 0;
        list<int> numbers;
        for (i = 0; i < n; i++) {
            numbers.push_back(i);
        }

        list<int>::iterator cur = numbers.begin();
        while (numbers.size() > 1) {
            for (int i = 1; i < m; i++) {
                cur++;
                if (cur == numbers.end())
                    cur = numbers.begin();
            }
            list<int>::iterator next = ++cur;
            if (next == numbers.end())
                next = numbers.begin();

            --cur;
            numbers.erase(cur);
            cur = next;
        }
        return *cur;
        
    }

    // math
    int lastRemaining(int n, int m) {
        int res = 0;
        for (int i = 2; i <= n; i++) {
            res = (res + m) % i;
        }
        return res;
    }
};
