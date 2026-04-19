//내리막 길

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));

int case_;

int map_[502][502];
int dp[502][502];

int sol2(int i,int j) {
	if (i == 1 and j == 1) {
		return 1;
	}
	if (dp[i][j] != 0) {
		return dp[i][j] - 1;
	}
	int dum = map_[i][j];
	int r = 0;
	if (dum < map_[i - 1][j])r += sol2(i - 1, j);
	if (dum < map_[i + 1][j])r += sol2(i + 1, j);
	if (dum < map_[i][j-1])r += sol2(i, j-1);
	if (dum < map_[i][j+1])r += sol2(i, j+1);

	dp[i][j] = r+1;
	return r;
}

void sol() {
	llint n, m;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map_[i+1][j+1];
		}
	}
	cout << sol2(n,m);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//cin >> case_;
	case_ = 1;
	for (int c = 0; c < case_; c++) {
		sol();
	}
}






