//고속도로

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));


int n, r;
int li[200000];
int li4[200000];
int li5[200000];
int li6[200000];//kmp
//vector<int> li2[360000];
//int li3[360000];//값이 n이 되면 됨

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;

	for (int i = 0; i < n; i++) {
		int inp;
		cin >> inp;
		li[i] = inp;
	}
	sort(li, li + n);
	int his = li[0];
	for (int i = 1; i < n; i++) {
		//li2[li[i] - his].push_back(i - 1);
		li4[i - 1] = li[i] - his;
		//cout << li[i] - his << "\n";
		his = li[i];
	}
	li4[n - 1] = li[0] + 360000 - his;
	//li2[li[0]+360000- his].push_back(n - 1);
	//cout << li[0] + 360000 - his << "\n";


	for (int i = 0; i < n; i++) {
		int inp;
		cin >> inp;
		li[i] = inp;
	}
	sort(li, li + n);
	his = li[0];
	for (int i = 0; i < n; i++) {
		int dum;
		if (i == n - 1) {
			dum = li[0] + 360000 - his;
		}
		else {
			dum = li[i + 1] - his;
		}
		//cout << dum << "\n";


		li5[i] = dum;

		//for (auto iter = li2[dum].begin(); iter != li2[dum].end(); iter++) {
		//	if ((*iter) < i) {
		//		li3[(*iter) + n - i] += 1;
		//	}
		//	else {
		//		li3[(*iter) - i] += 1;
		//	}
		//}


		if (i == n - 1) {
			break;
		}
		his = li[i + 1];
	}
	//for (int i = 0; i < 360000; i++){
	//	if (li3[i] == n) {
	//		r = 1;
	//	}

	//}




	int p1 = 1;
	int p2 = 0;
	for (int i = 0; i < n; i++) {
		if (li5[p1] == li5[p2]) {
			li6[p1] = p2 + 1;
			p1++;
			p2++;
		}
		else {
			if (p2 == 0) {
				p1++;
			}
			p2 = li6[p2 - 1];
		}

	}
	p1 = 0;
	p2 = 0;//부분문자열
	for (int i = 0; i < n * 2; i++) {
		if (li5[p2] == li4[p1]) {
			p1++;
			p2++;
		}
		else {
			if (p2 == 0) {
				p1++;
			}
			p2 = li6[p2-1];
		}
		if (p2 == n) {
			r = 1;
			break;
		}
		p1 = p1 % n;
	}


	if (r == 1) {
		cout << "possible";
	}
	else {
		cout << "impossible";
	}


}






