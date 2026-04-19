//공장

#define _USE_MATH_DEFINES

#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

struct node {
	int first;
	int second;
};


int li[1000001];
int li2[500001];
llint tree[20][500001];
llint n,r;

int treeget(int a,int i) {
	if (i == 20) {
		return 0;
	}
	return tree[i][a] + treeget(a / 2, i + 1);
}

void treeadd(int i, int j, int l, int r,int p) {
	//cout << i << " " << j << " " << l << " " << r << " " << p << "\n";
	if (j * p == l and r == l + p) {
		tree[i][j] += 1;
	}
	else if (j * p+p/2 > l and j * p + p / 2 >= r) {
		treeadd(i - 1, j * 2, l, r, p / 2);
	}
	else if (j * p + p / 2 <= l and j * p + p / 2 < r) {
		treeadd(i - 1, j * 2+1, l, r, p / 2);
	}
	else {
		treeadd(i - 1, j * 2, l, j * p + p / 2, p / 2);
		treeadd(i - 1, j * 2 + 1, j * p + p / 2, r, p / 2);
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
		li[inp] = i;
	}
	for (int i = 0; i < n; i++) {
		int inp;
		cin >> inp;
		//li2[i] = inp;
		//int dum  = li[inp] - treeget(li[inp], 0);
		//cout << dum << "\n";
		r += li[inp] - treeget(li[inp],0);
		//for (int k = 0;k < 5; k++) {
		//	for (int j = 0; j < n; j++) {
		//		cout << tree[k][j] << " ";
		//	}
		//	cout << "\n";
		//}


		//int dum = li[inp] - treeget(li[inp], 0);
		//int dum2 = treeget(li[i], 0);
		//if (dum >0  or dum2>0) {
		//	r += 1;
		//}
		treeadd(19, 0, li[inp], n,pow(2,19));

	}
	cout << r << "\n";


	//r = 0;
	//for (int i = 0; i < n; i++) {
	//	int dum = 0;
	//	for (int j = i+1; j < n; j++) {
	//		if (li[li2[i]] > li[li2[j]]) {
	//			dum+= 1;
	//		}
	//	}
	//	cout << dum << " ";
	//	r += dum;
	//}
	//cout << r << "\n";

}






