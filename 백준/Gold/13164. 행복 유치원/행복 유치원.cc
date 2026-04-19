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

int li[300000];
int li2[300000];

int sol(int case_) {
	int n,m,r;
	r = 0;
	cin >> n >> m;
	for(int i = 0; i < n;i++){
		cin >> li[i];
	}
	for (int i = 0; i < n-1; i++) {
		li2[i] = li[i+1]- li[i];
		r += li2[i];
	}

	sort(li2, li2 + n - 1);
	for (int i = 0; i < m - 1; i++) {
		r -= li2[n - 2-i];
	}
	cout << r;

	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//cin >> case_;


	for (int i = 0; i < case_; i++) {
		sol(i);
	}

	//while (!sol()) {

	//}


}