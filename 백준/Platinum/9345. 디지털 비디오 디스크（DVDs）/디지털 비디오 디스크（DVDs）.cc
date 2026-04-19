//디지털 비디오 디스크(DVDs)

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

struct node {
	int range[2];
};

#define swap(a,b,t) ((t=a),(a=b),(b=t));

node tree[18][100000];//범위
//int dvds[100000];//실제 dvd의 넘버
int case_;

node nodeSum(node a, node b) {
	node r = {};
	r.range[0] = min(a.range[0], b.range[0]);
	r.range[1] = max(a.range[1], b.range[1]);
	return r;
}

void treeUpdate(int j) {
	for (int i = 1; i < 18; i++) {
		j = j / 2;
		tree[i][j] = nodeSum(tree[i-1][j * 2], tree[i-1][j * 2 + 1]);
	}
}

node treeSol(int i,int j,int l,int r,int num) {
	//cout << i<<" " << j << " " << l << " " << r << " " << num << "\n";
	if (l==num*j and r == l+num) {
		return tree[i][j];
	}
	int dum = num * j + (num / 2);
	if (l < dum and r <= dum) {
		return treeSol(i - 1, j * 2, l, r, num / 2);
	}
	else if (l >= dum and r > dum) {
		return treeSol(i - 1, j * 2+1, l, r, num / 2);
	}
	else {
		node nodel = treeSol(i - 1, j * 2, l, dum, num / 2);
		node noder = treeSol(i - 1, j * 2+1, dum, r, num / 2);
		return nodeSum(nodel, noder);
	}
}

void sol() {
	int n, k;
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		//dvds[i] = i;
		tree[0][i].range[0] = i;
		tree[0][i].range[1] = i;
	}
	int dum = n;
	for (int i = 1; i < 18; i++) {
		dum = dum/2+dum%2;
		for (int j = 0; j < dum; j++) {
			tree[i][j] = nodeSum(tree[i-1][j*2], tree[i-1][j*2+1]);
		}
	}

	for (int i = 0; i < k; i++) {
		int q, a, b;
		cin >>q >> a>>b;
		if (q == 0) {
			node tmp = tree[0][a];
			tree[0][a] = tree[0][b];
			tree[0][b] = tmp;
			treeUpdate(a);
			treeUpdate(b);
		}
		else {
			node r = treeSol(17,0,a,b+1,pow(2,17));
			bool rr = true;
			if (r.range[0] == a and r.range[1] == b) {
				cout << "YES\n";
			}
			else {
				cout << "NO\n";

			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> case_;

	for (int c = 0; c< case_; c++) {
		sol();
	}
}






