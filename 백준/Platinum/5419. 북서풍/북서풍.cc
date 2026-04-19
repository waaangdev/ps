//북서풍

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));

struct pos {
	llint x;
	llint y;
};

int case_;
pos islands[75000];
llint sorty_tree[18][75001];

bool compairx(pos a, pos b) {
	if (a.x == b.x) {
		return a.y > b.y;
	}
	return a.x < b.x;
}
bool compairy(pos a, pos b) {
	if (a.y == b.y) {
		return a.x < b.x;
	}
	return a.y < b.y;
}

void treeadd(int j, int num) {
	for (int i = 0; i < 18; i++) {
		sorty_tree[i][j] += num;
		j /= 2;
	}
}

llint treeSol(int l, int r, int i, int j, int num) {
	if (l == j * num and l + num == r) {
		return sorty_tree[i][j];
	}
	llint dum = j * num + num / 2;
	if (l < dum and r <= dum) {
		return treeSol(l, r, i - 1, j * 2, num / 2);
	}
	else if (l >= dum and r > dum) {
		return treeSol(l, r, i - 1, j * 2 + 1, num / 2);
	}
	else {
		return treeSol(l, dum, i - 1, j * 2, num / 2) + treeSol(dum, r, i - 1, j * 2 + 1, num / 2);
	}
}

void sol() {
	llint n, r;
	r = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int inp1, inp2;
		cin >> inp1 >> inp2;
		islands[i] = { inp1,inp2 };
	}
	sort(islands, islands + n, compairy);

	//y좌표압축
	int dum = -1;
	int dum2 = -2000000001;
	for (int i = 0; i < n; i++) {
		if (dum2 != islands[i].y) {
			dum += 1;
			dum2 = islands[i].y;
			sorty_tree[0][dum] = 0;
		}
		islands[i].y = dum;
		sorty_tree[0][dum] += 1;

	}

	dum = n;
	for (int i = 1; i < 18; i++) {
		dum = dum / 2 + dum % 2;
		for (int j = 0; j < dum; j++) {
			sorty_tree[i][j] = sorty_tree[i - 1][j * 2] + sorty_tree[i - 1][j * 2 + 1];
		}
	}


	sort(islands, islands + n, compairx);

	for (int i = 0; i < n; i++) {
		r += treeSol(0, islands[i].y + 1, 17, 0, pow(2, 17)) - 1;
		treeadd(islands[i].y, -1);
		//cout << islands[i].x << " " << islands[i].y << "\n";

	}
	cout << r << "\n";
	//int rr;
	//cin >> rr;
	//if (rr != r) {
	//	cout << "WRONG";
	//	case_ = -1;
	//}

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> case_;

	for (int c = 0; c < case_; c++) {
		sol();
	}
}






