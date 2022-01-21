#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int N;
    cin >> N;
    vector<pair<int, int>> ba(N);
    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        pair<int, int> tmp(b, a);
        ba[i] = tmp;
    }
    sort(ba.begin(), ba.end());
    for (auto i : ba) {
        int a, b;
        tie(b, a) = i;
        cout << a <<" "<< b << endl;
    }
}