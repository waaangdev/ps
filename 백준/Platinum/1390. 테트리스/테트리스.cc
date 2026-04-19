//테트리스

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));

struct edge {
	int top;
	int center;
	int bottom;
};

int n;
list<edge> blocks[6][6];

void createBlock(edge l, edge r, int updown) {
	if(updown == -1){
		blocks[l.top + 2][l.bottom + 2].push_back(r);
	}
	else if (updown == 0) {
		blocks[l.top + 2][5].push_back(r);
	}
	else if (updown == 1) {
		blocks[5][l.bottom+2].push_back(r);
	}
	
}

llint dp[301][5][5];
bool dp2[301][5][5];

llint sol(int n, edge eg) {
	//cout << n << " " << eg.top << " " << eg.center<< " " << eg.bottom << "\n";
	if (dp2[n][eg.top + 2][eg.bottom + 2]) {
		return dp[n][eg.top + 2][eg.bottom + 2];
	}
	llint r = 0;
	if (n < max(eg.top, eg.bottom) or n==0) {
		if (eg.top == 0 and eg.bottom == 0) {
			return 1;
		}
		return 0;
	}
	for (int i = 0; i < 3; i++) {
		int dum2[] = { eg.top + 2,eg.bottom + 2 };
		if (i == 1) {
			dum2[1] = 5;
		}
		if (i == 2) {
			dum2[0] = 5;
		}
		for (auto iter = blocks[dum2[0]][dum2[1]].begin(); iter != blocks[dum2[0]][dum2[1]].end(); iter++) {
			edge dum = { eg.top + (iter->top) - (iter->center),0,eg.bottom + (iter->bottom) - (iter->center) };
			if (abs(dum.top) <= 2 and abs(dum.bottom) <= 2) {
				r += sol(n - (*iter).center, dum);
				r = r % 1000000;
			}
		}
	}
	dp[n][eg.top + 2][eg.bottom + 2] = r;
	dp2[n][eg.top + 2][eg.bottom + 2] = true;
	return r;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;

	createBlock({ 0,0,1 }, { 1,2,1 }, -1);
	createBlock({ 1,0,0 }, { 1,2,1 }, -1);
	createBlock({ 0,0,0 }, { 1,2,1 }, -1);
	createBlock({ 1,0,1 }, { 1,2,1 }, -1);
	createBlock({ 0,0,0 }, { 1,1,2 }, -1);
	createBlock({ 0,0,0 }, { 2,1,1 }, -1);
	createBlock({ 0,0,-1 }, { 1,1,2 }, -1);
	createBlock({ -1,0,0 }, { 2,1,1 }, -1);


	createBlock({ 0,0,0 }, { 2,2,0 }, 0);
	createBlock({ 0,0,0 }, { 0,2,2 }, 1);

	createBlock({ 1,0,0 }, { 2,2,0 }, 0);
	createBlock({ 0,0,-1 }, { 0,2,2 }, 1);

	createBlock({ -1,0,0 }, { 2,2,0 }, 0);
	createBlock({ 0,0,1 }, { 0,2,2 }, 1);


	createBlock({ 1,0,0 }, { 1,3,0 }, 0);
	createBlock({ 0,0,-1 }, { 0,1,3 }, 1);
	createBlock({ -1,0,0 }, { 3,1,0 }, 0);
	createBlock({ 0,0,1 }, { 0,3,1 }, 1);

	createBlock({ 2,0,0 }, { 1,3,0 }, 0);
	createBlock({ 0,0,-2 }, { 0,1,3 }, 1);
	createBlock({ 0,0,0 }, { 3,1,0 }, 0);
	createBlock({ 0,0,0 }, { 0,3,1 }, 1);

	createBlock({ -2,0,0 }, { 3,1,0 }, 0);
	createBlock({ 0,0,2 }, { 0, 3,1 }, 1);
	createBlock({ 0,0,0 }, { 1,3,0 }, 0);
	createBlock({ 0,0,0 }, { 0, 1,3 }, 1);


	cout << sol(n, {});


}






