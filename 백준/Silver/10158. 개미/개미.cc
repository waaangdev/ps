#include <iostream>
#include <string>
#include <array>
#include <map>
#include <list>

using namespace std;
int x, y,w,h,t;
int main() {
	cin >> w >> h;
	cin >> x >> y;
	cin >> t;
	int i = t;
	if (((x + i) / w) % 2 == 0) {
		cout << (x + i) % w;
	}
	else {
		cout << w - ((x + i) % w);
	}
	cout << " ";
	if (((y + i) / h) % 2 == 0) {
		cout << (y + i) % h;
	}
	else {
		cout << h - ((y + i) % h);
	}
	cout << "\n";
	

}


/*
int w, h,dum,dum2,dum3,dum4;
char get1;
array<array<int, 600>, 600> m;
array<array<pair<array<array<int, 3>, 9>,int>, 600>, 600> m2;//array<int,3> : [좌표,주변에 있는 지뢰수,감지한 타일 수]
array<array<int, 2>, 360000> gam; //array<int,2> [감지한 총 타일 수,내가 감지한 타일수] 
array<array<bool, 600>, 600> rm;

int main() {
	cin >> h >> w;
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			get1 = cin.get();
			if (get1 == '\n') {
				get1 = cin.get();
			}
			m[i][j] = get1;
		}
	}
	while (1) {
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				dum = 0;

				for (int k = -1; k < 2; k++) {
					for (int l = -1; l < 2; l++) {
						if (i + k > -1 && i + k < h && j + l > -1 && j + l < w) {
							
						}
					}
				}

				for (int k = -1; k < 2; k++) {
					for (int l = -1; l < 2; l++) {
						if (i + k > -1 && i + k < h && j + l > -1 && j + l < w) {
							dum += 1;
						}
					}
				}

				for (int k = -1; k < 2; k++) {
					for (int l = -1; l < 2; l++) {
						if (i + k > -1 && i + k < h && j + l > -1 && j + l < w) {
							dum2 = m2[i + k][j + l].second;
							m2[i + k][j + l].first[dum2] = { (i + k) * 600 + (j + l),m[i][j],dum };
						}
					}
				}
			}
		}


	}

}
*/