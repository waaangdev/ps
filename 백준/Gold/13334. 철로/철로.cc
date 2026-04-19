//철로
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

typedef struct st {
	llint first, second;
} node;

llint n,d,r1,r;
deque<array<llint, 2>> inp_li;
deque<array<llint, 2>> li[2];

bool compare(array<llint, 2> a, array<llint, 2> b) {
	return a[0] < b[0];
}


int main() {
	cin >> n;

	for (int i = 0; i < n; i++) {
		llint inp1, inp2;
		cin >> inp1 >> inp2;
		if (inp1 > inp2) {
			inp_li.push_back({ inp2,inp1 });
		}
		else {
			inp_li.push_back({ inp1,inp2 });
		}

	}
	cin >> d;
	for (int i = 0; i < n; i++) {
		if (inp_li[i][1] - inp_li[i][0] <= d) {
			li[0].push_back({ inp_li[i][0] ,i });
			li[1].push_back({ inp_li[i][1]-d ,i });
		}

	}
	sort(li[0].begin(), li[0].end(),compare);
	sort(li[1].begin(), li[1].end(), compare);

	while (!li[0].empty() or !li[1].empty()) {
		int dum = 0;
		array<llint, 2> dum2;
		if (li[0].empty()) {
			dum = 1;
		}
		else if (li[1].empty()) {
			dum = 0;
		}
		else {
			if (li[0].front()[0] < li[1].front()[0]) {
				dum = 0;
			}
			else {
				dum = 1;
			}
		}
		dum2 = li[dum].front();
		li[dum].pop_front();
		//cout << dum << "   " << dum2[0] << " " << dum2[1] << "\n";

		r1 += dum * 2 - 1;
		r = max(r1, r);
	}
	cout << r;
}
