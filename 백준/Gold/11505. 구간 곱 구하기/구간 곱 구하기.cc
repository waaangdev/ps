//찾기
#include <bits/stdc++.h>
#include <sstream>

using namespace std;

typedef unsigned long long int llint;

typedef struct st {
	llint first, second;
} node;


llint a,b,c;
llint li[21][1000000];

llint solve(llint l, llint r, llint i,llint j,llint a) {
	//cout << l << " " <<r << " " << i << " " << j << " " << a << "\n";
	if (l == j*a and r == l+a) {
		return li[i][j];
	}
	if (l < j * a + a / 2 and r <= j * a + a / 2) {
		return solve(l,r,i-1,j*2,a/2);
	}
	else if (l >= j * a + a / 2 and r > j * a + a / 2) {
		return solve(l, r, i - 1, j * 2+1, a / 2);
	}
	else {
		return solve(l, j * a + a / 2, i - 1, j * 2, a / 2) * solve(j * a + a / 2, r, i - 1, j * 2 + 1, a / 2)% 1000000007;
	}
}


int main(){
	cin >> a >> b >> c;

	for (int i = 0; i < a; i++) {
		cin >> li[0][i];
	}

	llint dum = a/2;
	for (int i = 1; i < 21; i++) {
		fill(li[i], li[i] + dum + 1, 1);
		dum /= 2;
	}
	dum = a / 2;
	llint dumhis = a;
	for (int i = 1; i < 21; i++) {
		li[i - 1][dumhis] = 1;
		for (int j = 0; j < dum+1; j++) {
			li[i][j] = li[i - 1][j * 2] * li[i - 1][j * 2 + 1] % 1000000007;
			//cout << li[i][j] << " ";
		}
		//cout << "\n";
		dum /= 2;
		dumhis = (dumhis%2==0)?dumhis/2: dumhis/2+1;
	}

	for (int i = 0; i < b+c; i++) {
		llint m, inp1, inp2;
		cin >> m >> inp1 >> inp2;
		if (m==1) {
			inp1 -= 1;
			li[0][inp1] = inp2;
			llint dum2 = inp1/2;
			for (int j = 1; j < 21; j++) {
				li[j][dum2] = li[j - 1][dum2 * 2] * li[j - 1][dum2 * 2 + 1] % 1000000007;
				dum2 /= 2;
			}

			//dum = a / 2;
			//for (int i = 1; i < 21; i++) {
			//	for (int j = 0; j < dum + 1; j++) {
			//		cout << li[i][j] << " ";
			//	}
			//	cout << "\n";
			//	dum /= 2;
			//}

		}
		else {
			inp1 -= 1;
			cout << solve(inp1, inp2,20,0,pow(2,20)) << "\n";
		}
	}
}
