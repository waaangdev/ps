
#include <bits/stdc++.h>
#include <sstream>

using namespace std;

typedef long long int llint;

typedef struct st {
	llint first, second;
} node;


vector<node> li[17];

int n, m;

llint O;
//
//pair<llint, llint> solve(llint a, llint b, llint c,int d) {
//
//	pair<llint, llint> r = make_pair(1000000000,0);
//	if (a == b) {
//		return r;
//	}
//	cout << a << " " << b << " " << c << "\n";
//
//	if (c == 1) {
//		for (int i = a; i < b; i++) {
//			O += 1;
//			r.first = min(r.first, li[d][i].first);
//			r.second = max(r.second, li[d][i].second);
//		}
//		return r;
//	}
//	if ((b - a) >= c) {
//		llint left = (a)+(c - (a) % c);
//		if (a % c == 0) left = a;
//		llint right = b - (b % c);
//
//		pair<llint, llint> r2 = solve(a, left, c / 2, d - 1);
//		r.first = min(r.first, r2.first);
//		r.second = max(r.second, r2.second);
//		r2 = solve(right, b, c / 2, d - 1);
//		r.first = min(r.first, r2.first);
//		r.second = max(r.second, r2.second);
//		if (left != right) {
//			llint dum = left / c;
//			llint dum2 = right / c;
//			for (int i = dum; i < dum2; i++) {
//				O += 1;
//				r.first = min(r.first, li[d][i].first);
//				r.second = max(r.second, li[d][i].second);
//			}
//		}
//		return r;
//
//	}
//	else {
//		return solve(a, b, c / 2,d-1);
//	}
//}

node solve(llint a, llint b, llint c, int d, llint index) {
	//cout << a << " " << b << " " << c << " " << index << "\n";
	//if(a==b) return make_pair(1000000000, 0);

	if (a == index*c and a+c==b) {
		return li[d][index];
	}
	llint dum = index * c + c / 2;
	if (a < dum and b < dum+1) {
		return solve(a, b, c / 2, d - 1, index*2);
	}
	else if (a >= dum and b >= dum + 1) {
		return solve(a, b, c / 2, d - 1, index * 2+1);
	}
	else {
		node r = solve(a, dum, c / 2, d - 1, index * 2);

		node r2 = solve(dum, b, c / 2, d - 1, index * 2+1);
		r.first = min(r.first, r2.first);
		r.second = max(r.second, r2.second);

		return r;
	}
}



int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);


	cin >> n >> m;

	int dum = 1;
	int dum3 = 0;
	for (int i = 0; i < 17; i++) {
		if (n >= dum) {
			li[i] = vector<node>((n % dum != 0) ? n / dum + 1 : n / dum, { 1000000000, 0 });
			dum3 += 1;
		}
		dum *= 2;
	}
	//cout <<"dum3: " << dum3 << "\n";
	for (int i = 0; i < n; i++) {
		llint inp;
		cin >> inp;

		li[0][i].first = inp;
		li[0][i].second = inp;

		//int dum = 1;
		//for (int j = 0; j < dum3; j  ++) {
		//	int dumdum = (i) / dum;
		//	if (n / dum > dumdum) {
		//		//cout << "j: " << j << " k: " << k << " (i-k) / dum: " << (i - k) / dum << "\n";
		//		li[j][dumdum].first = min(li[j][dumdum].first, inp);
		//		li[j][dumdum].second = max(li[j][dumdum].second, inp);
		//		O += 1;
		//	}
		//	dum *= 2;
		//}
	}
	if (1) {
		int dum = 2;
		for (int j = 1; j < dum3; j++) {
			int dumdum = (n) / dum;
			for (int i = 0; i < dumdum; i++) {
				li[j][i].first = min(li[j - 1][i * 2].first, li[j - 1][i * 2 + 1].first);
				li[j][i].second = max(li[j - 1][i * 2].second, li[j - 1][i * 2 + 1].second);
			}
			dum *= 2;
		}
	}


	//cout << pow(2, dum3) << "\n";
	for (int i = 0; i < m; i++) {
		llint inp1,inp2;
		cin >> inp1 >> inp2;
		inp1 -= 1;

		node r = solve(inp1,inp2, pow(2, dum3 ),dum3,0);
		//llint min_ = 1000000000;
		//int dum = pow(2,dum3-1);
		//for (int j = 0; j < dum3; j++) {
		//	llint chai = inp2 - inp1;
		//	//cout << "dum: " << dum << "\n";
		//	//cout << "inp1: " << inp1 << " inp2: " << inp2 << "\n";
		//	if (chai >= dum) {



		//		//cout << "j: " << j << " inp1 % dum: " << inp1 % dum << " (inp1) / dum: " << (inp1) / dum << "\n";
		//		//max_ = max(max_, li[dum3-1-j][inp1 % dum][(inp1) / dum].second);
		//		//min_ = min(min_, li[dum3 - 1 - j][inp1 % dum][(inp1) / dum].first);
		//		//inp1 += dum;
		//	}
		//	dum /= 2;
		//}


		cout << r.first << " " << r .second<<"\n";
		
	}
	//cout << O;
}
