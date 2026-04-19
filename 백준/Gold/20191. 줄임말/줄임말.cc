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


int m, n;

string s;
string t;
vector<int> li[26];
int lli[26];

int binsearch(int l, int r,int num,int idx) {
	///cout << "-" << l << " " << r << " "<<l + (r - 1) / 2 << "\n";
	if (l >= r) {
		return -1;
	}
	if (l + 1 == r) {
		if (li[idx][l] >= num){
			return l;
		}
		else {
			return -1;
		}
	}
	int dum = (l + (r-1)) / 2;
	if (li[idx][dum] < num ) {
		return binsearch(dum + 1, r, num, idx);
	}
	else if(li[idx][dum] > num){
		return binsearch(l, dum+1, num, idx);
	}
	else {
		return dum;
	}
}


int sol() {
	cin >> s;
	cin >> t;
	int r=1;
	for (int i = 0; i < t.size(); i++) {
		li[t[i] - 'a'].push_back(i);
	}


	int poi = 0;
	for (int i = 0; i < s.size(); i++) {
		int dum2 = s[i] - 'a';
		//cout << "asdasd";
		if (li[dum2].size() == 0) {
			r = -1;
			break;
		}
		while (1) {
			//cout << poi << " " << dum2 << " " << "dum" << "\n";
			int dum = binsearch(lli[dum2], li[dum2].size(), poi, dum2);
			//cout << poi << " " << dum2 << " " << dum << "\n";
			if (dum == -1) {
				r += 1;
				for (int j = 0; j < 26; j++) {
					lli[j] = 0;
				}
				poi = 0;
			}
			else {
				lli[dum2] = dum;
				poi = li[dum2][dum]+1;
				break;
			}
		}
	}

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






