#include <bits/stdc++.h>

using namespace std;

int main()
{
    int a, b, i, j;
    cin >> a >> b;
    cout << "A:";
    while (i < a) {
        cout << "]";
        i++;
    }
    cout << endl
         << "B:";
    while (j < b) {
        cout << "]";
        j++;
    }
    cout << endl;
}