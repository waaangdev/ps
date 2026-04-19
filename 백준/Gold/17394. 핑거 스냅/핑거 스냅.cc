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

deque<int> q;
bool prime[100001];
int dp[1000001];

int sol(int case_) {
	int n,a,b,t;
	t = 0;
	cin >> n >> a>>b;

	q.push_back(n);
	dp[n] = case_ + 1;
	if (n >= a and n <= b) {
		if (!prime[n]) {
			cout << t << '\n';
			return 0;
		}
	}

	while (!q.empty()) {
		t += 1;
		int lenq = q.size();
		for (int i = 0; i < lenq; i++) {
			int qpop = q.front();
			q.pop_front();
			int dumli[] = { qpop + 1 ,qpop - 1,qpop / 2,qpop / 3 };
			for (int j = 0; j < 4; j++) {
				if (dumli[j] <= 1000000 and dumli[j] > -1) {
					if (dp[dumli[j]] != case_ + 1) {
						q.push_back(dumli[j]);
						dp[dumli[j]] = case_ + 1;

						if (dumli[j] >= a and dumli[j] <= b) {
							if (!prime[dumli[j]]) {
								cout << t << '\n';
								while (!q.empty()) {
									q.pop_front();
								}
								return 0;
							}
						}

					}
				}
			}
		}
	}
	cout << -1 << '\n';

	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> case_;


	for (int i = 2; i < 50001; i++) {
		if (!prime[i]) {
			//cout << i << '\n';
			for (int j = i + i; j < 100001; j += i) {
				prime[j] = true;
			}
		}
	}

	for (int i = 0; i < case_; i++) {
		sol(i);
	}

	//while (!sol()) {

	//}


}