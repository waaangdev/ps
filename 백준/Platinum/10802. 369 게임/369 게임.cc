#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));

int case_ = 1;


struct llint_pair {
	llint first;
	llint second;
};


llint n;
string a,b;
llint mod = 20150523;
llint dp[100010][2][2][3];
llint pdp[100010];
llint adp[100010];
llint bdp[100010];


llint ddp(llint idx, llint low, llint high, llint mod3) {
	if (idx == n) {
		return (mod3 % 3 == 0) ? 1 : 0;
	}
	if (dp[idx][low][high][mod3] != 0) {
		return dp[idx][low][high][mod3]-1;
	}

	llint r = 0;
	llint mins = (low)? (llint)(a[idx] - '0'):0;
	llint maxs = (high)? (llint)(b[idx] - '0')+1:10;

	for (llint i = mins; i < maxs; i++) {
		llint nl = (i == mins)?low:0;
		llint nh = (i == maxs-1) ? high : 0;
		if (i == 3 or i == 6 or i == 9) {
			if (idx == n - 1) {
				r += 1;
			}
			else {
				llint dmin = (nl) ? adp[idx + 1] : 0;
				llint dmax = (nh) ? (bdp[idx + 1] + 1) : pdp[n - idx - 1];
				r += (dmax - dmin+ mod)%mod;
			}
		}
		else {
			r += ddp(idx + 1, nl, nh, (mod3 + i) % 3);
		}
		r %= mod;
	}
	dp[idx][low][high][mod3] = r+1;
	return r;
}

int sol() {
	cin >> a >> b;
	a = string(b.length() - a.length(), '0') + a;
	n = b.length();

	pdp[0] = 1;
	pdp[1] = 10;
	for (llint i = 2; i < 100010; i++) {
		pdp[i] = (pdp[i - 1] * 10) % mod;
	}

	for (llint i = n-1; i > -1; i--) {
		adp[i] = (adp[i + 1] + (llint)(a[i]-'0')*pdp[n - i - 1]) % mod;
	}
	for (llint i = n - 1; i > -1; i--) {
		bdp[i] = (bdp[i + 1] + (llint)(b[i] - '0') * pdp[n - i - 1]) % mod;
	}

	cout << ddp(0, 1, 1, 0)%mod;

	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//cin >> case_;

	for (int i = 0; i < case_; i++) {
		if (sol()) break;
	}

	//while (!sol()) {

	//}


}	






