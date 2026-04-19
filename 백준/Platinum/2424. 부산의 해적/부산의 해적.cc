// 부산의 해적
#include <iostream>
#include<string>
#include<deque>
#include <array>
using namespace std;

int h, w;
bool m[700][700];
string inp;
array<int, 2> hst;
array<int, 2> sst;
array<int, 2> mok;
array<deque<array<int, 2>>,2> q;
bool hbang[700][700][6];
bool sbang[700][700];
int lenq;
array<int, 2> qpop;
array<array<int, 2>, 4> ang;
int dum1,dum2, dum3, dum4;
bool end_;


int main() {
	ang[0] = { 0,1 };
	ang[1] = { 0,-1 };
	ang[2] = { -1,0 };
	ang[3] = { 1,0 };

	cin >> h >> w;
	for (int i = 0; i < h; i++) {
		cin >> inp;
		for (int j = 0; j < w; j++) {
			if (inp[j] == 'I') {
				m[i][j] = true;
			}
			else if (inp[j] == 'V') {
				hst[0] = i;
				hst[1] = j;
			}
			else if (inp[j] == 'Y') {
				sst[0] = i;
				sst[1] = j;
			}
			else if (inp[j] == 'T') {
				mok[0] = i;
				mok[1] = j;
			}
		}
	}

	q[0].push_back(sst);
	q[1].push_back(hst);

	end_ = false;

	while (!q[0].empty() && !end_) {


		for (int i = 1; i > -1; i--) {
			lenq = q[i].size();
			for (int j = 0; j < lenq; j++) {

				qpop = q[i].front();
				q[i].pop_front();



				for (int k = 0; k < 4; k++) {
					dum1 = qpop[0] + ang[k][0];
					dum2 = qpop[1] + ang[k][1];
					if (dum1 > -1 && dum1 < h && dum2 > -1 && dum2 < w) {
						if (i == 0) {
							
							if (!sbang[dum1][dum2] && !hbang[dum1][dum2][4] && !m[dum1][dum2]) {
								sbang[dum1][dum2] = true;
								q[0].push_back({dum1,dum2});
								
								if (dum1 == mok[0] && dum2 == mok[1]) {
									end_ = true;
								}
							}
						}
						else {
							if (!hbang[dum1][dum2][5] && !m[dum1][dum2]) {
								q[1].push_back({ dum1,dum2 });

								hbang[dum1][dum2][5] = true;
								hbang[dum1][dum2][4] = true;

								for (int l = 0; l < 4; l++) {
									for (int o = 1; o < 700; o++) {
										dum3 = dum1 + ang[l][0] * o;
										dum4 = dum2 + ang[l][1] * o;
										if (dum3 < 0 || dum3 >= h || dum4 < 0 || dum4 >= w) {
											break;
										}
										if (m[dum3][dum4] || hbang[dum3][dum4][l]) {
											break;
										}
										hbang[dum3][dum4][l] = true;
										hbang[dum3][dum4][4] = true;
									}
								}
								
							}
						}
					}
				}

			}

		}
	}
	if (end_) {
		cout << "YES";
	}
	else {
		cout << "NO";
	}
	return 0;
}
