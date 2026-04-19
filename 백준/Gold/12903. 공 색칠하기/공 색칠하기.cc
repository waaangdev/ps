
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

int Fact[2001];

llint FastPow(llint a, llint b) {//a^b%.. https://heahgo.tistory.com/entry/%EB%AA%A8%EB%93%88%EB%9F%AC-%EA%B1%B0%EB%93%AD%EC%A0%9C%EA%B3%B1-%EC%97%B0%EC%82%B0
	a %= 1000000007;
	b %= 1000000007;

	llint r = 1;
	llint i = 0;
	llint dum = a;
	while (b) {
		if ((b & 1) == 1) {
			r *= dum;
			r %= 1000000007;
		}
		b = b >> 1;
		i += 1;

		dum *= dum;
		dum %= 1000000007;
	}
	return r;
}


llint EulerDivide(llint a, llint b) {
	a %= 1000000007;
	b %= 1000000007;

	return a * FastPow(b, 1000000007-2) % 1000000007;
}

llint C(llint a, llint b) {
	//aCb
	if (b > a / 2) return C(a, a - b);
	llint up = (llint)Fact[a] % 1000000007;
	llint down = (llint)Fact[b] * (llint)Fact[a-b] % 1000000007;


	return EulerDivide(up,down);
}

llint H(llint a, llint b) {
	//aHb
	return C(a + b - 1, b);
}


int sol() {
	llint k;
	cin >> k;
	llint li[1000];
	for (llint i = 0; i < k; i++) {
		cin >> li[i];
	}

	llint r = 1;

	int dum = 1;
	Fact[0] = dum;
	for (llint i = 1; i < 2001; i++) {
		dum = ((llint)dum * (i)) % 1000000007;
		Fact[i] = dum;
	}
	llint dum2 = 0;
	for (llint i = 0; i < k; i++) {
		r *= H(dum2+1, li[i]-1);
		r %= 1000000007;
		dum2 += li[i];
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