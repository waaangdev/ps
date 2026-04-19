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

int n, m;
string inp;

int sol() {
	int r = 0;
	int r2[2] = {0,0};
	cin >> n;
	cin >> inp;
	int lr, rr;
	lr = 0;
	rr = 0;
	for (int i = 0; i < n; i++) {
		if (inp[i] == 'H') {
			r2[0] += 1;
		}
		else {
			r2[1] += 1;
		}
	}

	if (n % 3 != 0) {
		r = 1;
	}
	if (r2[0] != n / 3 * 2) {
		r = 1;
	}
	if (r2[1] != n / 3) {
		r = 1;
	}


	int r3[2] = { 0,0 };
	for (int i = 0; i < n; i++) {
		if (inp[i] == 'H') {
			r3[0] += 1;
			r2[0] -= 1;
		}
		else {
			r2[1] -= 1;

			if (r2[0] > r2[1] and r3[0] > r3[1]) {

			}
			else {
				r = 1;
			}
			if (r2[0]-1 + r3[0]-1 == (r3[1]+r2[1])*2) {

			}
			else {
				r = 1;
			}

			r3[1] += 1;
		}
	}

	if (r==1) {
		cout << "mix";
	}
	else {
		cout << "pure";
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