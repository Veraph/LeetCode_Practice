class Solution {
public:
    int calculate(string s) {
        vector<int> aux;
        char preSign = '+';
        int num = 0;
        int sz = s.size();
        for (int i = 0; i < sz; i++) {
            if (isdigit(s[i])) {
                num = num * 10 + int(s[i] - '0');
            }

            if ((!isdigit(s[i]) && s[i] != ' ') || i == sz - 1) {
                switch(preSign) {
                    case '+':
                        aux.push_back(num);
                        break;
                    case '-':
                        aux.push_back(-num);
                        break;
                    case '*':
                        aux.back() *= num;
                        break;
                    default:
                        aux.back() /= num;
                }
                    preSign = s[i];
                    num = 0;
                }
            }
        return accumulate(aux.begin(), aux.end(), 0);

    }
};
