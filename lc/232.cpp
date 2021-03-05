class MyQueue {
private:
    stack<int> aux, main;
    
    void check() {
        if (main.empty()) {
            while (!aux.empty()) {
                main.push(aux.top());
                aux.pop();
            }
        }
    }

public:
    MyQueue() {
    }

    void push(int x) {
        aux.push(x);
    }

    int pop() {
        check();
        int x = main.top();
        main.pop();
        return x;
    }

    int peek() {
        check();
        return main.top();
    }

    bool empty() {
        return main.empty() && aux.empty();
    }
};
