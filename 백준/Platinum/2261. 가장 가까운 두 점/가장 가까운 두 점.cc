//가장 가까운 두 점

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
struct node2 {
	int first;
	int second;
	int third;
};

#define swap(a,b,t) ((t=a),(a=b),(b=t));

llint n,r;

node inpli[100001];
int li[100001];
node2 li2[20001];//본인의 x좌표, 내 스타팅 index,x좌표에있는애들갯수
int li2_c;

int sol(int l, int r, int a) {
	int dum = (l + r) / 2;
	if (l + 1 == r) {
		return l;
	}
	if (li2[dum].first > a) {
		return sol(l, dum, a);
	}
	else {
		return sol(dum, r, a);
	}
}
int sol2(int l, int r, int a) {
	int dum = (l + r) / 2;
	if (l + 1 == r) {
		return l;
	}
	if (li[dum] > a) {
		return sol2(l, dum, a);
	}
	else {
		return sol2(dum, r, a);
	}
}

bool compair(node a, node b) {
	if (a.first == b.first) {
		return a.second < b.second;
	}
	return a.first < b.first;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int tmp;

	cin >> n;
	for (int i = 0; i < n; i++) {
		int inp1, inp2;
		cin >> inp1 >> inp2;
		inp1 += 10000;
		inp2 += 10000;
		inpli[i].first = inp1;
		inpli[i].second = inp2;
	}
	sort(inpli, inpli + n, compair);
	int dum = -1;
	for (int i = 0; i < n; i++) {
		//cout << inpli[i].first << "\n";
		if (dum != inpli[i].first) {
			li2[li2_c].first = inpli[i].first;
			li2[li2_c].second = i;
			li2_c += 1;
			dum = inpli[i].first;
		}
		li2[li2_c - 1].third += 1;
		li[i] = inpli[i].second;
	}
	//cout << "li2_c : " << li2_c << "\n";


	r = -1;
	for (int i = 0; i < n; i++) {
		int sqrtr = 0;
		if (r == -1) {
			sqrtr = 20001;
		}
		else {
			sqrtr = sqrt(r);
		}
		int minx = sol(0, li2_c, inpli[i].first - sqrtr);
		int maxx = sol(0, li2_c, inpli[i].first + sqrtr);
		bool samep = true;
		for (int j= minx; j<= maxx; j++) {
			int miny = sol2(li2[j].second, li2[j].second+ li2[j].third, inpli[i].second - sqrtr);
			int maxy = sol2(li2[j].second, li2[j].second + li2[j].third, inpli[i].second + sqrtr);
			for (int k = miny; k <= maxy; k++) {
				int dist = pow(li2[j].first - inpli[i].first, 2) + pow(li[k] - inpli[i].second, 2);
				if (dist == 0 and samep) {
					samep = false;
				}
				else {
					if (dist < r or r == -1) {
						r = dist;
					}
				}
			}
		}
	}

	//int testr = r;
	//for (int i = 0; i < n; i++) {
	//	for (int j = i+1; j < n; j++) {
	//		if (i != j) {
	//			testr = min(testr, (int)pow(inpli[j].first - inpli[i].first, 2) + (int)pow(inpli[i].second - inpli[j].second, 2));
	//		}
	//	}
	//}
	//cout << testr << "\n";
	cout << r;
}






