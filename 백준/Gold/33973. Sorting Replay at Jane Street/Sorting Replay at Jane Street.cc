//scsc-Sorting Replay at Jane Street

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

struct llint_list {
	llint li[2000];
};

int n, m;
llint li[2000];
llint li2[2000][2000];
llint fact[2001];
int sorteds[2000];
llint_pair sorteds_sort[2000];

int sortpivs[2000];

int compare_piv = 0;

bool compair(llint_pair a, llint_pair b) {
	return a.first > b.first;
}
bool compair2(llint a, llint b) {
	return li2[a][compare_piv] < li2[b][compare_piv];
}

int sol() {
	llint dum = 1;
	fact[0] = 1;
	for (int i = 1; i < 2001; i++) {
		dum *= i;
		dum %= 998244353;
		fact[i] = dum;
		//998244353
	}

	llint r = 0;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> li2[i][j];
		}
	}
	for (int i = 0; i < n; i++) {
		li[i] = i;
	}
	int inp[2];
	int ranran = 0;
	for (int asd = 1; asd < m + 1; asd++) {
		cin >> inp[0] >> inp[1];
		if (inp[0] == 1) {
			ranran = 1;
			for (int i = 0; i < 2000; i++) {
				sorteds[i] = 0;
			}
			sorteds[inp[1] - 1] = 1;
		}
		else {
			sorteds[inp[1] - 1] = asd;
		}
	}
	for (int i = 0; i < 2000; i++) {
		sorteds_sort[i].first = sorteds[i];
		sorteds_sort[i].second = i;
	}
	sort(sorteds_sort, sorteds_sort + 2000, compair);
	r = 1;
	int lastsort = -1;
	for (int i = 0; i < 2000; i++) {
		if (sorteds_sort[i].first == 0) {
			break;
		}
		else {
			int dumpiv = sorteds_sort[i].second;
			int idxhis = 0;
			compare_piv = dumpiv;
			for (int j = 0; j < n + 1; j++) {
				if (sortpivs[j] == 1 or j == n) {
					sort(li + idxhis, li + j, compair2);
					for (int k = idxhis + 1; k < j; k++) {
						if (li2[li[k - 1]][compare_piv] != li2[li[k]][compare_piv]) {
							sortpivs[k] = 1;
						}
					}
					idxhis = j;
				}
			}
		}
	}
	sortpivs[0] = 1;
	int zcount = 0;
	r = 1;
	//for (int i = 0; i < n; i++) {
	//	cout << sortpivs[i];
	//}
	//cout << "\n";
	if (ranran == 1) {
		for (int i = 0; i < n + 1; i++) {
			if (i == n or sortpivs[i] == 1) {
				r *= fact[zcount + 1];
				r %= 998244353;
				zcount = 0;
			}
			else if (sortpivs[i] == 0) {
				zcount += 1;
			}
		}
	}
	cout << r;
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
