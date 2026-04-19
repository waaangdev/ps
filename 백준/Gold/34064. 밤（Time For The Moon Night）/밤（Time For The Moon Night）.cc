//b
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
	bool operator()(llint_pair a, llint_pair b) {
		return a.first > b.first;
	}
};

int n, k ,m;
llint r = 0;
int maps[500][500];
int groops[2][500][500];
llint groops_size[2][5000];
int groops_pos[2][5000][2];
int rans[2][2][2];
int bang[500][500];
int bang_num = 1;
int gnum[2];

int comb[5000][5000];

int gbang[5000];


int ang[4][2] = { {0,1},{-1,0},{1,0},{0,-1} };

int sol() {
	cin >> n >> m >> k;
	for (int i = 0; i < k; i++) {
		int inp[2];
		cin >> inp[0] >> inp[1];
		inp[0] -= 1;
		inp[1] -= 1;
		maps[inp[0]][inp[1]] = 1;
	}
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			for (int k = 0; k < 2; k++) {
				cin >> rans[i][j][k];
				rans[i][j][k] -= 1;
			}
		}
	}
	for (int j = 0; j < 2; j++) {
		for (int i = rans[j][0][0]; i <= rans[j][1][0]; i++) {
			for (int k = rans[j][0][1]; k <= rans[j][1][1]; k++) {
				//cout << i << k << "---\n";
				if (maps[i][k] == 0) {
					if (groops[j][i][k] == 0) {
						gnum[j] += 1;

						groops[j][i][k] = gnum[j];
						groops_size[j][gnum[j]] = 1;
						groops_pos[j][gnum[j]][0] = i;
						groops_pos[j][gnum[j]][1] = k;
						//bang_num += 1;
						deque<llint_pair> q;
						q.push_back({ i,k });
						while (!q.empty()) {
							int lenq = q.size();
							for (int l = 0; l < lenq; l++) {
								llint_pair dum = q.front();
								q.pop_front();
								for (int o = 0; o < 4; o++) {
									if (dum.first + ang[o][0] < n and dum.first + ang[o][0] > -1 and dum.second + ang[o][1] < m and dum.second + ang[o][1] >-1) {
										if (maps[dum.first + ang[o][0]][dum.second + ang[o][1]] != 1) {
											if (groops[j][dum.first + ang[o][0]][dum.second + ang[o][1]] == 0) {
												q.push_back({ dum.first + ang[o][0],dum.second + ang[o][1] });
												groops[j][dum.first + ang[o][0]][dum.second + ang[o][1]] = gnum[j];
											}
										}
									}
								}
							}
						}


					}
					else {
						groops_size[j][groops[j][i][k]] += 1;
					}




				}
			}
		}
	}
	int j = 0;
	for (int i = 0; i < n; i++) {
		for (int k = 0; k < m; k++) {
			if (maps[i][k] == 0) {
				if (groops[0][i][k] != 0 and groops[1][i][k] != 0) {
					if (comb[groops[0][i][k]][groops[1][i][k]] == 0) {
						comb[groops[0][i][k]][groops[1][i][k]] = 1;
						r += groops_size[0][groops[0][i][k]] * groops_size[1][groops[1][i][k]];
					}
				}
			}
		}
	}
	//for (int i = 0; i < n; i++) {
	//	for (int j = 0; j < m; j++) {
	//		cout << maps[i][j] << " ";
	//	}
	//	cout << "\n";
	//}
	//cout << "\n";
	//for (int i = 0; i < n; i++) {
	//	for (int j = 0; j < m; j++) {
	//		cout << groops[0][i][j] << " ";
	//	}
	//	cout << "\n";
	//}
	//cout << "\n";
	//for (int i = 0; i < n; i++) {
	//	for (int j = 0; j < m; j++) {
	//		cout << groops[1][i][j] << " ";
	//	}
	//	cout << "\n";
	//}
	//for (int i = 1; i < gnum[0] + 1; i++) {
	//	cout << groops_size[0][i] << " ";
	//}
	//cout << "\n";

	//for (int i = 1; i < gnum[1] + 1; i++) {
	//	cout << groops_size[1][i] << " ";
	//}
	//cout << "\n";

	//for (int i = 1; i < gnum[0]+1; i++) {
	//	bang_num += 1;
	//	deque<llint_pair> q;
	//	q.push_back({ groops_pos[0][i][0],groops_pos[0][i][1] });
	//	bang[groops_pos[0][i][0]][groops_pos[0][i][1]] = bang_num;
	//	if (groops[1][groops_pos[0][i][0]][groops_pos[0][i][1]] != 0) {
	//		int dum = groops[1][groops_pos[0][i][0]][groops_pos[0][i][1]];
	//		r += groops_size[0][i] * groops_size[1][dum];
	//		//cout << "asdjnasjd " << i << " " << dum << "\n";
	//		gbang[dum] = bang_num;
	//	}
	//	while (!q.empty()) {
	//		int lenq = q.size();
	//		for (int l = 0; l < lenq; l++) {
	//			llint_pair dum = q.front();
	//			q.pop_front();
	//			for (int o = 0; o < 4; o++) {
	//				if (dum.first + ang[o][0] < n and dum.first + ang[o][0] > -1 and dum.second + ang[o][1] < m and dum.second + ang[o][1] >-1) {
	//					if (maps[dum.first + ang[o][0]][dum.second + ang[o][1]] != 1) {
	//						if (bang[dum.first + ang[o][0]][dum.second + ang[o][1]] != bang_num) {
	//							q.push_back({ dum.first + ang[o][0],dum.second + ang[o][1] });
	//							bang[dum.first + ang[o][0]][dum.second + ang[o][1]] = bang_num;


	//							if (groops[1][dum.first + ang[o][0]][dum.second + ang[o][1]] != 0) {
	//								int dum2 = groops[1][dum.first + ang[o][0]][dum.second + ang[o][1]];
	//								if (gbang[dum2] != bang_num) {
	//									r += groops_size[0][i] * groops_size[1][dum2];
	//									gbang[dum2] = bang_num;
	//								}
	//							}
	//						}
	//					}
	//				}
	//			}
	//		}
	//	}
	//}

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
