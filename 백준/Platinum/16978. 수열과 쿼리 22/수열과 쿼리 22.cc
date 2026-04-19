//가장 가까운 두 점

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

struct node {
	int first;
	llint second;
	bool third;
};

#define swap(a,b,t) ((t=a),(a=b),(b=t));

llint n, q;

node queue2[100000];
int queue1[100000][2];
llint tree[18][100000];
node ans[100000];

llint sol(int l, int r, int i, int j, int num) {
	//cout << l << " " << r << " " <<i << " " <<j << " " << num << "\n";
	if (l == num * j and r == l + num) {
		return tree[i][j];
	}
	int dum = num * j + num/2;
	if (l < dum and r <= dum) {
		return sol(l, r, i - 1, j * 2, num / 2);
	}
	else if (l >= dum and r > dum) {
		return sol(l, r, i - 1, j * 2+1, num / 2);

	}
	else {
		return sol(l, dum, i - 1, j * 2, num / 2)+sol(dum, r, i - 1, j * 2 + 1, num / 2);
	}
}

bool compair(node a, node b) {
	if (a.first == b.first) {
		if (b.third == true and a.third==false) {
			return false;
		}
		else {
			if (b.third == false and a.third == true) {
				return true;
			}
			else {
				return false;
			}
		}
	}
	return a.first < b.first;
}
bool compair2(node a, node b) {
	return a.first < b.first;
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int tmp;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> tree[0][i];
	}
	int dum = n/2;
	for (int i = 1; i < 18; i++) {
		for (int j = 0; j < dum+1; j++) {
			tree[i][j] = tree[i - 1][j * 2] + tree[i - 1][j * 2 + 1];
		}
		dum /= 2;
	}


	cin >> q;
	int onetype_c = 0;
	for (int i = 0; i < q; i++) {
		int inp1, inp2, inp3;
		cin >> inp1 >> inp2 >> inp3;
		if (inp1 == 1) {
			queue2[i] = { onetype_c,i,false };
			onetype_c += 1;
			queue1[i][0] = inp2;
			queue1[i][1] = inp3;
		}
		else {
			int inp4;
			cin >> inp4;
			queue2[i] = { inp2,i,true };
			queue1[i][0] = inp3;
			queue1[i][1] = inp4;

		}
	}
	sort(queue2, queue2 + q, compair);
	int ans_c = 0;
	for (int i = 0; i < q; i++) {
		int inp1 = queue1[queue2[i].second][0];
		int inp2 = queue1[queue2[i].second][1];
		bool inp3 = queue2[i].third;

		//cout << queue2[i].second << "\n";

		if (!inp3) {
			tree[0][inp1 - 1] = inp2;
			dum = (inp1 - 1)/2;
			for (int i = 1; i < 18; i++) {
				tree[i][dum] = tree[i - 1][dum * 2] + tree[i - 1][dum * 2 + 1];
				dum /= 2;
			}
		}
		else {
			ans[ans_c].first= queue2[i].second;
			ans[ans_c].second = sol(inp1-1, inp2,17,0,pow(2,17));
			ans_c += 1;
		}
	}
	sort(ans, ans + ans_c, compair2);
	for (int i = 0; i < ans_c; i++) {
		//cout << ans[i].first <<" " << ans[i].second << '\n';
		cout << ans[i].second << '\n';
	}
}






