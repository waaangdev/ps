#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));

int case_ = 1;


struct llint_pair {
	llint first;
	llint second;
};

llint n, m;
llint li[100];
llint li2[100];
llint dp[100][10001];
int dp2[100][10001];


llint sol2(int idx,llint left) {
	if (idx == n) {
		return 0;
	}
	if (dp2[idx][left]) {
		return dp[idx][left];
	}
	llint r = -1;
	if (left >= li2[idx]) {
		r = sol2(idx + 1, left - li2[idx]) + li[idx];
	}
	if (r == -1) r = sol2(idx + 1, left);
	else r = max(r, sol2(idx + 1, left));


	dp2[idx][left] = true;
	dp[idx][left] = r;

	return r;
	
}


int sol() {
	cin >> n >>m;
	
	for (int i = 0; i < n; i++) {
		cin >> li[i];
	}
	for (int i = 0; i < n; i++) {
		cin >> li2[i];
	}

	for (int i = 0; i <= 10000; i++) {
		if (sol2(0, i) >= m) {
			cout << i;
			break;
		}
	}

	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//cin >> case_;

	for (int i = 0; i < case_; i++) {
		sol();
	}

	//while (!sol()) {

	//}


}






