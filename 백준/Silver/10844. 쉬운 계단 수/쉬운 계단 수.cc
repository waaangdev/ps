//디피그리디

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

llint dp[100][10];

llint sol2(int num,int n) {

	if (n == 0) {
		return 1;
	}
	if (dp[n][num] != 0) {
		return dp[n][num] - 1;
	}
	llint r = 0;
	if (num != 0) {
		r+= sol2(num - 1, n-1);
	}
	if (num != 9) {
		r += sol2(num + 1, n-1);
	}
	r %= 1000000000;
	dp[n][num] = r+1;
	return r;
}

int sol() {
	llint n,r;
	r = 0;
	cin >> n;
	for (int i = 1; i < 10; i++) {
		r += sol2(i,n-1);
		r %= 1000000000;
	}
	cout << r;

	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//cin >> case_;

	//for (int i = 0; i < case_; i++) {
	//	sol();
	//}

	while (sol()) {

	}


}






