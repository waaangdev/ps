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
	int idx;
};

int n, q;
int li[100000];
int rli[100000];
vector<int_pair> li2[251];
int li3[1000001];
int sums;

bool compare(int_pair a, int_pair b) {
	if (a.first < b.first) {
		return true;
	}
	if (a.first > b.first) {
		return false;
	}
	if (a.second < b.second) {
		return true;
	}
	if (a.second > b.second) {
		return false;
	}
	return false;
}


int sol() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> li[i];
	}
	cin >> q;
	for (int i = 0; i < q; i++) {
		int l, r;
		cin >> l >> r;

		li2[(r - l) / 400].push_back({l,r,i});
	}
	for (int i = 0; i < 251; i++) {
		for (int j = 0; j < 1000001; j++) {
			li3[j] = 0;
		}
		sums = 0;
		sort(li2[i].begin(), li2[i].end(), compare);
		int pl = -1;
		int pr = -1;
		if (li2[i].size()) {
			pl = li2[i][0].first;
			pr = li2[i][0].second;

			for (int j = pl-1; j < pr; j++) {
				li3[li[j]] += 1;
				if (li3[li[j]] == 1) sums += 1;
			}

			rli[li2[i][0].idx] = sums;
		}
		for (int j = 1; j < li2[i].size(); j++) {
			for (int k = pl-1; k < li2[i][j].first-1; k++) {
				li3[li[k]] -= 1;
				if (li3[li[k]] == 0) sums -= 1;

			}
			if (pr > li2[i][j].second) {
				for (int k = li2[i][j].second; k < pr; k++) {
					li3[li[k]] -= 1;
					if (li3[li[k]] == 0) sums -= 1;

				}
			}
			else {
				for (int k = pr; k < li2[i][j].second; k++) {
					li3[li[k]] += 1;
					if (li3[li[k]] == 1) sums += 1;

				}
			}

			rli[li2[i][j].idx] = sums;

			pl = li2[i][j].first;
			pr = li2[i][j].second;
		}
	}
	
	for (int i = 0; i < q; i++) {
		cout << rli[i] << "\n";
	}

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






