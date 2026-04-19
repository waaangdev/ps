#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));

int case_ = 1;


struct llint_pair {
	llint first;
	llint second;
};

struct pairs {
	int x;
	int y;
	vector<int> li;
};

int n;
string li,r;
deque<int> q;

int sol() {
	cin >> n;
	cin >> li;
	
	for (int i = n - 1; i > -1; i--) {
		if (li[i] == 'S') {
			if (q.empty()) {
				r += "U";
				q.push_back(1);
			}
			else {
				if (q.front() == 1) {
					r += "U";
					q.push_back(1);
				}
				else {
					q.pop_front();
				}
			}
		}
		else {
			if (q.empty()) {
				r += "S";
				q.push_back(0);
			}
			else {
				if (q.front() == 0) {
					r += "S";
					q.push_back(0);
				}
				else {
					q.pop_front();
				}
			}
		}
		r += "N";
	}

	cout << r.size()<<"\n";
	cout << r;
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






