class MedianFinder {
public:
    // use minheap and max heap
    priority_queue<int, vector<int>, greater<int>> minheap;
    priority_queue<int, vector<int>, less<int>> maxheap; // default, bigger is on the top

    MedianFinder() {

    }

    void addNum(int num) {
        if (minheap.size() == maxheap.size()) {
            maxheap.push(num);
            minheap.push(maxheap.top());
            maxheap.pop();
        } else {
            minheap.push(num);
            maxheap.push(minheap.top());
            minheap.pop();
        }
    
    }

    double findMedian() {
        int sizeMax = maxheap.size(), sizeMin = minheap.size();
        int midMax = maxheap.top(), midMin = minheap.top();
        return (sizeMax + sizeMin) & 1 ? 1.0 * (midMin) : (midMax + midMin) * 0.5;
    }

};
