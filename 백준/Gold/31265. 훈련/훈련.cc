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


//struct llint_pair {
//	llint first;
//	llint second;
//};


//bool compare(llint_pair i, llint_pair j) {
//	if (i.first == j.first) {
//		return i.second < j.second;
//	}
//	return i.first < j.first;
//}

//struct cmp {
//	bool operator()(llint_pair a, llint_pair b) {
//		return a.first < b.first; 큰게 top
//	}
//};


//void print(vector<llint> li) {
//	for (int i = 0; i < li.size(); i++) {
//		cout << li[i] << " ";
//	}
//	cout << "\n";
//}



int n, m;
int di[1000];
int di2[1000];
int dp[10001][2][1000];
bool dp2[10001][2][1000];
vector<int> ti[1000];


int dps(int idx, int idx2, int tf, int left) {
	if (idx == n) return 0;
	if (idx2 == di[idx]) {
		if (tf)return dps(idx + 1, 0, 0, left);
		else return -1;
	}
	int i = di2[idx] + idx2;
	if (!dp2[left][tf][i]) {
		dp2[left][tf][i] = true;
		dp[left][tf][i] = -1;
		if (left >= ti[idx][idx2]) {
			int dum = dps(idx, idx2 + 1, 1, left - ti[idx][idx2]);
			if (dum != -1) dp[left][tf][i] = max(dp[left][tf][i], dum + ti[idx][idx2]);
		}

		int dum = dps(idx, idx2 + 1, tf, left);
		if (dum != -1)dp[left][tf][i] = max(dp[left][tf][i], dum);

	}
	return dp[left][tf][i];
}


int sol() {
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		cin >> di[i];
	}
	for (int i = 1; i < n; i++) {
		di2[i] = di[i - 1] + di2[i - 1];
	}

	for (int i = 0; i < n; i++) {

		for (int j = 0; j < di[i]; j++) {
			int dum;
			cin >> dum;
			ti[i].push_back(dum);

		}
	}


	cout << dps(0, 0, 0, m);
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






