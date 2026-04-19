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

struct cmp {
	bool operator()(array<int, 2> a, array<int, 2> b);
};
bool cmp::operator()(array<int, 2> a, array<int, 2> b) {
	return a[1] > b[1];
}

vector<array<int,2>> way[10000];
int bang[10000];
priority_queue<array<int,2>, vector<array<int, 2>>,cmp> q;



int sol() {
	int n, d, c,inp[3];
	cin >> n >> d >> c;
	for (int i = 0; i < d; i++) {
		cin >> inp[0] >> inp[1] >> inp[2];
		way[inp[1]-1].push_back({ inp[0]-1,inp[2] });
	}
	for (int i = 0; i < n; i++) {
		bang[i] = -1;
	}
	q.push({ c - 1 ,0});
	bang[c - 1] = 0;

	while (!q.empty()) {
		int idx = q.top()[0];
		//cout << q.top()[0] << " "<< q.top()[1] << "\n";
		q.pop();
		for (auto i = way[idx].begin(); i != way[idx].end(); i++) {
			if (bang[(*i)[0]] == -1 or bang[(*i)[0]] > bang[idx]+(*i)[1]) {
				bang[(*i)[0]] = bang[idx] + (*i)[1];
				q.push({ (*i)[0] ,bang[(*i)[0]] });
			}
		}
	}
	int r[2] = {0,0};
	for (int i = 0; i < n; i++) {
		while (!way[i].empty())way[i].pop_back();
		//cout << bang[i] << " ";
		r[0] = max(r[0], bang[i]);
		if (bang[i] != -1) {
			r[1] += 1;
		}
	}
	//cout << "\n";
	cout << r[1] <<" " << r[0]<<"\n";

	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> case_;
	 
	for (int i = 0; i < case_; i++) {
		sol();
	}

	//while (!sol()) {

	//}


}






