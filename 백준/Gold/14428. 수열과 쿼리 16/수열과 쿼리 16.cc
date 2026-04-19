#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

typedef struct st {
	int first, second;
} node;

llint n, m;
node tree[17][100000];

node solve(llint l, llint r, llint i, llint j, llint a) {
	//cout << l << " " <<r << " " << i << " " << j << " " << a << "\n";
	if (l == j * a and r == l + a) {
		return tree[i][j];
	}
	if (l < j * a + a / 2 and r <= j * a + a / 2) {
		return solve(l, r, i - 1, j * 2, a / 2);
	}
	else if (l >= j * a + a / 2 and r > j * a + a / 2) {
		return solve(l, r, i - 1, j * 2 + 1, a / 2);
	}
	else {
		node ret, ret2;
		ret = solve(l, j * a + a / 2, i - 1, j * 2, a / 2);
		ret2 = solve(j * a + a / 2, r, i - 1, j * 2 + 1, a / 2);
		if (ret2.first < ret.first) {
			ret = ret2;
		}
		return ret;
	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	int dum = n;
	int AAA = pow(2, 17);
	//for (int i = 0; i < 17; i++) {
	//	cout << tree[i].size() << "\n";
	//}

	for (int i = 0; i < n; i++) {
		cin >> tree[0][i].first;
		tree[0][i].second = i;
	}
	dum = n / 2;
	for (int i = 1; i < 17; i++) {
		for (int j = 0; j < dum; j++) {
			if (tree[i - 1][j * 2].first > tree[i - 1][j * 2 + 1].first and tree[i - 1][j * 2 + 1].first != 0) {
				tree[i][j].first = tree[i - 1][j * 2 + 1].first;
				tree[i][j].second = tree[i - 1][j * 2 + 1].second;
			}
			else {
				tree[i][j].first = tree[i - 1][j * 2].first;
				tree[i][j].second = tree[i - 1][j * 2].second;
			}
		}
		dum /= 2;
	}

	cin >> m;
	for (int i2 = 0; i2 < m; i2++) {
		int inp1, inp2, inp3;
		cin >> inp1 >> inp2 >> inp3;
		inp2 -= 1;
		if (inp1 == 1) {
			tree[0][inp2].first = inp3;
			int dum2 = inp2 / 2;
			for (int i = 1; i < 17; i++) {
				int dum4 = dum2 * 2 + 1;
				if (tree[i - 1][dum2 * 2].first > tree[i - 1][dum4].first and tree[i - 1][dum4].first != 0) {
					tree[i][dum2].first = tree[i - 1][dum4].first;
					tree[i][dum2].second = tree[i - 1][dum4].second;
				}
				else {
					tree[i][dum2].first = tree[i - 1][dum2 * 2].first;
					tree[i][dum2].second = tree[i - 1][dum2 * 2].second;
				}
				dum2 /= 2;
			}
		}
		else {
			int dum2 = solve(inp2, inp3, 17, 0, AAA).second + 1;
			cout << dum2 << "\n";

			//int dum3, dum4;
			//dum3 = 1000000001;
			//for (int i = inp2; i < inp3; i++) {
			//	if (tree[0][i].first < dum3) {
			//		dum3 = tree[0][i].first;
			//		dum4 = i;
			//	}
			//}

			//if (dum2 != dum4) {
			//	cout << "--------------LOL-------------";
			//}
		}
	}

}