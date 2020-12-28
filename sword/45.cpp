class Solution {
public:
    // use stl sort
    string minNumber(vector<int> &nums) {
        if (nums.size() == 1) return to_string(nums[0]);

        vector<string> aux;
        string res = "";

        for (int i : nums) aux.push_back(to_string(i));
        sort(aux.begin(), aux.end(), strCompare);
        for (string s : aux) res += s;

        return res;
    }

    static bool strCompare(const string &s1, const string &s2) {
        string left = s1 + s2;
        string right = s2 + s1;

        return left < right;
    }

    // use quick sort
    string minNumber(vector<int> &nums) {
        if (nums.size() == 1) return to_string(nums[0]);

        vector<string> aux;
        for (int i : nums) aux.push_back(to_string(i));
        quickSort(aux, 0, aux.size() - 1);
        
        string res;
        for (string s : aux) res += s;
        return res;
    }

    void quickSort(vector<string> &strs, int l, int r) {
        if (l >= r) return;
        int i = l, j = r;
        while (true) {
            // use the r as the base
            // find all less than r and put in the left side
            // find all more than r and put in the right side
            while (strs[i] + strs[r] <= strs[r] + strs[i] && i < j) i++;
            while (strs[j] + strs[r] >= strs[r] + strs[j] && i < j) j--;

            if (i >= j) break;
            swap(strs[i], strs[j]);    
        }
        swap(strs[i], strs[r]);
        quickSort(strs, l, i - 1);
        quickSort(strs, i + 1, r);
    }
};
