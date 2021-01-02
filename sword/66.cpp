class Solution {
public:
    vector<int> constructArr(vector<int>& a) {
        if (a.empty()) return {};
        int sz = a.size();
        vector<int> front(sz);
        vector<int> back(sz);
        front[0] = 1; back[sz - 1] = 1;
        for (int i = 1; i < sz; i++) {
            front[i] = a[i - 1] * front[i - 1];
            back[sz - 1 - i] = a[sz - i] * back[sz - i];
        }
        vector<int> b;
        for (int i = 0; i < sz; i++) {
            b.push_back(front[i] * back[i]);
        }
        return b;
    }


    // dp optimize
    vector<int> constructArr(vector<int>& a) {
        if (a.empty()) return {};
        int sz = a.size();
        vector<int> b(sz); b[0] = 1;
        for (int i = 1; i < sz; i++) {
            b[i] = b[i - 1] * a[i - 1];
        }
        
        int aux = 1;
        for (int i = sz - 2; i >= 0; i--) {
            aux *= a[i + 1];
            b[i] *= aux;
        }
        return b;
    }
};
