//사장님 달려가고 있습니다
#include<iostream>
#include<array>
#include<string>
#include<deque>

using namespace std;

int n,dum1, dum2,lenq,t,dum3;
int m[100][100];
bool bang[100][100][4][15];
//int bang2[100][100][4][15];
deque<array<int, 4>> q;
bool end_;
int ang1[] = { 0,1,0,-1 };
int ang2[] = { 1,0,-1,0 };

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> m[i][j];
		}
	}
	t = 0;
	q.push_back({ 0,0,0,0 });

	while (!q.empty() && !end_) {
		t += 1;
		lenq = q.size();
		for (int i = 0; i < lenq; i++) {
			for (int j = 0; j < 4; j++) {
				dum1 = q.front()[0] + ang1[j]+ (ang1[j]*q.front()[3]) * (j == q.front()[2]);
				dum2 = q.front()[1] + ang2[j] + (ang2[j] * q.front()[3]) * (j == q.front()[2]);
				if (dum1 > -1 && dum1 < n && dum2 > -1 && dum2 < n) {
					dum3 = 0;
					if (j == 0 || j == 2) {
						for (int k = 1; k < ang2[j] + (ang2[j] * q.front()[3]) * (j == q.front()[2]); k++) {
							if (m[q.front()[0] + ang1[j] * k][q.front()[1] + ang2[j] * k] < t && m[q.front()[0] + ang1[j] * k][q.front()[1] + ang2[j] * k] != 0) {
								dum3 = 1;
							}
						}
					}
					else {
						for (int k = 1; k < ang1[j] + (ang1[j] * q.front()[3]) * (j == q.front()[2]); k++) {
							if (m[q.front()[0] + ang1[j] * k][q.front()[1] + ang2[j] * k] < t && m[q.front()[0] + ang1[j] * k][q.front()[1] + ang2[j] * k] != 0) {
								dum3 = 1;
							}
						}
					}
					if ((m[dum1][dum2] > t || m[dum1][dum2] == 0) && !dum3) {
						if (!bang[dum1][dum2][j][1+(q.front()[3]) * (j == q.front()[2])]) {
							q.push_back({ dum1,dum2,j,1+(q.front()[3]) * (j == q.front()[2]) });
							bang[dum1][dum2][j][1+(q.front()[3]) * (j == q.front()[2])] = true;
							if (dum1 == n-1 && dum2 == n-1) {
								end_ = true;
							}
						}
					}
					
				}
			}
			q.pop_front();
		}
	}
	if (end_) {
		cout << t;
	}
	else {
		cout << "Fired";
	}
	return 0;
}