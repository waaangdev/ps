#include <iostream>
#include <string>
#include <array>
#include <map>
#include <list>

using namespace std;
int w, h, case1, dumy, dumx, dum, r;
char get1;
array<array<char, 20>, 20> m;
int main() {
	cin >> case1;
	for (int ii = 0; ii < case1; ii++) {
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
		r = 1;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (m[i][j] != 'F') {
					dum = 0;
					for (int ang = -1; ang < 2; ang++) {
						for (int ang2 = -1; ang2 < 2; ang2++) {
							dumy = i + ang;
							dumx = j + ang2;
							if (dumy > -1 && dumy < h && dumx > -1 && dumx < w) {
								dum += (m[dumy][dumx] == 'F');
							}
						}
					}
					if (dum != (m[i][j] - '0')) {
						r = 0;
					}
				}
				if (m[i][j] == 'F') {
					dum = 0;
					for (int ang = -1; ang < 2; ang++) {
						for (int ang2 = -1; ang2 < 2; ang2++) {
							dumy = i + ang;
							dumx = j + ang2;
							if (dumy > -1 && dumy < h && dumx > -1 && dumx < w) {
								dum += (m[dumy][dumx] != 'F');
							}
						}
					}
					if (dum == 0) {
						r = 0;
					}
				}
			}
		}
		if (r == 1) {
			cout << "Well done Clark!\n";
		}
		else {
			cout << "Please sweep the mine again!\n";
		}
	}
}
