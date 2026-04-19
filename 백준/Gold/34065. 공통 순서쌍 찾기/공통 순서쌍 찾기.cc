

//c
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
	llint third;
};

struct cmp {
	bool operator()(llint_pair a, llint_pair b) {
		return a.first > b.first;
	}
};

int n, k ,r,k2;
int ab_idxs[200000];
int li[2][200000];
int lis[200000][2];
vector<llint_pair> liss[200000];
priority_queue<llint_pair, vector<llint_pair>, cmp> pq;
//int r[2][200000];

void dfs(int host,int idx) {
	for (int i = 0; i < liss[idx].size(); i++) {
		if (k2 == k)break;
		//dfs(host, liss[idx][i].third);
		cout << liss[idx][i].second << " "<< host << "\n";
		k2 += 1;
	}
}


int sol() {
	cin >> n >> k;
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < n; j++) {
			cin >> li[i][j];
		}
	}
	for (int j = 0; j < n; j++) {
		ab_idxs[li[1][j] - 1] = j;
	}
	for (int j = 0; j < n; j++) {
		lis[j][0] = ab_idxs[li[0][j] - 1];
		lis[j][1] = li[0][j];
	}
	for (int j = 0; j < n; j++) {
		while (!pq.empty()) {
			llint_pair top = pq.top();
			if (top.first < lis[j][0]) {
				liss[j].push_back(top);
				r += 1;//liss[top.third].size() + 1;
				pq.pop();
				if (r >= k) {
					break;
				}
			}
			else {
				break;
			}
		}
		for (int i = 0; i < liss[j].size(); i++) {
			pq.push(liss[j][i]);
		}
		if (r >= k) {
			break;
		}

		pq.push({ lis[j][0],lis[j][1], j});
	}
	
	//for (int j = 0; j < n; j++) {
	//	cout << lis[j][0] << " ";
	//}

	//cout << "r = " << r << '\n';

	//for (int j = 0; j < n; j++) {
	//	cout << "-";
	//	for (int k = 0; k < liss[j].size(); k++) {
	//		cout << liss[j][k].second << " ";
	//	}
	//	cout << "\n";
	//}

	if (r >= k) {
		cout << "Yes\n";

		for (int j = 0; j < n; j++) {
			dfs(li[0][j], j);
		}

	}
	else {
		cout << "No\n";
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
