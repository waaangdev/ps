//배열 알아맞히기

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

llint q,t,k;
llint tree[21][1000000];
bool tree2[21][1000000];
bool tree3[21][1000000];


llint sol(int i, int j) {
	if (i == 0) {
		return tree[i][j];
	}
	if (tree2[i][j]) {
		return tree[i][j];
	}
	else {
		if (tree2[i - 1][j * 2]) {
			llint r = tree[i - 1][j * 2];
			if (tree3[i - 1][j * 2 + 1]) {
				r += sol(i - 1, j * 2 + 1);
			}
			return r;
		}
		else {
			if (tree3[i - 1][j * 2]) {
				return sol(i - 1, j * 2);
			}
			else {
				return 0;
			}
		}
		

	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);


	cin >> q;
	for (int i = 0; i < q; i++) {
		cin >> t >> k;
		
		k -= 1;
		if (t == 1) {
			tree[0][k] += 1;
		}
		else {
			tree[0][k] -= 1;
		}
		tree2[0][k] = false;
		if(tree[0][k] != 0) tree2[0][k] = true;
		tree3[0][k] = false;
		if (tree[0][k] != 0) tree3[0][k] = true;
		k /= 2;
		for (int i = 1; i < 21; i++) {
			tree[i][k] = tree[i-1][k*2]+ tree[i - 1][k * 2+1];
			tree2[i][k] = tree2[i - 1][k * 2] and tree2[i - 1][k * 2 + 1];
			tree3[i][k] = tree3[i - 1][k * 2] or tree3[i - 1][k * 2 + 1];
			k /= 2;
		
		}

		cout << sol(20, 0) << "\n";
	}
}






