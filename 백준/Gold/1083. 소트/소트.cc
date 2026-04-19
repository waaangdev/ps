//디피그리디

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));

int case_ = 1;
int li[50];

void sol() {
	int n,m;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> li[i];
	}
	cin >> m;

	for (int i = 0; i < n; i++) {
		int max_ = 0;
		int max_i = 0;
		int max_i2 = 0;
		int j2 = 0;
		for (int j = 0; j < n; j++) {
			if (li[j] > max_) {
				max_ = li[j];
				max_i = j;
				max_i2 = j2;
			}
			if (li[j] != 0) {
				j2++;
			}
			if (j2 == m+1) {
				break;
			}
		}
		cout << max_ << " ";

		m -= max_i2;
		li[max_i] = 0;
	}

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//cin >> case_;
	for (int i = 0; i < case_; i++) {
		sol();
	}


}






