//Rush Hour Puzzle
#include <iostream>
#include <deque>
#include <string>
#include <array>
using namespace std;

int lenq, t;
int dum1[2];
int dum2[10];
deque<array<int, 10>> q;
bool bang[5][5][5][5][5][5][5][5][5][5];
bool end_;
int m[6][6];
int ang1[4] = { 0,-1,0,1 };
int ang2[4] = { 1,0,-1,0 };
bool dumli[10];
int cars[10][3];
int carsu = 0;
array<int, 10 > st;

int main() {
	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < 6; j++) {
			cin >> m[i][j];
		}
	}
	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < 6; j++) {
			if (m[i][j] != 0 && !dumli[m[i][j] - 1]) {
				carsu += 1;
				dumli[m[i][j] - 1] = true;
				for (int k = 0; k < 4; k++) {
					if (m[i + ang1[k]][j + ang2[k]] == m[i][j]) {
						if (k % 2 == 1) {
							cars[m[i][j] - 1][0] = 0;
							cars[m[i][j] - 1][1] = j;
							st[m[i][j] - 1] = i;
						}
						else {
							cars[m[i][j] - 1][0] = 1;
							cars[m[i][j] - 1][1] = i;
							st[m[i][j] - 1] = j;
						}

						if (m[i + ang1[k] * 2][j + ang2[k] * 2] == m[i][j]) {
							cars[m[i][j] - 1][2] = 3;
						}
						else {
							cars[m[i][j] - 1][2] = 2;
						}
					}
				}
			}
		}
	}
	/*
	for (int i = 0; i < 10; i++) {
		cout << st[i]<<" ";
	}
	cout << "\n";
	for (int i = 0; i < 10; i++) {
		cout << cars[i][1] << " ";
	}
	cout << "\n";
	*/
	if (cars[0][1] == 2 && st[0] == 4) {
		end_ = true;
	}
	q.push_back(st);
	t = 0;
	while (!q.empty() && !end_) {
		if (t == 8) {
			break;
		}
		t += 1;
		lenq = q.size();
		for (int i = 0; i < lenq; i++) {



			for (int j = 0; j < 6; j++) {
				for (int k = 0; k < 6; k++) {
					m[j][k] = 0;
				}
			}
			for (int j = 0; j < carsu; j++) {
				dum2[j] = q.front()[j];

				dum1[cars[j][0]] = q.front()[j];
				dum1[cars[j][0] * -1 + 1] = cars[j][1];

				m[dum1[0]][dum1[1]] = j + 1;
				dum1[cars[j][0]] += 1;
				m[dum1[0]][dum1[1]] = j + 1;
				if (cars[j][2] == 3) {
					dum1[cars[j][0]] += 1;
					m[dum1[0]][dum1[1]] = j + 1;
				}
			}
			/*
			cout << "\n";
			for (int j = 0; j < 6; j++) {
				for (int k = 0; k < 6; k++) {
					cout << m[j][k];
				}
				cout << "\n";
			}
			cout << "\n";
			*/
			for (int j = 0; j < carsu; j++) {
				dum1[cars[j][0]] = q.front()[j];
				dum1[cars[j][0] * -1 + 1] = cars[j][1];

				for (int l = 1; l < 2; l++) {
					dum1[cars[j][0]] += -1;
					if (dum1[cars[j][0]] == -1) {
						break;
					}
					if (m[dum1[0]][dum1[1]] == 0) {
						dum2[j] = dum1[cars[j][0]];

						if (!bang[dum2[0]][dum2[1]][dum2[2]][dum2[3]][dum2[4]][dum2[5]][dum2[6]][dum2[7]][dum2[8]][dum2[9]]) {
							bang[dum2[0]][dum2[1]][dum2[2]][dum2[3]][dum2[4]][dum2[5]][dum2[6]][dum2[7]][dum2[8]][dum2[9]] = true;
							q.push_back({ dum2[0],dum2[1],dum2[2],dum2[3],dum2[4],dum2[5],dum2[6],dum2[7],dum2[8],dum2[9] });
						}

					}
					else {
						break;
					}
				}
				dum1[cars[j][0]] = q.front()[j];

				for (int l = 1; l < 2; l++) {
					dum1[cars[j][0]] += cars[j][2];
					if (dum1[cars[j][0]] == 6) {
						break;
					}
					if (m[dum1[0]][dum1[1]] == 0) {
						dum1[cars[j][0]] -= cars[j][2] - 1;
						dum2[j] = dum1[cars[j][0]];
						if (j == 0 && dum2[j] + cars[j][2] == 6 && cars[j][1] == 2) {
							end_ = true;
						}
						if (!bang[dum2[0]][dum2[1]][dum2[2]][dum2[3]][dum2[4]][dum2[5]][dum2[6]][dum2[7]][dum2[8]][dum2[9]]) {
							bang[dum2[0]][dum2[1]][dum2[2]][dum2[3]][dum2[4]][dum2[5]][dum2[6]][dum2[7]][dum2[8]][dum2[9]] = true;
							q.push_back({ dum2[0],dum2[1],dum2[2],dum2[3],dum2[4],dum2[5],dum2[6],dum2[7],dum2[8],dum2[9] });
						}

					}
					else {
						break;
					}
				}


				dum2[j] = q.front()[j];
			}

			q.pop_front();
		}
	}
	if (end_) {
		cout << t + 2;
	}
	else {
		cout << -1;
	}

	return 0;
}
