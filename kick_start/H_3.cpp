#include <iostream>
#include <algorithm>
#include <cstdlib>
#define maxN 100000

using namespace::std;

int main() {
    int T; cin >> T;
    long corX[maxN];
    long corY[maxN];
    for (int t = 0; t < T; ++t) {
        int N; cin >> N;
        for (int n = 0; n < N; ++n) {
            cin >> corX[n] >> corY[n];
        }
        
        sort(corX, corX + N);
        sort(corY, corY + N);
        long tarY = corY[N/2];
        long tarX = corX[N/2];

        long movY = 0;
        for (int i = 0; i < N; ++i) {
            movY += abs(tarY - corY[i]);
        }

        long movX = 0;
        for (int i = 0; i < N; ++i) {
            if (i > N / 2) {
                movX += abs(tarX + (i - N/2) - corX[i]);
            } else {
                movX += abs(tarX - (N/2 - i) - corX[i]);
            }
        }
        cout << movX << endl;
        cout << movY << endl;
        cout << "Case #" << t + 1 << ": " << movX + movY << endl;
    }
    return 0;
}
