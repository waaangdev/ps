//수열과 쿼리 21

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

llint n,m;
llint tree[18][100000][2];//기존값,더해질값
bool tree2[18][100000];//갱신안되었는가

void sol(int l, int r, int i, int j, int num,int addnum) {
	if (tree2[i][j]) {
		tree[i][j][0] += tree[i][j][1]* num;
		if (i == 0) {

		}
		else {
			tree[i - 1][j*2][1] += tree[i][j][1];
			tree2[i - 1][j * 2] = true;
			tree[i - 1][j * 2+1][1] += tree[i][j][1];
			tree2[i - 1][j * 2+1] = true;
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
		sol(l, r, i - 1, j * 2+1, num / 2, addnum);

	}
	else {
		sol(l, dum, i - 1, j * 2, num / 2, addnum);
		sol(dum, r, i - 1, j * 2+1, num / 2, addnum);
	}
}

llint sol2(int i , int j,int num,int target) {
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
		return tree[i][j][0];
	}
	else {
		if (target < num * j + num / 2) {
			return sol2(i - 1, j*2, num / 2, target);
		}
		else {
			return sol2(i - 1, j * 2+1, num / 2, target);

		}
	}
}



int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);


	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> tree[0][i][0];
	}
	llint dumn = n/2;
	for (int i = 1; i < 17; i++) {
		for (int j = 0; j < dumn+1; j++) {
			tree[i][j][0] = tree[i-1][j*2][0] + tree[i-1][j*2+1][0];
			//cout << tree[i][j][0] << " ";
		}
		//cout << "\n";
		n /= 2;
	}

	cin >> m;

	for (int i = 0; i < m; i++) {
		int inp1, inp2,inp3,inp4;
		cin>> inp1 >> inp2;
		if (inp1 == 1) {
			cin >> inp3 >> inp4;
			sol(inp2 - 1, inp3, 17, 0, pow(2, 17), inp4);
		}
		else {
			inp2 -= 1;
			cout << sol2(17, 0, pow(2, 17), inp2) <<"\n";
		}
	}
}






