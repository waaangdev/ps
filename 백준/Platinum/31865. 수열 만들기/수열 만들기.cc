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

int n, m;
int tree[20][300000];
int pos[300000];
int li[300000];


void treeadd(int idx) {
	for (int i = 0; i < 20; i++) {
		tree[i][idx] += 1;
		idx = (idx >> 1);
	}
}

int seg(int l, int r, int idx, int d) {
	int num = (1 << d);
	if (l == r) return 0;
	if (l == (idx << d) and r == l + num) {
		return tree[d][idx];
	}
	int mid = (idx << d) + (1 << (d - 1));
	if (l < mid and r <= mid) {
		return seg(l, r, (idx << 1), d - 1);
	}
	if (l >= mid and r > mid) {
		return seg(l, r, (idx << 1) + 1, d - 1);
	}
	return seg(l, mid, (idx << 1), d - 1) + seg(mid, r, (idx << 1) + 1, d - 1);
}

int sol() {
	cin >> n;
	//for (int i = 0; i < n; i++) {
	//	tree[0][i] = 1;
	//}
	//int dum = n;
	//for (int i = 1; i < 20; i++) {
	//	dum = (dum >> 1) + (dum & 1);
	//	for (int j = 0; j < dum; j++) {
	//		tree[i][j] = tree[i-1][(j<<1)]+ tree[i - 1][(j << 1)+1];
	//	}
	//}
	treeadd(0);
	pos[0] = 0;
	li[0] = 0;

	for (int i = 1; i < n; i++) {
		int p, x;
		cin >> p >> x;
		p -= 1;
		int cnt = pos[p] - seg(0, pos[p], 0, 19) + x;

		if (cnt % (n - tree[19][0])==0 and cnt !=0) {
			cnt = n - tree[19][0];
		}
		else {
			cnt %= (n - tree[19][0]);
		}
		//cout <<"- " << cnt << ' ';

		int idx = 0;
		int d = 19;
		while (d > -1) {
			int dum = (1 << d) - tree[d][idx];
			if (dum >= cnt) {
				idx = (idx << 1);
				d -= 1;
			}
			else if (dum < cnt) {
				idx += 1;
				cnt -= dum;
			}
		}
		idx = idx >> 1;
		li[idx] = i;
		pos[i] = idx;
		treeadd(idx);
		//cout << idx << "";
		//if (1) {
		//	int dum = n*2;
		//	for (int ii = 0; ii < 20; ii++) {
		//		dum = (dum >> 1) + (dum & 1);
		//		cout << "\n- ";
		//		for (int j = 0; j < dum; j++) {
		//			cout << tree[ii][j]<< " ";
		//		}
		//		if (dum == 1)break;
		//	}
		//}
		//cout << '\n';
	}

	for (int i = 0; i < n; i++) {
		cout << li[i] + 1 << "\n";
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






