//디피그리디
//24522

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


int m, n;
int li[2][1000000];
int li2[1000000];

bool compare(int a,int b,bool idx) {
	return (a == b or ((idx) and a > 0 and a < b));
}


int naive_kmp(int* li1,int* li2,int ln,int lm) {
	int r = 0;
	for (int i = 0; i < ln - lm + 1; i++) {
		int dum = 1;
		for (int j = 0; j < lm;j++) {
			if (compare(li2[j], li1[i + j], (j==0 or j==lm-1))) {

			}
			else {
				dum = 0;
				break;
			}
		}
		r += dum;
	}
	return r;
}


void sol2(int n, int idx) {
	for (int i = 0; i < (n - 1) * 2 - 1; i++) {
		li[idx][i] = 0;
	}

	int his[2],dum[2];
	int hisangle = 0;
	cin >> his[0] >> his[1];
	int idx2 = 0;
	for (int i = 0; i < n - 1; i++) {
		cin >> dum[0] >> dum[1];
		if (dum[0] < his[0]) {
			//l
			if (i != 0) {
				li[idx][idx2] = (hisangle - 2);
				li[idx][idx2] = (li[idx][idx2] + 1) / 2 - 2;
				idx2 += 1;
			}
			hisangle = 2;
			li[idx][idx2] = abs(dum[0] - his[0]);
		}
		else if (dum[0] > his[0]) {
			//r
			if (i != 0) {
				li[idx][idx2] = (hisangle - 0);
				if (hisangle == 3) {
					li[idx][idx2] = -1;
				}
				li[idx][idx2] = (li[idx][idx2]+1)/2-2;
				idx2 += 1;
			}
			hisangle = 0;
			li[idx][idx2] = abs(dum[0] - his[0]);
		}
		else if (dum[1] < his[1]) {
			//d
			if (i != 0) {
				li[idx][idx2] = (hisangle - 3);
				if (hisangle == 0) {
					li[idx][idx2] = 1;
				}
				li[idx][idx2] = (li[idx][idx2] + 1) / 2 - 2;
				idx2 += 1;
			}
			hisangle = 3;
			li[idx][idx2] = abs(dum[1] - his[1]);
		}
		else if (dum[1] > his[1]) {
			//u
			if (i != 0) {
				li[idx][idx2] = (hisangle - 1);
				li[idx][idx2] = (li[idx][idx2] + 1) / 2 - 2;
				idx2 += 1;
			}
			hisangle = 1;
			li[idx][idx2] = abs(dum[1]- his[1]);
		}
		idx2 += 1;
		his[0] = dum[0];
		his[1] = dum[1];
	}
}

int sol() {
	//kmp 부분이 문제인듯, 파이썬으로 테케 만들어서 테스트ㄱㄱ
	cin >> n >> m;

	int r = 0;
	int naive_r = 0;

	sol2(n, 0);
	sol2(m, 1);

	int lm = (m - 1) * 2 - 1;
	int ln = (n - 1) * 2 - 1;

	for (int j = 0; j < 2; j++) {
		naive_r += naive_kmp(li[0], li[1], ln, lm);

		for (int i = 1; i < lm; i++) {
			li2[i] = 0;
		}
		int idx = 0;
		for (int i = 1; i < lm; i++) {
			if (compare(li[1][idx], li[1][i], (idx == 0 or idx == lm - 1))) {
				idx++;
				li2[i] = idx;
			}
			else {
				//idx = 0;
				if (idx == 0) {
					idx = 0;
				}
				else {
					idx = li2[idx - 1];
					i -= 1;
				}
			}
		}


		//for (int i = 1; i < lm; i++) {
		//	cout << li2[i] << ",";
		//}
		//cout << "\n";
		//for (int i = 0; i < (n - 1) * 2 - 1; i++) {
		//	if(li[0][i] > 0)cout << li[0][i] << ",";
		//	else cout << "LR"[abs(li[0][i])-1] << ",";
		//}
		//cout << "\n";
		//for (int i = 0; i < (m - 1) * 2 - 1; i++) {
		//	cout << li[1][i]<<",";
		//}
		//cout << "\n";
		//cout <<r<< " r\n";

		idx = 0;
		for (int i = 0; i < ln; i++) {
			//cout <<"kmp " << idx<<" " << i << "\n";
			if (compare(li[1][idx], li[0][i], (idx == 0 or idx == lm - 1))) idx++;
			else {
				if (idx == 0) {
					idx = 0;
				}
				else {
					idx = li2[idx - 1];
					i -= 1;

				}
			}
			if (idx == lm) {
				if (compare(li[1][li2[idx - 2]], li[0][i], true)) {
					idx = li2[idx -2]+1;
				}
				else {
					idx = li2[idx - 1];
				}
				r += 1;
				//if (compare(li[1][idx], li[0][i], (idx == 0 or idx == lm - 1))) {
				//	idx += 1;
				//}
			}
		}
		//cout << "\n";

		int dum = 0;
		int dum2 = 0;
		for (int i = 0; i < lm/2; i++) {
			swap(li[1][i], li[1][lm-1-i], dum);
			if ((li[1][i] > 0 and li[1][i] != li[1][lm - 1 - i]) or (li[1][i] < 0 and (li[1][lm - 1 - i] > 0 or li[1][i] == li[1][lm - 1 - i]))) {
				dum2 = 1;
			}
		}
		if (lm % 2 == 1 and li[1][lm / 2] < 0) {
			dum2 = 1;
		}
		if (dum2 == 0) {
			break;
		}
		for (int i = 0; i < lm; i++) {
			if (li[1][i] == -1) {
				li[1][i] = -2;
			}else if (li[1][i] == -2) {
				li[1][i] = -1;
			}
		}
	}
	cout << r;// << " " << naive_r << "\n";
	//if (r != naive_r) {
	//	cout << "no!!!!!!!!!!!!!!!!!!!!!\n";
	//	return 1;
	//}
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






