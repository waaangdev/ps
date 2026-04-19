	//

	#define _USE_MATH_DEFINES
	#include <bits/stdc++.h>
	#include <algorithm>
	#include <sstream>

	using namespace std;

	typedef long long int llint;

	struct node {
		int length_l;
		int length_r;
		int length_c;
		bool l;//L은 false, R은 true
		bool r;
	};

	#define swap(a,b,t) ((t=a),(a=b),(b=t));

	node tree[19][200000];
	int n, q;

	int main() {
		ios_base::sync_with_stdio(false);
		cin.tie(0);
		cout.tie(0);


		cin >> n >> q;

		int dumn = n;
		int dumn2 = 0;
		for (int i = 0; i < 19; i++) {
			for (int j = 0; j < dumn; j++) {
				tree[i][j].length_c = 1;
				tree[i][j].length_l = 1;
				tree[i][j].length_r = 1;
			}
			dumn = dumn/2 + dumn%2;
		}

		for (int qi = 0; qi < q; qi++) {
			int inp, dum;
			cin >> inp;
			inp -= 1;
			tree[0][inp].l = !tree[0][inp].l;
			tree[0][inp].r = !tree[0][inp].r;

			inp /= 2;
			dum = 2;
			for (int i = 1; i < 19; i++) {
				node nodel = tree[i - 1][inp * 2];
				node noder = tree[i - 1][inp * 2 + 1];

				tree[i][inp].l = nodel.l;
				tree[i][inp].r = noder.r;

				tree[i][inp].length_l = nodel.length_l;
				tree[i][inp].length_r = noder.length_r;

				tree[i][inp].length_c = -1;
				if (nodel.r != noder.l) {
					//cout << "aaa\n";
					tree[i][inp].length_c = nodel.length_r + noder.length_l;
					if (noder.length_r == dum / 2) {
						tree[i][inp].length_r = tree[i][inp].length_c;
					}
					if (nodel.length_l == dum / 2) {
						tree[i][inp].length_l = tree[i][inp].length_c;
					}
				}
				tree[i][inp].length_c = max(max(tree[i][inp].length_c, nodel.length_c), noder.length_c);

				//cout << tree[i][inp].length_l << " " << tree[i][inp].length_c << " " << tree[i][inp].length_r << "\n";
				inp /= 2;
				dum *= 2;
			}

			cout << max(max(tree[18][0].length_c, tree[18][0].length_r), tree[18][0].length_l) << "\n";
		}


	}






