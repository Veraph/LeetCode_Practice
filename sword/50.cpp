class Solution {
public:
    // map
    char firstUniqChar(string s) {

        map<char, int> freq;
        for (char c : s) freq[c]++;

        for (char c : s) {
            if (freq[c] == 1) return c;
        }

        return ' ';
    }

    // map optimization
    char firstUniqChar(string s) {
        // if only need to count some data
        // and the order is not important
        // or you only need single element access
        unordered_map<char, bool> aux; // change int to bool to optimize
        for (char c : s)
            aux[c] = aux.find(c) == aux.end();

        for (char c : s)
            if (aux[c]) return c;

        return ' ';
    }

    // ordered map
    // c++ do not have linked list map
    // hence we could use an extra vector
    char firstUniqChar(string s) {
        unordered_map<char, bool> aux;
        vector<char> key;
        for (char c : s) {
            bool check = aux.find(c) == aux.end();
            if (check) key.push_back(c);
            aux[c] = check;
        }

        for (char c : key)
            if (aux[c]) return c;

        return ' ';
    }

};
