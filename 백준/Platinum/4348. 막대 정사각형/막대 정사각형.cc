#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));
#define segment 1000000

int case_ = 1;


struct int_pair {
	int first;
	int second;
};

int counts,n,adds;
int li[20];
bool dps[3][1048576];
int dps2[3][1048576];

bool dp(int next, int bit) {
	//cout << next << " " << bitset<20>(bit) << "\n";
	if (dps2[next][bit] == counts) return dps[next][bit];
	bool r = 0;
	int dum = 0;
	int rnext = (next + 1) * adds;

	for (int i = 0; i < n; i++) {
		if (bit & (1<<i)) {
			dum += li[i];
		}
	}
	//cout << dum << " " << rnext << "\n";
	for (int i = 0; i < n; i++) {
		if (not (bit & (1 << i))) {
			if (dum + li[i] < rnext) {
				if (dp(next, bit | (1 << i))) {
					r = 1;
					break;
				}
			}
			else if (dum + li[i] == rnext) {
				if (next == 2) {
					return 1;
				}
				if (dp(next+1, bit | (1 << i))) {
					r = 1;
					break;
				}
			}
		}
	}


	dps2[next][bit] = counts;
	dps[next][bit] = r;
	return r;
}


int sol() {
	cin >> n;
	counts += 1;
	int sums = 0;
	for (int i = 0; i < n; i++) {
		cin >> li[i];
		sums += li[i];
	}
	if (sums % 4 == 0) {
		adds = sums / 4;
		if (dp(0, 0)) {
			cout << "yes\n";
		}
		else {
			cout << "no\n";
		}
	}
	else {
		cout << "no\n";
	}

	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> case_;

	for (int i = 0; i < case_; i++) {
		if (sol()) break;
	}

	//while (!sol()) {

	//}


}






