//연속합과 쿼리

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

struct node {
	int r;
	int l;
	int c;
	int l_len;
	int r_len;
	int all;
};

#define swap(a,b,t) ((t=a),(a=b),(b=t));

node tree[18][100000];
int n, q;

node sol(int l,int r,int i,int j,int num) {
	if (l == num * j and r == l + num) {
		return tree[i][j];
	}
	int dum = j * num + num / 2;
	if (l < dum and r <= dum) {
		return sol(l, r, i - 1, j * 2, num / 2);
	}
	else if (l >= dum and r > dum) {
		return sol(l, r, i - 1, j * 2+1, num / 2);
	}
	else {
		node nodel = sol(l, dum, i - 1, j * 2, num / 2);
		node noder = sol(dum, r, i - 1, j * 2+1, num / 2);
		node r = {0,0,0};
		r.l = nodel.l;
		r.l_len = nodel.l_len;
		r.r = noder.r;
		r.r_len = noder.r_len;
		if (nodel.l_len == num/2) {  
			if (noder.l >= 0) {
				r.l = nodel.l + noder.l;
				r.l_len = nodel.l_len + noder.l_len;
			}
		}
		if (noder.r_len == num / 2) {
			if (nodel.r >= 0) {
				r.r = nodel.r + noder.r;
				r.r_len = noder.r_len + nodel.r_len;
			}
		}
		r.c = noder.l+ nodel.r;
		r.c = max(max(r.c, nodel.c), noder.c);

		if (r.l_len == num and r.l >= r.r) {
			r.r = r.l;
			r.r_len = r.l_len;
		}
		if (r.r_len == num and r.r >= r.l) {
			r.l = r.r;
			r.l_len = r.r_len;
		}

		r.all = nodel.all + noder.all;
		if (nodel.all + noder.l >= r.l) {
			r.l = nodel.all + noder.l;
			r.l_len = num/2 + noder.l_len;
		}
		if (noder.all + nodel.r >= r.r) {
			r.r = noder.all + nodel.r;
			r.r_len = num / 2 + nodel.r_len;
		}

		return r;
	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);


	cin >> n;

	for (int i = 0; i < n; i++) {
		int inp;
		cin >> inp;
		tree[0][i] = {inp ,inp ,inp ,1,1,inp};
	}

	int dumn = n/2+ n % 2;
	int dum2 = 1;
	for (int i = 1; i < 18; i++) {
		for (int j = 0; j < dumn; j++) {
			node nodel = tree[i - 1][j * 2];
			node noder = tree[i - 1][j * 2 + 1];

			tree[i][j].l = nodel.l;
			tree[i][j].l_len = nodel.l_len;
			tree[i][j].r = noder.r;
			tree[i][j].r_len = noder.r_len;
			if (nodel.l_len == dum2) {
				if (noder.l >= 0) {
					tree[i][j].l = nodel.l+ noder.l;
					tree[i][j].l_len = nodel.l_len+ noder.l_len;
				}
			}
			//if (nodel.r_len == dum2) {
			//	if (noder.l >= 0) {
			//		tree[i][j].l = nodel.l + noder.l;
			//		tree[i][j].l_len = nodel.l_len + noder.l_len;
			//	}
			//}
			if (noder.r_len == dum2) {
				if (nodel.r >= 0) {
					tree[i][j].r = nodel.r + noder.r;
					tree[i][j].r_len = noder.r_len + nodel.r_len;
				}
			}
			

			tree[i][j].c = nodel.r+noder.l;

			tree[i][j].c = max(max(tree[i][j].c, nodel.c), noder.c);

			if (tree[i][j].l_len == dum2*2 and tree[i][j].l >= tree[i][j].r) {
				tree[i][j].r = tree[i][j].l;
				tree[i][j].r_len = tree[i][j].l_len;
			}
			if (tree[i][j].r_len == dum2 * 2 and tree[i][j].r >= tree[i][j].l) {
				tree[i][j].l = tree[i][j].r;
				tree[i][j].l_len = tree[i][j].r_len;
			}

			tree[i][j].all = nodel.all + noder.all;
			if (nodel.all + noder.l >= tree[i][j].l) {
				tree[i][j].l = nodel.all + noder.l;
				tree[i][j].l_len = dum2+ noder.l_len;
			}
			if (noder.all + nodel.r >= tree[i][j].r) {
				tree[i][j].r = noder.all + nodel.r;
				tree[i][j].r_len = dum2 + nodel.r_len;
			}

			//cout << tree[i][j].l << "("<< tree[i][j].l_len << ") "<< tree[i][j].c<<" " << tree[i][j].r << "(" << tree[i][j].r_len << ") " " | ";


		}
		//cout << "\n";
		dumn = dumn/2 + dumn%2;
		dum2 *= 2;
	}
	cin >> q;

	for (int qi = 0; qi < q; qi++) {
		int inp1, inp2;
		cin >> inp1 >> inp2;
		node r = sol(inp1-1,inp2,17,0,pow(2,17));
		cout << max(max(r.c,r.r),r.l)<<"\n";


	}


}






