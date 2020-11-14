#include <iostream>
#include <stack>
using std::stack;

class Cqueue {
    stack<int> stack1, stack2;

public:
    Cqueue() {
        // initialize
        while (stack1.size())
            stack1.pop();
        while (stack2.size())
            stack2.pop()
    }

    void add(int val) {
        stack1.push(val);
    }

    int deleteHead() {
        if (stack2.empty()) {
            while (stack1.size) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }

        if (stack2.empty()) {
            return -1;
        }

        int deleteItem = stack2.top();
        stack2.pop()
        return deleteItem;
    }
};

