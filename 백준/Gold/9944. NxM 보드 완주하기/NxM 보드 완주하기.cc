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

int map_[30][30],emptysu, emptysu2;
int n, m, r;

int sol2(int y,int x) {
	if (emptysu == 1) {
		return 0;
	}
	int r = 30 * 30 + 1;
	int bang[4][2] = { {0,1},{0,-1},{1,0},{-1,0} };
	for (int i = 0; i < 4; i++) {
		int dumy = y + bang[i][0];
		int dumx = x + bang[i][1];
		if (dumy > -1 and dumy < n and dumx > -1 and dumx < m) {
			if (map_[dumy][dumx] == 0) {
				int dum = 0;
				while (map_[dumy][dumx] == 0) {
					if (!(dumy > -1 and dumy < n and dumx > -1 and dumx < m)){
						break;
					}
					map_[dumy - bang[i][0]][dumx - bang[i][1]] = 1;
					dum += 1;
					emptysu -= 1;
					dumy += bang[i][0];
					dumx += bang[i][1];
				}
				dumy -= bang[i][0];
				dumx -= bang[i][1];
				int dumr = sol2(dumy, dumx);
				if (dumr != -1) {
					r = min(r, dumr+1);
				}
				dumy -= bang[i][0];
				dumx -= bang[i][1];
				for (int j = 0; j < dum; j++) {
					map_[dumy][dumx] = 0;
					emptysu += 1;
					dumy -= bang[i][0];
					dumx -= bang[i][1];
				}
			}
		}
	}

	if (r == 30 * 30 + 1) {
		r = -1;
	}
	return r;
}

int sol() {
	r = 30*30+1;
	if (!(cin >> n >> m)) {
		return 1;
	}
	emptysu2 = 0;
	for (int i = 0; i < n; i++) {
		string inp;
		cin >> inp;
		for (int j = 0; j < m; j++) {
			if (inp[j] == '*') {
				map_[i][j] = 1;
			}
			else {
				map_[i][j] = 0;
				emptysu2 += 1;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (map_[i][j] == 0) {
				emptysu = emptysu2;
				int dum = sol2(i, j);
				if(dum != -1)r = min(r,dum);
			}
		}
	}
	if (r == 30 * 30 + 1) {
		r = -1;
	}
	cout << "Case " << case_ << ": " << r<<"\n";
	case_ += 1;


	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//cin >> case_;

	//for (int i = 0; i < case_; i++) {
	//	sol();
	//}

	while (!sol()) {

	}


}






