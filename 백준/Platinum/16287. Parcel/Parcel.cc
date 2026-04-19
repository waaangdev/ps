//볼록껍질

#define _USE_MATH_DEFINES

#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

struct node {
	int first;
	int second;
};


int li[5000];
bool li_is[200001];
short li2[799995][50];
int li2_c[799995];
int w, n,r;

int main() {  
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> w >> n;

	for (int i = 0; i < n; i++) {
		int inp1;
		cin >> inp1;
		li[i] = inp1;
		li_is[inp1] = true;
	}
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			int dum = li[i] + li[j];
			if (dum <= w) {
				li2_c[dum] += 1;
				//li2[dum][i] += 1;
				//li2[dum][j] += 1;
			}
		}
		//cout << "a";
	}
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			int dum = li[i] + li[j];
			if (dum <= w) {
				int dum2 = w - dum;
				int dum3 = li2_c[dum2];
				if (dum2 == dum)dum3 += 1;
				if (dum2 - li[i] > 0 and dum2 - li[i] < 200001) {
					if (li_is[dum2 - li[i]]) {
						dum3 -= 1;
					}
				}if (dum2 - li[j] > 0 and dum2 - li[j] < 200001) {
					if (li_is[dum2 - li[j]]) {
						dum3 -= 1;
					}
				}
				if (dum3 > 0) {
					r = 1;
					//cout << "aaa"<< li2_c[dum2] << " " << li2[dum2][i] << " " << li2[dum2][j] << "\n";
				}
			}
		}
	}

	//for (int i = 0; i < n; i++) {
	//	for (int j = i+1; j < n; j++) {
	//		int dum = li[i] + li[j];
	//		if (dum <= w) {
	//			int dum2 = w - dum;
	//			//cout << li[i] << " " << li[j] << " " << dum2 << "\n";
	//			int dum3 = li2_c[dum2] - li2[dum2][i] - li2[dum2][j];
	//			if (dum2 == dum)dum3 += 1;
	//			if (dum3 > 0) {
	//				r = 1;
	//				//cout << "aaa"<< li2_c[dum2] << " " << li2[dum2][i] << " " << li2[dum2][j] << "\n";
	//			}
	//		}
	//	}
	//}
	if (r) {
		cout << "YES";
	}
	else {
		cout << "NO";
	}
}






