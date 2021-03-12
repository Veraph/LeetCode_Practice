class Solution {
public:
    bool isValidSerialization(string preorder) {
        int sz = preorder.size();
        int slots = 1;

        int i = 0;
        while (i < sz) {
            if (!slots) return false;

            if (preorder[i] == ',') {
                i++;
            } else if (preorder[i] == '#') {
                slots--;
                i++;
            } else {
                while (i < sz && preorder[i] != ',') i++;
                slots++;
            }
        }
        return !slots;

    }
};
