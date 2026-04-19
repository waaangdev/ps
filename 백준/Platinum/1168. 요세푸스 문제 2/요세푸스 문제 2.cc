#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));
#define DMAX 18

int case_ = 1;


struct int_pair {
	int first;
	int second;
};

int n, k;
int tree[1 << 18];

int treeUpdate(int idx) {
	for (int i = 0; i < DMAX; i++) {
		tree[idx] += 1;
		idx = (idx >> 1);
	}
	return 0;
}

int findIdx(int d, int idx, int score) {
	//cout << d << " " << idx << " " << score << "\n";
	int nd = n;
	int dum = nd -tree[idx];

	while (dum != score or d != 0) {
		int ndhis = nd;
		idx = (idx << 1);
		d -= 1;
		nd = min(nd, (1 << (d)));
		dum = nd -tree[idx];
		//cout << d << " " << idx- (1 << (17-d)) << " "<< " "<<dum << " "<< nd <<" "<<score << "\n";
		if (dum < score) {
			idx += 1;
			score -= dum;
			nd = ndhis - (1 << (d));
			if (d == 0) {
				return idx;
			}
		}
	}
	return idx;
}

int treeSet(int n) {
	for (int j = 0; j < n; j++) {
		tree[(1 << (DMAX - 1)) + j] = 1;
	}
	for (int i = (1 << (DMAX - 1)) - 1; i > 0; i--) {
		tree[i] = tree[(i << 1)] + tree[(i << 1) + 1];
	}
	return 0;
}


int sol() {
	cin >> n >> k;
	int k2 = k;
	int idx = 0;
	cout << "<";
	for (int i = 0; i < n; i++) {
		idx = (findIdx(17, 1, k2));
		k2 += k - 1;
		if (k2 > n-tree[1]) k2 = -(n-tree[1]) + k2 + 1;
		treeUpdate(idx);
		cout << idx + 1 - (1 << (DMAX - 1));
		if (i == n - 1) { cout << ">\n"; break; }
		else cout << ", ";

		k2 %= n-tree[1];
		if (k2 == 0) k2 += n-tree[1];
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






