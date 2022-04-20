#include <bits/stdc++.h> 
using namespace std;

void solve(){
    long long int m,n;
    cin >> m >> n;

    long long int k;
    cin >> k;

    vector< vector< long long int >> matrix (m, vector< long long int > (n,0));
    vector< pair<long long int, long long int >> index_position;
    
    for (long long int i=0; i<m; i++){
        for (long long int j=0; j<n; j++){
            cin >> matrix[i][j];
            if(matrix[i][j] == k){
                index_position.push_back(make_pair(i,j));
            }
        }
    }
    for(auto i: index_position){
        cout << i.first << ' ' << i.second << endl;
    }

}

int32_t main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    solve();
    return 0;
}