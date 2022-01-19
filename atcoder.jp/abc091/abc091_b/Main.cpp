#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<string> S(N);
  for(int i=0;i<N;i++){
    cin >> S[i];
  }
  int M;
  cin >> M;
  vector<string> T(M);
  for(int i=0;i<M;i++){
    cin >> T[i];
  }
  
  map<string,int> blue;
  map<string,int> red;
  for(int i=0;i<N;i++){
    blue[S[i]]=0;
  }
  for(int i=0;i<M;i++){
    red[T[i]]=0;
  }

  for(int i=0;i<N;i++){
    blue[S[i]]++;
  }
  for(int i=0;i<M;i++){
    red[T[i]]++;
  }
  
  int ans=0;
  for(int i=0;i<N;i++){
    ans=max(ans,blue[S[i]]-red[S[i]]);
  }
  cout << ans << endl;
}
