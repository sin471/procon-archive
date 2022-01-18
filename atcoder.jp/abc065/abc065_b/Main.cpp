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
    int i = 1, cnt = 0;
    vector<int> flags(N);
    while (true)
    {
        
        i = A[i - 1];
        cnt++;
        if (i == 2)
        {
            cout << cnt << endl;
            break;
        }
        else if (flags[i - 1])
        {
            cout << -1 << endl;
            break;
        }
        flags[i - 1] = 1;
    }
}