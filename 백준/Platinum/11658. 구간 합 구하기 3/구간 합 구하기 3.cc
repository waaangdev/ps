//디피그리디

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));

int case_ = 1;


struct llint_pair {
	llint first;
	llint second;
};

llint tree[2048][2048];
bool treedp[2048][2048];
llint treeidx[11];
int a, b;


llint segi(int idx,int li, int ri, int lj, int rj, int dep,int mode) {
	//cout <<'-' << idx << ' ' << li << ' ' << ri << ' ' << dep << '\n';
	if (li == ri) {
		return 0;
	}
	if (li == idx * (1 << (10 - dep)) and ri== li+ (1 << (10 - dep))) {
		//cout << "a";
		if (mode == 0) {
			return segi(0, lj, rj, dep, idx, 0, 1);
		}
		else {
			return tree[treeidx[lj] + rj][treeidx[dep] + idx];
		}
	}
	int dum = idx * (1 << (10 - dep)) + (1 << (9 - dep));
	llint r = 0;
	r += segi(idx * 2, min(li, dum), min(ri, dum), lj, rj, dep + 1, mode);
	r += segi(idx * 2+1, max(li, dum), max(ri, dum), lj, rj, dep + 1, mode);
	return r;
}


void treeSet2(int ii,int jj ,int i, int j, int depi, int depj,int num) {
	cout << ii << " " << jj << '\n';
	tree[treeidx[depi] + ii][treeidx[depj] + jj] += num;
	if (depi != 10) {
		if (i>= ii*pow(2,10- depi)+ pow(2, 9 - depi)) {
			treeSet2(ii*2 + 1, jj, i, j, depi + 1, depj, num);
		}
		else {
			treeSet2(ii * 2, jj, i, j, depi + 1, depj, num);
		}
	}
	if (depj != 10) {
		if (j >= jj * pow(2, 10 - depj) + pow(2, 9 - depj)) {
			treeSet2(ii, jj * 2 + 1, i, j, depi, depj + 1, num);
		}
		else {
			treeSet2(ii, jj * 2, i, j, depi, depj + 1, num);
		}
	}
}

llint treeSet(int i, int j, int depi, int depj) {
	//cout << i << " " << j << '\n';
	llint r = 0;
	if (depi == 10 and depj == 10) {
		return tree[treeidx[10] + i][treeidx[10] + j];
	}
	if (treedp[treeidx[depi] + i][treeidx[depj] + j]) {
		return tree[treeidx[depi] + i][treeidx[depj] + j];
	}
	if (depi != 10) {
		r = 0;
		r += treeSet(i * 2, j, depi + 1, depj);
		r += treeSet(i * 2+1, j, depi + 1, depj);
		tree[treeidx[depi] + i][treeidx[depj] + j] = r;
	}							   
	if (depj != 10) {
		r = 0;
		r += treeSet(i, j * 2, depi, depj + 1);
		r += treeSet(i, j * 2+1, depi, depj + 1);
		tree[treeidx[depi] + i][treeidx[depj] + j] = r;
	}
	treedp[treeidx[depi] + i][treeidx[depj] + j] = true;
	return r;
}


int sol() {
	int dum = 0;
	for (int i = 0; i < 11; i++) {
		treeidx[i] = dum;
		dum += pow(2, i);
	}

	cin >> a >> b;
	for (int i = 0; i < a; i++) {
		for (int j = 0; j < a; j++) {
			int dum = 0;
			cin >> tree[treeidx[10]+i][treeidx[10] + j];//tree[0][i][j];
		}
	}
	treeSet(0,0,0,0);
	//cout << tree[0][0] <<"asd\n";

	for (int i1 = 0; i1 < b; i1++) {
		int m;
		cin >> m;
		if (m == 0) {
			int i,j,num;
			cin >> i >> j >> num;
			i -= 1;
			j -= 1;
			num = num- tree[treeidx[10] + i][treeidx[10] + j];
			//cout << num<<"\n";
			int i2 = i;
			for (int ii = 10; ii > -1; ii--) {
				int j2 = j;
				for (int jj = 10; jj > -1; jj--) {
					tree[treeidx[ii] + i2][treeidx[jj] + j2]+=num;
					j2 /= 2;
				}
				i2 /= 2;
			}
			
			//treeSet2(0, 0, i, j, 0, 0, num);

		}
		else {
			int lx,ly, rx, ry;
			cin >> lx >> ly >> rx>> ry;
			lx -= 1;
			ly -= 1;
			cout << segi(0,lx, rx, ly, ry, 0, 0)<<'\n';
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
		sol();
	}

	//while (!sol()) {

	//}


}






