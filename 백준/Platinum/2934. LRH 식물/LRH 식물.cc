//LRH 식물

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

llint n,rr;
llint tree[18][100000][2];//기존값,더해질값
bool tree2[18][100000];//갱신안되었는가

void sol(int l, int r, int i, int j, int num, int addnum) {
	if (tree2[i][j]) {
		tree[i][j][0] += tree[i][j][1] * num;
		if (i == 0) {

		}
		else {
			tree[i - 1][j * 2][1] += tree[i][j][1];
			tree2[i - 1][j * 2] = true;
			tree[i - 1][j * 2 + 1][1] += tree[i][j][1];
			tree2[i - 1][j * 2 + 1] = true;
		}
		tree2[i][j] = false;
		tree[i][j][1] = 0;
	}
	int dum = num * j + num / 2;
	if (i == 0) {

	}
	if (l == num * j and l + num == r) {
		tree[i][j][1] += addnum;
		tree2[i][j] = true;
	}
	else if (l < dum and r <= dum) {
		sol(l, r, i - 1, j * 2, num / 2, addnum);
	}
	else if (l >= dum and r > dum) {
		sol(l, r, i - 1, j * 2 + 1, num / 2, addnum);

	}
	else {
		sol(l, dum, i - 1, j * 2, num / 2, addnum);
		sol(dum, r, i - 1, j * 2 + 1, num / 2, addnum);
	}
}

llint sol2(int i, int j, int num, int target) {
	if (tree2[i][j]) {
		tree[i][j][0] += tree[i][j][1] * num;
		if (i == 0) {

		}
		else {
			tree[i - 1][j * 2][1] += tree[i][j][1];
			tree2[i - 1][j * 2] = true;
			tree[i - 1][j * 2 + 1][1] += tree[i][j][1];
			tree2[i - 1][j * 2 + 1] = true;
		}
		tree2[i][j] = false;
		tree[i][j][1] = 0;
	}
	if (i == 0) {
		if (tree[i][j][0] > 0) { tree[i][j][1] -= tree[i][j][0]; tree2[i][j] = true;
		}
		return tree[i][j][0];
	}
	else {
		if (target < num * j + num / 2) {
			return sol2(i - 1, j * 2, num / 2, target);
		}
		else {
			return sol2(i - 1, j * 2 + 1, num / 2, target);

		}
	}
}



int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	for (int i = 0; i < n; i++) {
		int l, r;
		cin >> l >> r;
		l -= 1;
		r -= 1;

		if (l + 1 < r) {
			sol(l + 1, r, 17, 0, pow(2, 17), 1);
		}
		cout << sol2(17, 0, pow(2, 17), l) + sol2(17, 0, pow(2, 17), r) <<"\n";

		//llint dumn = 10;
		//for (int i = 0; i < 17; i++) {
		//	for (int j = 0; j < dumn + 1; j++) {
		//		cout << tree[i][j][0]+ tree[i][j][1] << " ";
		//	}
		//	cout << "\n";
		//	dumn /= 2;
		//}
	}

}






