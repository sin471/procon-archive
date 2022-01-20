#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int N;
    cin >> N;
    vector<int> T(N);
    for (int i = 0; i < N; i++) cin >> T[i];
    int M;
    cin >> M;
    vector<vector<int>> PX(M, vector<int>(2));

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < 2; j++) {
            cin >> PX[i][j];
        }
    }
    int P, X;
    int sum = 0;
    for (int i = 0; i < M; i++) {
        vector<int> a;
        a = T;
        P = PX[i][0];
        X = PX[i][1];
        a[P - 1] = X;
        sum = accumulate(a.begin(), a.end(), 0);
        cout << sum << endl;
    }
}