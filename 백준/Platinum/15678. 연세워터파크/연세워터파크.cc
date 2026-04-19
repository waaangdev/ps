//연세워터파크

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


int li[100000];
llint dp[100000];
vector<llint> dp2;
int n, d;

llint r;

//llint sol(int p,int sc) {
//	if (p >= n) return 0;
//	if (dp2[p]) {
//		return dp[p];
//	}
//	sc += li[p];
//	llint r = 0;
//	for (int i = 1; i <= d; i++) {
//		llint dum = sol(p+i, sc);
//		r = max(r, dum);
//	}
//	r = max(r, r - sc + li[p]);
//	dp[p] = r;
//	dp2[p] = true;
//	return r;
//
//}
//llint sol(int p) {
//	if (p >= n) return 0;
//	if (dp2[p]) {
//		return dp[p];
//	}
//	llint r = li[p];
//	for (int i = 1; i <= d; i++) {
//		llint dum = sol(p+i)+li[p];
//		r = max(r, dum);
//	}
//	dp[p] = r;
//	dp2[p] = true;
//	return r;
//
//}


void sortInsert(llint a) {
	if (dp2.size() == 0) {
		dp2.insert(dp2.begin()+0, a);
		return;
	}
	int p1, p2;
	p1 = 0;
	p2 = dp2.size();
	while (p2 - p1 > 0) {
		int dum = (p1 + p2) / 2;
		if (dp2[dum] > a) {
			if (p2 == dum)
				break;
			p2 = dum;
		}
		else {
			if (p1 == dum)
				break;
			p1 = dum;
		}
	}
	dp2.insert(dp2.begin() + p2, a);
}

void sortDelete(llint a) {
	if (dp2.size() == 0) {
		return;
	}
	int p1, p2;
	p1 = 0;
	p2 = dp2.size();
	while (p2 - p1 > 0) {
		int dum = (p1 + p2) / 2;
		if (dp2[dum] > a) {
			if (p2 == dum)
				break;
			p2 = dum;
		}
		else {
			if (p1 == dum)
				break;
			p1 = dum;
		}
	}
	dp2.erase(dp2.begin() + p1);
}



int main() {  
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> d;
	
	
	for (int i = 0; i < n; i++) {
		llint inp1;
		cin >> inp1;
		li[i] = inp1;
		
	}
	r = li[0];

	for (int i = n - 1; i > -1; i--) {
		llint dum = li[i];

		if (dp2.size() != 0) {
			dum = max(dum, dp2[dp2.size()-1] + li[i]);
		}
		sortInsert(dum);
		if (dp2.size() > d) {
			sortDelete(dp[i + d]);
			//cout <<	"insert "<<dum << "   delete " << dp[i + d] << "\n";
		}
		//for (int j =0; j < dp2.size(); j++) {
		//	cout << dp2[j] << " ";
		//}
		//cout << " \n";
		//for (int j = i + 1; j < min(n, i + d + 1); j++) {
		//	dum = max(dum, dp[j] + li[i]);
		//}
		dp[i] = dum;

	}


	//sol(0);
	for (int i = 0; i < n; i++) {
		r = max(r, dp[i]);
		//cout << dp[i] << " ";
	}
	//cout << "\n";
	cout << r;

}






