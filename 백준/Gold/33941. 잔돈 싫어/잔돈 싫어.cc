#define _USE_MATH_DEFINES
#include <bits/stdc++.h>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;

int _case = 1;
int _caseidx = 0;

template<typename T> using MinHeap = priority_queue<T, vector<T>, greater<T>>;

template <typename T> bool minimize(T &target, T candidate) {
    return target > candidate ? (target = candidate, true) : false;
}
template <typename T> bool maximize(T &target, T candidate) {
    return target < candidate ? (target = candidate, true) : false;
}

// struct int_pair {
// 	int first;
// 	int second;
// };

//bool compare(int_pair i, int_pair j) {
//	if (i.first == j.first) {
//		return i.second < j.second;
//	}
//	return i.first < j.first;
//}

//auto [a,b,c] = tuple(1,2,3);


int n;
llint dp[101010][50];
llint li[101010];
int sol() {
	cin >> n;

    for (int i = 0; i < n;i++){
        llint d;
        cin >> d;
        d/=10;

        if(d < 2000 and d > 50){
            li[i]=d-50;
        }
        else{
            li[i]=-1;
        }
    }
    for (int i = n; i > -1;i--){
        for (int j = 0; j < 50;j++){
            if(i==n){
                if(j == 0){
                    dp[i][j]=0;
                }
                else{
                    dp[i][j]=-1;
                }
            }
            else{
                dp[i][j] = max(dp[i+1][j],(dp[i+1][(j+li[i])%50]==-1)?-1:(dp[i+1][(j+li[i])%50]+li[i]));
            }
        }
    }
    if(dp[0][0]==-1){
        dp[0][0]=0;
    }
    cout << dp[0][0]*10;

	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//cin >> _case;

	for (_caseidx = 0; _caseidx < _case; _caseidx++) {
		if (sol()) break;
	}

	//while (!sol()) {

	//}
}






