//디피그리디

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));

int case_ = 1;
int dp[32768][4][182];

int sol2(int n,int c,int l) {
	//cout << n << "\n";
	if (n < 0) return 0;
	if (n == 0) return 1;
	if (c == 4) return 0;
	if (dp[n][c][l] != 0)return dp[n][c][l]-1;
	int r = 0;
	int dum = 0;
	for (int i = l; i < 182; i++) {
		dum = n - (i * i);
		if (dum >= 0) r += sol2(dum,c+1,i);
		else break;
	}
	dp[n][c][l] = r+1;
	return r;
}


int sol() {
	int n;
	cin >> n;
	if (!n)return 1;

	cout << sol2(n,0,1) << "\n";

	return 0;

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//cin >> case_;
	// 
	//for (int i = 0; i < case_; i++) {
	//	sol();
	//}

	while (!sol()) {

	}


}






