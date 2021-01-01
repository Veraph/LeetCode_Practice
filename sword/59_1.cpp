class MaxQueue {
public:
    queue<int> mainQue;
    deque<int> auxQue;
    MaxQueue() {}

    int max_value() {
        if (!auxQue.empty())
            return auxQue.front();
        return -1;
    }

    void push_back(int value) {
        mainQue.push(value);
        while (!auxQue.empty() && value > auxQue.back()) {
                auxQue.pop_back();
        }
        auxQue.push_back(value);
    }

    int pop_front() {
        if (!mainQue.empty() && !auxQue.empty()) {
            if (mainQue.front() == auxQue.front())
                auxQue.pop_front();
            int tmp = mainQue.front();
            mainQue.pop();
            return tmp;
        }
        return -1;
    }
};



