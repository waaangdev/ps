//요세푸스 문제 2

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));

int n, m;
int way[1000000];
multiset<int> li;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		int inp;
		cin >> inp;
		way[i] = inp;
	}
	int dum = min(n, (m) * 2-1);
	for (int i = 0; i < dum; i++) {
		li.insert(way[i]);
	}
	cout << *(--li.end()) << " ";
	int p2 = 0;
	for (int i = dum; i < n; i++) {
		li.erase(li.find(way[p2]));
		li.insert(way[i]);
		cout << *(--li.end()) << " ";
		p2 += 1;
	}
}






