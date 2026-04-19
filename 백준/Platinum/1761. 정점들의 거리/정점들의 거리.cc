#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

struct node {
	int first;
	int second;
};

int bumo[40000][2];//
int depth[40000];
int depth_dp[40000][2];
//map<int, int> bumo_dp[40000];
map<int, int> way[40000];
int n, m;
deque<int> q;
bool bang[40000];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	for (int i = 0; i < n - 1; i++) {
		int inp1, inp2, inp3;
		cin >> inp1 >> inp2 >> inp3;
		inp1 -= 1;
		inp2 -= 1;
		way[inp1][inp2] = inp3;
		way[inp2][inp1] = inp3;
	}
	q.push_back(0);
	bang[0] = true;
	int t = 1;
	while (!q.empty()) {
		int lenq = q.size();
		for (int i = 0; i < lenq; i++) {
			int qpop = q.front();
			q.pop_front();
			for (auto j = way[qpop].begin(); j != way[qpop].end(); j++) {
				int dum = (*j).first;
				if (!bang[dum]) {
					q.push_back(dum);
					bumo[dum][0] = qpop;
					bumo[dum][1] = (*j).second;
					depth[dum] = t;
					bang[dum] = true;
					//cout << (*j).first << "\n";
				}
			}
		}
		t += 1;
		
	}
	cin >> m;
	for (int i = 0; i < m; i++) {
		int p[2], r;
		r = 0;
		cin >> p[0] >> p[1];
		p[0] -= 1;
		p[1] -= 1;
		//int dump[2] = {p[0] ,p[1]};

		if (depth[p[0]] != depth[p[1]]) {
			int dum = 0;//갚은쪽
			if (depth[p[0]] < depth[p[1]]) {
				dum = 1;
			}
			int dum2 = depth[p[1 - dum]];

			int debug = 0;
			//if (depth[p[dum]] - dum2 > 10001) { cout << depth[400000000]; }
			deque<int> q2[2];
			while (dum2 < depth[p[dum]]) {
				if (dum2 <= depth[p[dum]] - 4 and depth_dp[p[dum]][1] != 0) {
					r += depth_dp[p[dum]][1];
					p[dum] = depth_dp[p[dum]][0];
					q2[0].clear();
					q2[1].clear();
				}
				else {
					q2[0].push_back(p[dum]);
					q2[1].push_back(r);
					r += bumo[p[dum]][1];
					p[dum] = bumo[p[dum]][0];
					debug += 1;
					if (q2[0].size() == 4) {
						depth_dp[q2[0].front()][0] = p[dum];
						depth_dp[q2[0].front()][1] = r-q2[1].front();
						q2[0].pop_front();
						q2[1].pop_front();
					}
				}
				//cout << depth[p[0]] << " " << depth[p[1]] << "\n";
			}
		}
		int debug = 0;
		while (p[0] != p[1]) {
			//cout << p[0] << " " << p[1] << "\n";
			r += bumo[p[0]][1];
			p[0] = bumo[p[0]][0];
			r += bumo[p[1]][1];
			p[1] = bumo[p[1]][0];
			debug += 1;
			//if (debug == 10002) { cout << depth[4000000000]; }
		}
		//bumo_dp[dump[0]][depth[p[0]]] = p[0];
		//bumo_dp[dump[1]][depth[p[1]]] = p[1];
		cout << r << "\n";

	}

	return 0;
}