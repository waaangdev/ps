//고속도로

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));


int n,case_;
string dp[1001];
map<char, int> m = { {'(',1},{')',2},{'{',3},{'}',4},{'[',5},{']',6} };

bool strCompair(string a,string b) {//a가 더 작으면 true
	if (a.length() == b.length()) {
		bool r = true;
		for (int i = 0; i < a.length(); i++) {
			if (a[i] != b[i]) {
				r = m[a[i]] < m[b[i]];
				break;
			}
		}
		return r;
	}
	else {
		return a.length() < b.length();
	}
}


string sol(int n) {
	if (dp[n] != "") {
		return dp[n];
	}
	if (n==0) {
		return "";
	}
	if (n == 1) {return "()";}
	if (n == 2) { return "{}"; }
	if (n == 3) { return "[]"; }


	string r = "";
	string dum;
	r = "()"+ dp[n -1];

	if (n % 2 == 0) {
		dum = "(" + dp[n / 2] +")";
		if (strCompair(dum, r)) { r = dum; }
	}
	if (n % 3 == 0) {
		dum = "{" + dp[n / 3] + "}";
		if (strCompair(dum, r)) { r = dum; }
	}
	if (n % 5 == 0) {
		dum = "[" + dp[n/5] + "]";
		if (strCompair(dum, r)) { r = dum; }
	}

	for (int i = 1; i < n; i++) {
		dum = dp[n-i] + dp[i];
		if (strCompair(dum, r)) { r = dum; }
	}

	dp[n] = r;
	return r;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >>case_;
    dp[1] = "()";
    dp[2] = "{}";
    dp[3] = "[]";
	for (int i = 0; i < 1001; i++) {
		sol(i);
	}


	for (int c = 0; c < case_; c++) {
		cin >> n;

		cout << dp[n]<<'\n';
		
	}

}






