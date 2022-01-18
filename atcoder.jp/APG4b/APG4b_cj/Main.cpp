#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int INF32 = 2147483647;         // 32bit整数のinf
const ll INF64 = 9223372036854775807; // 64bit整数のinf
const int MOD = 1000000007;           //問題による

ll myceil(ll a, ll b) { return (a + (b - 1)) / b; }
ll myfloor(ll a, ll b) { return a / b; }

int main()
{
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    int sum = accumulate(A.begin(), A.end(), 0);
    int mean = sum / N;
    for (int i = 0; i < N; i++)
    {
        cout << abs(A[i] - mean) << endl;
    }
}