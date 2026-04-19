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

llint n, m;
string mapinput[50];
bool maps[52][52];
int bang[52][52];
int bang2[52][52];//섬 넘버링
int bang3[52][52];
int bang4[52][52];
int dirs[8][2] = { {0,1},{-1,0},{1,0},{0,-1},{-1,1} ,{1,1} ,{-1,-1} ,{1,-1} };
int rli[100];

vector<int> ways[2500];
bool ways_inable[2500][2500];
bool stisland[2500];


deque<llint_pair> q;


void bfs(bool mode,int mode2,int ridx,int bfsmode) {
	while (!q.empty()) {
		int lenq = q.size();
		for (int i = 0; i < lenq; i++) {
			llint_pair qpop = q.front();
			q.pop_front();
			bool island = maps[qpop.first][qpop.second];
			for (int j = 0; j < 8-(island ?0:4); j++) {
				int x = qpop.first + dirs[j][0], y = qpop.second + dirs[j][1];

				if (x > -1 and x < n + 2 and y > -1 and y < m + 2) {
					if (bfsmode == 0) {
						if (bang[x][y] == 0) {
							if (maps[x][y] == mode) {
								q.push_back({ x,y });
								bang[x][y] = mode2;
								//if (mode == true) {
								//	rli[ridx] += 1;
								//}
							}
							else {
								bang[x][y] = mode2 + 1;
							}
						}
					}
					else if(bfsmode == 1) {
						if (bang2[x][y] == 0 and bang[x][y]==mode2) {
							q.push_back({ x,y });
							bang2[x][y] = 1;
						}
					}
					else if (bfsmode == 2) {
						if (bang3[x][y] == 0) {
							//if (maps[x][y] == mode) {
							if (bang[qpop.first][qpop.second] != bang[x][y]) {
								if (bang[x][y] != 1) {
									bang3[x][y] = bang3[qpop.first][qpop.second] + 1;
									bang4[x][y] = 1;
								}
							}
							else {
								q.push_back({ x,y });
								bang3[x][y] = bang3[qpop.first][qpop.second];
							}
							//}
							//else {
							//	bang4[x][y] = 1;
							//}
						}
						//if (mode == false) {//바다
						//	if (bang3[x][y] == 0) {
						//		q.push_back({ x,y });
						//		bang3[x][y] = mode2;
						//	}
						//}
						//else {//섬
						//	if (bang3[x][y] == 0) {
						//		q.push_back({ x,y });
						//		bang3[x][y] = mode2;
						//	}
						//}
					}
					else if (bfsmode == 4) {
						if (bang2[x][y] == 0 and bang3[x][y] == mode2) {
							q.push_back({ x,y });
							bang2[x][y] = 1;
						}
					}
					else if (bfsmode == 5) {
						if (maps[x][y]) {
							if (bang2[x][y] == 0) {
								q.push_back({ x,y });
								bang2[x][y] = mode2;
							}
						}
					}
					else if (bfsmode == 6) {
						if (bang[x][y] == 0) {
							if (maps[x][y] == mode) {
								q.push_back({ x,y ,qpop.third});
								bang[x][y] = mode2;
								//if (mode == true) {
								//	rli[ridx] += 1;
								//}
							}
							else {
								bang[x][y] = mode2 + 1;
								if (bang[x][y] == 2) {
									stisland[bang2[x][y]] = true;
								}
								if (qpop.third != 0 and bang2[x][y] != 0) {
									if (!ways_inable[qpop.third][bang2[x][y]]) {
										ways_inable[qpop.third][bang2[x][y]] = true;
										ways[qpop.third].push_back(bang2[x][y]);
									}
								}

								if (bang2[x][y] == 0) {
									bang2[x][y] = qpop.third;
									//cout << "a\n";
								}
							}
						}
					}
				}
			}
		}
	}

}


void newq(int mode) {
	for (int i = 0; i < n + 2; i++) {
		for (int j = 0; j < m + 2; j++) {
			if (bang[i][j] == mode) {
				q.push_back({ i,j ,bang2[i][j]});
			}
			//cout << bang[i][j];
		}
		//cout << "\n";
	}
}
void newqpr() {
	for (int i = 0; i < n + 2; i++) {
		for (int j = 0; j < m + 2; j++) {
			cout << bang[i][j];
		}
		cout << "\n";
	}
}
void newqpr2() {
	for (int i = 0; i < n + 2; i++) {
		for (int j = 0; j < m + 2; j++) {
			cout << bang2[i][j];
		}
		cout << "\n";
	}
}

void newq4(int mode) {
	for (int i = 0; i < n + 2; i++) {
		for (int j = 0; j < m + 2; j++) {
			if (bang[i][j] == mode and bang3[i][j] == 0) {
				q.push_back({ i,j });
				bang3[i][j] = 2;
			}
			//cout << bang[i][j];
		}
		//cout << "\n";
	}
}
void newq3(int mode) {
	for (int i = 0; i < n + 2; i++) {
		for (int j = 0; j < m + 2; j++) {
			if (bang4[i][j] == 1) {
				q.push_back({ i,j });
				bang4[i][j] = 0;
			}
			//cout << bang[i][j];
		}
		//cout << "\n";
	}
}
void newq2(int mode) {
	for (int i = 0; i < n + 2; i++) {
		for (int j = 0; j < m + 2; j++) {
			if (bang3[i][j] == mode and bang[i][j] != 2) {
				q.push_back({ i,j });
			}
			cout << bang3[i][j];
		}
		cout << "\n";
	}
}

int sol2(int idx) {
	int r = -1;
	for (int i = 0; i < ways[idx].size(); i++) {
		r = max(r, sol2(ways[idx][i]));
	}
	rli[r + 1] += 1;
	return r + 1;
}


int sol() {
	cin >> n >>m;
	
	for (int i = 0; i < n; i++) {
		cin >> mapinput[i];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (mapinput[i][j] == 'x') {
				maps[i+1][j+1] = true;
			}
		}
	}


	int modeidx = 1;
	for (int i = 1; i < n + 1; i++) {
		for (int j = 1; j < m + 1; j++) {
			if (maps[i][j]) {
				if (bang2[i][j] == 0) {
					q.push_back({ i,j });
					bang2[i][j] = modeidx;
					bfs(false, modeidx, 0, 5);
					modeidx++;
				}
			}
		}
	}
	//newqpr2();

	int nodesu = modeidx - 1;

	for (int i = 0; i < n + 2; i++) {
		for (int j = 0; j < m + 2; j++) {
			if (i == 0 or i == n + 1 or j == 0 or j == m + 1) {
				q.push_back({ i,j ,0});

			}
		}
	}

	bool mode = false;
	modeidx = 1;
	while (!q.empty()) {
		bfs(mode, modeidx, 0,6);
		modeidx += 1;
		mode = !mode;

		newq(modeidx);
	}
	//newqpr();
	//newqpr2();

	//for (int i = 0; i < nodesu; i++) {
	//	cout << i + 1 << "-";
	//	for (int j = 0; j < ways[i+1].size();j++) {
	//		cout << ways[i + 1][j] << " ";
	//	}
	//	cout << "\n";
	//}



	for (int i = 0; i < 2500; i++) {
		if (stisland[i]) {
			sol2(i);
		}
	}



	if (rli[0] == 0) {
		cout << -1;
	}
	else {
		int ridx = 0;
		while (rli[ridx] != 0) {
			cout << rli[ridx] << " ";
			ridx++;
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






