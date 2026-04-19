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


int n, m,keycount,cases;
int bang[100][100][4][2];
int maps[100][100];
int keys[100][100][2];
int keys_pos[10][2];
int ways[10][10][4][2];
int dirs[4][2] = { {-1,0},{0,+1},{1,0},{0,-1} };
deque<llint_pair> q;


int dp[10][2048][4][2];

int sol2(int idx,int times,int vis) {
	if (idx == keycount-1 and vis == (1<<(keycount))-1) return 0;
	//if (counts == 10) return -1;
	if (dp[idx][vis][times][1] == cases) return dp[idx][vis][times][0];
	int r = -1;
	for (int i = 0; i < keycount; i++) {
		if (i != idx and (vis & (1 << i)) == 0) {
			int dum = sol2(i, (times + ways[idx][i][(times)%4][0]) % 4, vis | (1 << i));
			if (dum != -1) {
				dum += ways[idx][i][(times) % 4][0];
				if (r == -1 or r > dum) r = dum;
			}
		}
	}
	dp[idx][vis][times][0] = r;
	dp[idx][vis][times][1] = cases;
	return r;
}


int sol() {
	cin >> n >> m;
	cases += 1;
	if (n == 0 and m == 0) return 1;
	for (int i = 0; i < n; i++) {
		string inp;
		cin >> inp;
		for (int j = 0; j < m; j++) {
			if (inp[j] == 'N') maps[i][j] = 0;
			else if (inp[j] == 'E') maps[i][j] = 1;
			else if (inp[j] == 'S') maps[i][j] = 2;
			else if (inp[j] == 'W') maps[i][j] = 3;
		}
	}
	cin >> keycount;
	for (int i =1; i < keycount+1; i++) {
		cin >> keys_pos[i][0] >> keys_pos[i][1];
		keys_pos[i][0] -= 1;
		keys_pos[i][1] -= 1;
		keys[keys_pos[i][0]][keys_pos[i][1]][0] = i + 1;
		keys[keys_pos[i][0]][keys_pos[i][1]][1] = cases;
	}
	keys_pos[0][0] = 0;
	keys_pos[0][0] = 0;
	keys[0][0][0] = 1;
	keys[0][0][1] = cases;
	keys_pos[keycount+1][0] = n-1;
	keys_pos[keycount+1][1] = m-1;
	keys[n-1][m-1][0] = keycount + 2;
	keys[n - 1][m - 1][1] = cases;

	keycount += 2;

	for (int i = 0; i < keycount; i++) {
		for (int times = 0; times < 4; times++) {
			q.push_back({ keys_pos[i][0],keys_pos[i][1],times });
			while (!q.empty()) {
				int lenq = q.size();
				for (int j = 0; j < lenq; j++){
					llint_pair qpop = q.front();
					//cout << qpop.first << " " << qpop.second << " " << qpop.third <<"\n";
					q.pop_front();
					int dir = (maps[qpop.first][qpop.second] + qpop.third) % 4;

					for (int k = 0; k < 2; k++) {
						llint_pair newq = { qpop.first + dirs[dir][0]*k,qpop.second + dirs[dir][1]*k,qpop.third + 1 };
						if (newq.first > -1 and newq.first < n and newq.second > -1 and newq.second < m) {
							if (bang[newq.first][newq.second][newq.third%4][0] != i*4+ times +1 or bang[newq.first][newq.second][newq.third % 4][1] != cases) {
								bang[newq.first][newq.second][newq.third % 4][0] = i * 4 + times + 1;
								bang[newq.first][newq.second][newq.third % 4][1] = cases;
								q.push_back(newq);
								if (keys[newq.first][newq.second][1] == cases and keys[newq.first][newq.second][0] != i + 1) {
									if (ways[i][keys[newq.first][newq.second][0] - 1][times][1] != cases) {
										ways[i][keys[newq.first][newq.second][0] - 1][times][0] = newq.third - times;
										ways[i][keys[newq.first][newq.second][0] - 1][times][1] = cases;
									}
								}
							}
						}
					}
				}
			}
			//cout << "---\n";
		}
	}

	//for (int i = 0; i < keycount; i++) {
	//	for (int j = 0;j < keycount; j++) {
	//		cout <<i << "->" <<j <<":";
	//		for (int k = 0; k < 4; k++) {
	//			cout << ways[i][j][k] <<" ";
	//		}
	//		cout << "\n";
	//	}
	//}

	cout << sol2(0, 0, 1)<<"\n";


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






