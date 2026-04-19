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

int r[100];
int dp[50][50][50][3][2],dpnum;

bool sol2(int num, int idx, int add,int len) {
	int p = 0;
	for (int i = 0; i < num; i++) {
		if (p >= len) { return false; }
		while (r[p] != 0) {
			p += 1;
		}
		if (p >= len) { return false; }
		r[p] = idx;
		p += add;
	}
	return true;
}

string sol3(int a, int b, int c, int c2, int b2) {
	if (a == 0 and b == 0 and c == 0) {
		return "";
	}
	if (c2 != 0) c2 -= 1;
	if (b2 != 0) b2 -= 1;
	if (dp[a][b][c][c2][b2] == dpnum) {
		return "-1";
	}
	if (c2 == 0 and c > 0) {
		string str = sol3(a, b, c - 1, 3, b2);
		if (str != "-1") {
			return "C"+ str;
		}
	}
	if (b2 == 0 and b >0) {
		string str = sol3(a, b-1, c, c2, 2);
		if (str != "-1") {
			return "B" + str;
		}

	}
	if (a > 0) {
		string str = sol3(a-1, b, c, c2, b2);
		if (str != "-1") {
			return "A" + str;
		}
	}
	dp[a][b][c][c2][b2] = dpnum;
	return "-1";

	
}

int sol() {
	string str;
	string strr2 = "";
	cin >> str;


	for (int i = 0; i < str.length(); i++) {
		r[i] = 0;
	}
	int r2 = 0;
	int count[3] = {0,0,0};
	for (int i = 0; i < str.length(); i++) {
		count[str[i] - 'A'] += 1;
	}
	if (!sol2(count[2], 2, 3, str.length())) r2 = 1;
	if (!sol2(count[1], 1, 2, str.length())) r2 = 1;
	if (r2) {
		for (int i = 0; i < str.length(); i++) {
			r[i] = 0;
		}
		r2 = 0;

		if (!sol2(count[1], 1, 2, str.length())) r2 = 1;
		if (!sol2(count[2], 2, 3, str.length())) r2 = 1;

		if (r2) {
			strr2 = "-1";
		}


	}
	if (strr2 == "") {
		for (int i = 0; i < str.length(); i++) {
			strr2 += "ABC"[r[i]];
		}
	}
	//cout <<"1 " << strr2 << "\n";

	dpnum += 1;
	string strr = sol3(count[0], count[1], count[2], 0, 0);
	cout << strr<<"\n";
	if ((strr2 == "-1") != (strr == "-1")) {
		return 1;
	}
	return 1;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//cin >> case_;
	 
	//for (int i = 0; i < case_; i++) {
	//	sol();
	//}

	while (!sol()) {

	}


}






