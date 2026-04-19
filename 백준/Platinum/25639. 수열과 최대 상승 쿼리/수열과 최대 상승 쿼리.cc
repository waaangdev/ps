//테트리스

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));

struct node {
	llint left;
	llint right;
	llint maxs;
};

int case_ = 1;
node tree[200022];
llint ili[19];
llint debug[100000];

node nodeMerge(node l, node r) {
	node rr = { min(l.left,r.left),max(l.right,r.right) ,max(l.maxs,r.maxs)};
	rr.maxs = max(rr.maxs, r.right - l.left);
	return rr;
}

node treeMax(int l,int r,int i,int j,int num) {
	//cout << l << " " << r << " " << i << " " << j << " " << num << "\n";
	if (l == j * num and r == l+num) {
		return tree[ili[i] + j];
	}
	int dum = j * num + (num >> 1);
	if (l < dum and r <= dum) {
		return treeMax(l, r, i - 1, j * 2, num >> 1);
	}
	else if (l >= dum and r > dum) {
		return treeMax(l, r, i - 1, j * 2+1, num >> 1);
	}
	else {
		return nodeMerge(treeMax(l, dum, i - 1, j * 2, num >> 1), treeMax(dum, r, i - 1, j * 2 + 1, num >> 1));
	}
}


void sol() {
	int n, q;
	cin >> n;
	int dum = 0;
	int dum2 = n;
	for (int i = 0; i < 19; i++) {
		ili[i] = dum;
		dum += dum2;
		dum2 = dum2 / 2 + dum2 % 2;
		//cout << ili[i] << "\n";
	}
	for (int i = 0; i < n; i++) {
		cin >> dum;
		debug[i] = dum;
		tree[i] = { dum ,dum,0};
	}
	for (int i = 1; i < 18; i++) {
		for (int j = 0; j < ili[i+1]-ili[i]; j++) {
			if (ili[i - 1] + j * 2 + 1 != ili[i]) {
				tree[ili[i] + j] = nodeMerge(tree[ili[i - 1] + j * 2], tree[ili[i - 1] + j * 2 + 1]); 
			}
			else {
				tree[ili[i] + j] = tree[ili[i - 1] + j * 2];
			}
			//if (j < 6) cout << "(" << tree[ili[i] + j].left << "," << tree[ili[i] + j].maxs << "," << tree[ili[i] + j].right << ") ";

		}
		//cout << '\n';
	}

	cin >> q;
	int inp[3];
	for (int i1 = 0; i1 < q; i1++) {
		cin >> inp[0] >> inp[1] >> inp[2];

		if (inp[0] == 1) {
			debug[inp[1] - 1] = inp[2];

			dum = inp[1] - 1;
			tree[dum] = { inp[2],inp[2] ,0 };
			for (int i = 1; i < 18; i++) {
				dum = dum / 2;
				if (ili[i - 1] + dum * 2 + 1 != ili[i]) {
					tree[ili[i]+dum] = nodeMerge(tree[ili[i - 1] + dum * 2], tree[ili[i - 1] + dum * 2 + 1]);
				}
				else {
					tree[ili[i] + dum] = tree[ili[i - 1] + dum * 2];
				}
			}
		}
		else {
			llint rr = treeMax(inp[1] - 1, inp[2], 17, 0, 1 << 17).maxs;
			cout << rr << "\n";

			//llint debugmax = 0;
			//for (int i = inp[1] - 1; i < inp[2]-1; i++) {
			//	debugmax = max(debugmax, debug[i + 1] - debug[i]);
			//}
			//cout << debugmax << "\n";
			//if (debugmax != rr) {
			//	cout << "NOOOOOOOOOOO\n";
			//	break;
			//}
		}

		//for (int i = 0; i < 18; i++) {
		//	for (int j = 0; j < ili[i + 1] - ili[i]; j++) {
		//		if (j < 6) cout << "(" << tree[ili[i] + j].left << "," << tree[ili[i] + j].maxs << "," << tree[ili[i] + j].right << ") ";

		//	}
		//	cout << '\n';
		//}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//cin >> case_;
	for (int i = 0; i < case_; i++) {
		sol();
	}


}






