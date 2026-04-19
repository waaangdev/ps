#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));
#define segment 1000000

int case_ = 1;


struct int_pair {
	int first;
	int second;
};

int a,b;
int ways[1006000][7];
int bang[1006000];
deque<int> q;

int sol() {
	int i2 = 0;
	int dum = 1;
	int num = 2;
	int dum2 = 0;
	for (int i = 0; i < 1000000; i++) {
		ways[num][0] += i2;
		for (int j = 0; j < 6; j++) {
			for (int k = 0; k < i; k++) {
				dum += (k != i - 1) ? 1 : 0;
				ways[num][0] += num - 1;
				ways[num][1] += num + 1;

				ways[num][2] = dum;
				ways[dum][ways[dum][6]++] = num;
				if (k != i - 1) {
					dum2 = dum - 1 + ((j+k==0)?(i2 - 6):0);
					ways[num][3] = dum2;
					ways[dum2][ways[dum2][6]++] = num;
					ways[num][6] = 4;
				}
				else {
					ways[num][6] = 3;
				}
				num++;
			}
		}
		ways[num-1][1] -= i2;

		i2 += 6;
		if (num >= 1000000) {
			break;
		}
	}
	//for (int i = 0; i < 20; i++) {
	//	for (int j = 0; j < 7; j++) {
	//		cout << ways[i][j] << " ";
	//	}
	//	cout << "\n";
	//}

	cin >> a >> b;

	q.push_back(b);
	bang[b] = b;
	if (a == b) {
		cout << a;
	}
	else {
		while (true) {
			int qpop = q.front();
			q.pop_front();
			for (int i = 0; i < 6; i++) {
				int dum = ways[qpop][i];
				if (dum <= 1000000) {
					if (bang[dum] == 0) {
						q.push_back(dum);
						bang[dum] = qpop;
						if (dum == a) {
							while (dum != b) {
								cout << dum << " ";
								dum = bang[dum];
							}
							cout << dum << " ";
							return 0;
						}
					}
				}
			}
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
		if (sol()) break;
	}

	//while (!sol()) {

	//}


}






