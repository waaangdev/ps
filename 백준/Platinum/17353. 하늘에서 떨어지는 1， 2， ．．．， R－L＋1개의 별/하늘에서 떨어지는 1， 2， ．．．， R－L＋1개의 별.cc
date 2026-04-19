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


void print(vector<llint> li) {
	for (int i = 0; i < li.size(); i++) {
		cout << li[i] << " ";
	}
	cout << "\n";
}



llint n,q;
llint tree[18][100000][3];//값,합,겹

llint treeSol(int l, int r, int i, int j,bool mode,llint st) {
	//print({ l, r, i, j, st });
	int num = (1 << i);
	llint dum = j * num + (num >> 1);

	if (tree[i][j][2] != 0) {
		if (i != 0) {
			tree[i - 1][(j << 1)][2] += tree[i][j][2];
			tree[i - 1][(j << 1)][1] += tree[i][j][1];


			tree[i - 1][(j << 1)+1][2] += tree[i][j][2];
			tree[i - 1][(j << 1)+1][1] += tree[i][j][1]+ ((num >> 1)* tree[i][j][2]);
		}
		tree[i][j][0] += tree[i][j][1] * num + tree[i][j][2] * ((num * (num + 1)) / 2 - num);
		tree[i][j][1] = 0;
		tree[i][j][2] = 0;
	}


	if (l == j * num and l + num == r) {
		if (mode) {
			tree[i][j][1] += st;
			tree[i][j][2] += 1;
			return 0;
		}
		else {
			return tree[i][j][0];
		}
	}
	if (l < dum and r <= dum) {
		return treeSol(l, r, i - 1, j << 1,mode,st);
	}
	else if (l >= dum and r > dum) {
		return treeSol(l, r, i - 1, (j << 1) + 1, mode, st);
	}
	else {
		return treeSol(l, dum, i - 1, (j << 1), mode, st) + treeSol(dum, r, i - 1, (j << 1) + 1, mode, st+(dum-l));
	}
}

int sol() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> tree[0][i][0];
	}

	cin >> q;

	for (int i_ = 0; i_ < q; i_++) {
		int m, l, r;
		cin >> m;
		if (m == 1) {
			cin >> l >> r;
			treeSol(l-1, r, 17, 0,true,1);
		}
		else {
			cin >> l;
			cout << treeSol(l - 1, l, 17, 0, false, 1) << "\n";
		}
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






