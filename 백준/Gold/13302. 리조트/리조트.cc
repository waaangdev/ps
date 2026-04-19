//고속도로

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));


int n,m;
bool map_[101];
int dp[101][40];

int sol(int idx,int tikat) {
	if (idx > n) {
		return 0;
	}
	if (dp[idx][tikat] != 0) {
		return dp[idx][tikat]-1;
	}
	if (map_[idx]) {
		return  sol(idx + 1, tikat);
	}
	int r = 0;
	r = (sol(idx + 1, tikat)+10000);
	r = min(sol(idx + 3, tikat+1) + 25000,r);
	r = min(sol(idx + 5, tikat+2) + 37000,r);
	if (tikat>=3) {
		r = min(sol(idx + 1, tikat-3), r);
	}
	dp[idx][tikat] = r + 1;
	//cout << idx << ' '<< tikat<<" "<<r<<"\n";
	return r;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int inp;
		cin >> inp;
		map_[inp] = true;
	}
	cout << sol(1, 0);

}






