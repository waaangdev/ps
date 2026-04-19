
//디피그리디

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

int score[36][200];
int alladd[200];

int sol() {
	int n,k;
	string inp;
	cin >> n;
	for (llint i = 0; i < n; i++) {
		cin >> inp;
		for (llint j = 0; j < inp.length();j++) {
			int dum1 = 0;
			if (inp[j] >= '0' and inp[j] <= '9') {
				dum1 = inp[j] - '0';
			}
			else {
				dum1 = inp[j] - 'A'+10;
			}
			int jdum = 199- inp.length()+j+1;
			alladd[jdum] += dum1;
			score[dum1][jdum] += 35-dum1;
			while (score[dum1][jdum] >= 36) {
				score[dum1][jdum - 1] += score[dum1][jdum] / 36;
				score[dum1][jdum] = score[dum1][jdum] % 36;
				jdum -= 1;
			}
		}
	}

	cin >> k;
	for (llint i = 0; i < k; i++) {
		int maxidx = 0;
		for (llint j = 0; j < 36; j++) {
			for (llint k = 0; k < 200; k++) {
				if (score[maxidx][k] != score[j][k]) {
					if (score[maxidx][k] < score[j][k]) {
						maxidx = j;
					}
					break;
				}
			}
		}
		for (llint k = 199; k > -1; k--) {
			alladd[k] += score[maxidx][k];
			score[maxidx][k] = -1;
		}
		for (llint k = 199; k > 0; k--) {
			alladd[k - 1] += alladd[k] / 36;
			alladd[k] = alladd[k] % 36;
		}
	}
	int rlen = 199;
	for (llint k = 199; k > 0; k--) {
		alladd[k - 1] += alladd[k] / 36;
		alladd[k] = alladd[k] % 36;
		if (alladd[k] != 0) {
			rlen = k;
		}
	}
	for (llint k = rlen; k < 200; k++){
		if (alladd[k] < 10) {
			cout << alladd[k];
		}
		else {
			cout << (char)(alladd[k]-10+'A');
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