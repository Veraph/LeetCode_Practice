class Solution {
public:
    // time O(n), space O(n)
    int candy(vector<int> &ratings) {
        int sz = ratings.size();
        vector<int> aux(sz, 1);

        for (int i = 1; i < sz; i++) {
            if (ratings[i] > ratings[i - 1])
                aux[i] = aux[i - 1] + 1;
        }

        int right = 0, res = 0;
        for (int i = sz - 1; i >= 0; i--) {
            if (i < sz - 1 && ratings[i] > ratings[i + 1])
                right++;
            else right = 1;

            res += max(aux[i], right); 
        }
        return res;
        
    }

    // time O(n), space O(1)
    int candy(vector<int> &ratings) {
        int sz = ratings.size();
        int pre = 1, inc = 1, dec = 0, res = 1;
        for (int i = 1; i < sz; i++) {
            if (ratings[i] >= ratings[i - 1]) {
                dec = 0;
                pre = ratings[i] == ratings[i - 1] ? 1 : pre + 1;
                res += pre;
                inc = pre;
            } else {
                dec++;
                if (dec == inc) dec++;
                res += dec;
                pre = 1;
            }
        }
        return res;
    }

};
