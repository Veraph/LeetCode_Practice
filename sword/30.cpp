class Solution {
public:
    stack<int> main, aux;

    MinStack() {}

    void push(int x) {
        main.push(x);

        if (aux.empty() || aux.top() > x) aux.push(x);
        else aux.push(aux.top());
    }

    void pop() {
        assert(!main.empty() && !aux.empty());
        main.pop();
        aux.pop();
    }

    int top() {
        assert(!main.empty() && !aux.empty());
        return main.top():
    }

    int min() {
        assert(!main.empty() && !aux.empty());
        return aux.top();
    }
};
