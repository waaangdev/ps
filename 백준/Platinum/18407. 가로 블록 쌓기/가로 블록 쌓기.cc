//가장 가까운 두 점

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

struct node {
	int left;
	int value;
	bool value2;//갱신여부,그니까 이 밑에껀 전부다 내거다 라는뜻
	int right;
};

#define swap(a,b,t) ((t=a),(a=b),(b=t));

llint n,r;

node li[16000000];
int li_c;


int sol(int l, int r, llint j, llint no, llint num) {
	if (l == j * num and r == l + num) {
		//cout << l << " " << r << " " << j << " " << num << " end\n";
		return li[no].value;
	}
	//cout << l << " " << r << " " << j << " " << num << "\n";

	if (li[no].value2 and num != 1) {
		li[no].value2 = false;
		if (li[no].left == 0) {
			li_c += 1;
			li[no].left = li_c;
		}
		li[li[no].left].value = li[no].value;
		li[li[no].left].value2 = true;
		if (li[no].right == 0) {
			li_c += 1;
			li[no].right = li_c;
		}
		li[li[no].right].value = li[no].value;
		li[li[no].right].value2 = true;
	}
	llint dum = j * num + num / 2;
	if (l < dum and r <= dum) {
		if (li[no].left == 0) {
			li_c += 1;
			li[no].left = li_c;
		}
		return  sol(l, r, j*2, li[no].left, num/2);
	}
	else if (l >= dum and r > dum) {
		if (li[no].right == 0) {
			li_c += 1;
			li[no].right = li_c;
		}
		return  sol(l, r, j * 2+1, li[no].right, num / 2);
	}
	else {
		if (li[no].left == 0) {
			li_c += 1;
			li[no].left = li_c;
		}
		if (li[no].right == 0) {
			li_c += 1;
			li[no].right = li_c;
		}
		return max(sol(l, dum, j * 2, li[no].left, num / 2), sol(dum, r, j * 2+1, li[no].right, num / 2));
	}

}

void sol2(int l, int r, llint j, llint no, llint num,llint numset) {
	if (li[no].value < numset) {
		li[no].value = numset;
	}
	if (l == j * num and r == l + num) {
		li[no].value2 = true;
		//cout << l << " " << r << " " << j << " " << num << " end\n";
		return;
	}
	//cout << l << " " << r << " " << j << " " << num << "\n";

	if (li[no].value2 and num != 1) {
		li[no].value2 = false;
		if (li[no].left == 0) {
			li_c += 1;
			li[no].left = li_c;
		}
		li[li[no].left].value = li[no].value;
		li[li[no].left].value2 = true;
		if (li[no].right == 0) {
			li_c += 1;
			li[no].right = li_c;
		}
		li[li[no].right].value = li[no].value;
		li[li[no].right].value2 = true;
	}
	llint dum = j * num + num / 2;
	if (l < dum and r <= dum) {
		if (li[no].left == 0) {
			li_c += 1;
			li[no].left = li_c;
		}
		sol2(l, r, j * 2, li[no].left, num / 2, numset);
	}
	else if (l >= dum and r > dum) {
		if (li[no].right == 0) {
			li_c += 1;
			li[no].right = li_c;
		}
		sol2(l, r, j * 2 + 1, li[no].right, num / 2, numset);
	}
	else {
		if (li[no].left == 0) {
			li_c += 1;
			li[no].left = li_c;
		}
		if (li[no].right == 0) {
			li_c += 1;
			li[no].right = li_c;
		}
		sol2(l, dum, j * 2, li[no].left, num / 2, numset);
		sol2(dum, r, j * 2 + 1, li[no].right, num / 2, numset);
	}

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;

	for (int i = 0; i < n; i++) {
		llint inp1, inp2,max_;
		cin >> inp1>> inp2;
		max_ = sol(inp2 - 1, inp2 - 1 + inp1, 0, 0, pow(2, 31));//최댓값구하기
		r = max(r, max_ + 1);
		//cout << max_ << '\n';
		sol2(inp2 - 1, inp2 - 1 + inp1, 0, 0, pow(2, 31), max_+1);//최댓값설정하기
		//cout << li_c << '\n';
	}
	cout << r;
}






