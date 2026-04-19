//아날로그 다이얼
//이거 안되면 걍 값구하는거하고 느리갱신하고 따로 구현해라
//욕심부리지말고
//값도 미리 구해너ㅘ라 존내짜증나니까
//값 미리구해놓는게 더 효율적인거알지? 차라리 노드두개 합치는함수를 따로만들든가

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));

struct node {
	int count[10];
	int pointer_add;
	int pointer;
	bool gangsin;
};

int n, m;
node tree[1048576];
string inpli;
int ili[19];

node nodesum(node l, node r,int rr_pointer) {
	node rr = {};
	rr.pointer = rr_pointer;
	for (int i = 0; i < 10; i++) {
		rr.count[i]= l.count[(i+l.pointer)%10] + r.count[(i + r.pointer) % 10];
	}
	return rr;
}

node sol(int l, int r, int i, int j, int num) {
	//cout << i << " " << j<<  " " << l << " " << r << " " << ili[(i)]+j <<"\n";
	if (tree[ili[i] + j].gangsin or 1) {

		//tree[ili[i] + j].pointer += tree[ili[i] + j].pointer_add;
		//tree[ili[i] + j].pointer = tree[ili[i] + j].pointer % 10;
		//tree[ili[i] + j].pointer_add = 0;
		//tree[ili[i] + j].gangsin = false;
		if (not (l == j * num and r == l + num)) {
			if (i != 0) {
				tree[ili[(i - 1)] + (j * 2)].pointer += tree[ili[i] + j].pointer;
				tree[ili[(i - 1)] + (j * 2 + 1)].pointer += tree[ili[i] + j].pointer;

				tree[ili[i] + j].pointer = 0;

			}
		}

		//tree[ili[i] + j].pointer += tree[ili[i] + j].pointer_add;
		//tree[ili[i] + j].pointer = tree[ili[i] + j].pointer % 10;
		//tree[ili[i] + j].pointer_add = 0;
		//tree[ili[i] + j].gangsin = false;
		//if (not (l == j * num and r == l + num)) {
		//	if (i != 0) {
		//		tree[ili[(i - 1)] + (j * 2)].pointer_add += 9;
		//		tree[ili[(i - 1)] + (j * 2 + 1)].pointer_add += 9;
		//	}
		//	//tree[ili[i] + j].pointer = 0;

		//}

		//int dum2 = 0;
		//if (l == j * num and r == l + num) {
		//	if (tree[ili[i] + j].on) {
		//		dum2 = 1;
		//		
		//	}
		//}
		//if (dum2 == 0) {
		//	if (tree[ili[i] + j].gangsin) {
		//		tree[ili[i] + j].pointer += tree[ili[i] + j].pointer_add;
		//		tree[ili[i] + j].pointer = tree[ili[i] + j].pointer % 10;
		//		tree[ili[i] + j].gangsin = false;
		//		tree[ili[i] + j].pointer_add = 0;
		//	}
		//	if (i != 0) {
		//		tree[ili[(i - 1)] + (j * 2)].pointer += tree[ili[i] + j].pointer;
		//		tree[ili[(i - 1)] + (j * 2 + 1)].pointer += tree[ili[i] + j].pointer;
		//	}
		//	tree[ili[i] + j].pointer = 0;
		//}
		

		//tree[ili[i] + j].pointer += tree[ili[i] + j].pointer_add;
		//tree[ili[i] + j].pointer = tree[ili[i] + j].pointer%10;
		//tree[ili[i] + j].pointer_add = 0;
		//tree[ili[i] + j].gangsin = false;
	}

	int dum = j * num + num / 2;
	if (l == j*num and r == l+num) {
		//cout << "end! \n";
		//if (tree[ili[i]+j].on) {
		//	if (tree[ili[i] + j].gangsin) {
		//		tree[ili[i] + j].pointer += tree[ili[i] + j].pointer_add;
		//		tree[ili[i] + j].pointer = tree[ili[i] + j].pointer % 10;
		//		tree[ili[i] + j].gangsin = false;
		//		tree[ili[i] + j].pointer_add = 0;
		//	}

		//	tree[ili[i] + j].gangsin = true;
		//	tree[ili[i] + j].pointer_add += 9;
		//	cout << "on! \n";
		//	return tree[ili[i] + j];
		//}
		//tree[ili[i] + j].gangsin = true;
		//tree[ili[i] + j].pointer_add += 9;
		return tree[ili[i] + j];

	}
	else if (l < dum and r<= dum) {
		return sol(l, r, i - 1, j * 2, num / 2);
	}
	else if (l >= dum and r > dum) {
		return sol(l, r, i - 1, j * 2+1, num / 2);
	}
	else {

		return nodesum(sol(l, dum, i - 1, j * 2, num / 2), sol(dum, r, i - 1, j * 2 + 1, num / 2), tree[ili[i] + j].pointer);
	}
}
void sol2(int l, int r, int i, int j, int num) {
	//cout << num << " " << j << " " << l << " " << r << "\n";
	//if (tree[ili[i] + j].gangsin) {
	//	tree[ili[i] + j].pointer += tree[ili[i] + j].pointer_add;
	//	tree[ili[i] + j].pointer = tree[ili[i] + j].pointer % 10;
	//	if (i != 0) {
	//		tree[ili[(i - 1)] + (j * 2)].pointer_add += tree[ili[i] + j].pointer;
	//		tree[ili[(i - 1)] + (j * 2 + 1)].pointer_add += tree[ili[i] + j].pointer;

	//		tree[ili[i] + j].pointer = 0;
	//	}
	//}
	int dum = j * num + num / 2;
	if (l == j * num and r == l + num) {
		tree[ili[i] + j].pointer += 9;
		tree[ili[i] + j].gangsin = true;
	}
	else if (l < dum and r <= dum) {
		sol2(l, r, i - 1, j * 2, num / 2);
		tree[ili[i] + j] = nodesum(tree[ili[i - 1] + j * 2 + 1], tree[ili[i - 1] + j * 2], tree[ili[i] + j].pointer);
	}
	else if (l >= dum and r > dum) {
		sol2(l, r, i - 1, j * 2 + 1, num / 2);
		tree[ili[i] + j] = nodesum(tree[ili[i - 1] + j * 2 + 1], tree[ili[i - 1] + j * 2], tree[ili[i] + j].pointer);
	}
	else {
		sol2(l, dum, i - 1, j * 2, num / 2);
		sol2(dum, r, i - 1, j * 2 + 1, num / 2);
		tree[ili[i] + j] = nodesum(tree[ili[i - 1] + j * 2 + 1], tree[ili[i - 1] + j * 2], tree[ili[i] + j].pointer);
	}

}
//void sol3(int l, int r, int i, int j, int num) {
//	if (tree[ili[i] + j].gangsin) {
//		tree[ili[i] + j].pointer += tree[ili[i] + j].pointer_add;
//		tree[ili[i] + j].pointer = tree[ili[i] + j].pointer % 10;
//		//if (i != 0) {
//		//	tree[ili[(i - 1)] + (j * 2)].pointer_add += tree[ili[i] + j].pointer;
//		//	tree[ili[(i - 1)] + (j * 2 + 1)].pointer_add += tree[ili[i] + j].pointer;
//
//		//	tree[ili[i] + j].pointer = 0;
//		//}
//	}
//
//	int dum = j * num + num / 2;
//	if (l == j * num and r == l + num) {
//		//tree[ili[i] + j].pointer_add += 9;
//		//tree[ili[i] + j].gangsin = true;
//	}
//	else if (l < dum and r <= dum) {
//		sol3(l, r, i - 1, j * 2, num / 2);
//		tree[ili[i] + j] = nodesum(tree[ili[i - 1] + j * 2 + 1], tree[ili[i - 1] + j * 2], tree[ili[i] + j].pointer);
//	}
//	else if (l >= dum and r > dum) {
//		sol3(l, r, i - 1, j * 2 + 1, num / 2);
//		tree[ili[i] + j] = nodesum(tree[ili[i - 1] + j * 2 + 1], tree[ili[i - 1] + j * 2], tree[ili[i] + j].pointer);
//	}
//	else {
//		sol3(l, dum, i - 1, j * 2, num / 2);
//		sol3(dum, r, i - 1, j * 2 + 1, num / 2);
//		tree[ili[i] + j] = nodesum(tree[ili[i - 1] + j * 2 + 1], tree[ili[i - 1] + j * 2], tree[ili[i] + j].pointer);
//	}
//
//}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> m;
	//n = 250000;
	cin >> inpli;

	for (int i = 0; i < n; i++) {
		int dum = inpli[i] - '0';
		tree[i].count[dum] = 1;
	}
	int dum5 = pow(2, 18);
	int dum2 = pow(2, 18);
	for (int i = 1; i < 19; i++) {
		ili[i] = dum5;
		//cout << dum5 << "\n";
		dum2 = dum2 / 2 + dum2 % 2;
		dum5 += dum2;
	}
	int dumn = n;
	for (int i = 1; i < 19; i++) {
		dumn = dumn / 2 + dumn % 2;
		for (int j = 0; j < dumn; j++) {
			tree[ili[i] + j] = nodesum(tree[ili[i - 1] + j * 2], tree[ili[i - 1] + j * 2 + 1],0);
		}
	}


	int inp1, inp2;
	for (int i = 0; i < m; i++) {
		cin >> inp1 >> inp2;
		node r = sol(inp1 - 1, inp2, 18, 0, pow(2, 18));
		sol2(inp1 - 1, inp2, 18, 0, pow(2, 18));
		//sol3(inp1 - 1, inp2, 18, 0, pow(2, 18));
		int sum = 0;
		for (int i = 0; i < 10; i++) {
			//cout << r.count[(r.pointer + i) % 10] << " ";
			sum += r.count[(r.pointer + i) % 10]*i;
		}
		//cout << "\n";
		cout <<sum <<"\n";

		//int dumn = n;
		//for (int i = 0; i < 10; i++) {
		//	for (int j = 0; j < dumn; j++) {
		//		cout << tree[ili[i] + j].pointer << " ";
		//	}
		//	cout << "\n";
		//	dumn = dumn / 2 + dumn % 2;
		//}
	}   
}






