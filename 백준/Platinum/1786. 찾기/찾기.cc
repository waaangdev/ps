//찾기
#include <bits/stdc++.h>
#include <sstream>

using namespace std;

typedef long long int llint;

typedef struct st {
	llint first, second;
} node;


string n, m;
int li[1000001];
int r2[1000001];
	
int p1, p2,p3;

int r = 0;
int jst = 0;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	getline(cin, n);
	getline(cin, m);
	if (n.length() < m.length()) {
		cout << 0;
		return 0;
	}
	int dum1 = 0;
	int dum2 = 1;
	while (dum2 < m.length()) {
		if (m[dum1] == m[dum2]) {
			li[dum2] = dum1+1;
			dum1++;
		}
		else {
			if(dum1!=0)dum2--;
			dum1 = li[dum1-1];
		}
		dum2++;
	}
	//for (int i = 0; i < m.length(); i++) {
	//	cout << li[i] << "";
	//}
	//cout << '\n';
	p1 = 0;
	p2 = 0;
	p3 = 0;
	while (p1 < n.length()) {
		if (n[p1] != m[p2]) {
			if (p2 == 0) {
				p1 += 1;
				p3 = p1;
			}
			else {
				p2 = li[p2 - 1];
				p3 = p1 - p2;
			}
		}
		else {
			p1 += 1;
			p2 += 1;
		}
		if (p2 == m.length()) {
			r2[r] = p3+1;
			r += 1;
			p2 = li[p2 - 1];
			p3 = p1 - p2;
		}
		//cout << p1 << " "<< p2 << '\n';
	}
	cout << r << '\n';
	for (int i = 0; i < r; i++) {
		cout << r2[i] << "\n";
	}

}
