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


struct int_pair {
	int first;
	int second;
};

int n;
ullint MOD= 1.8446744e+19;
ullint li[2][200000];;

bool fun(ullint x) {
	ullint value = x;
	for (int i = 0; i < n; i++) {
		if (li[0][i] <= x and li[1][i] >= x) {
			value = value ^ (((x | li[0][i]) + (x & li[1][i]) * (li[0][i] ^ li[1][i])) % MOD);
		}
	}
	return (value >= 0x0123456789ABCDEF);
}


int sol() {
	cin >> n;

	for (int j = 0; j < 2; j++) {
		for (int i = 0; i < n; i++) {
			cin >> li[j][i];
		}
	}
	
	ullint l = 0;
	ullint r = 1000000000000000000+1;

	while (l+1 < r) {
		ullint dum = (l + r) / 2;
		bool dum2 = fun(dum);


		if (dum2) {
			if (dum != 0) {
				if (fun(dum - 1) == false) {
					cout << dum - 1;
					return 0;
				}
			}
			r = dum;
		}
		else {
			if (dum != 0) {
				if (fun(dum + 1) == true) {
					cout << dum;
					return 0;
				}
			}
			l = dum;
		}
	}
	if (fun(l + 1) == true) {
		cout << l;
		return 0;
	}
	cout << -1;


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






