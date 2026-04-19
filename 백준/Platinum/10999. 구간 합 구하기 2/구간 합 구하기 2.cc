//구간 합 구하기 2
#include <bits/stdc++.h>
#include <sstream>

using namespace std;

typedef long long int llint;

typedef struct st {
	llint first, second;
} node;


llint a, b, c;
llint li[21][1000000];
vector<array<llint, 3>> li2;

llint solve(llint l, llint r, llint i, llint j, llint a) {
	//cout << l << " " <<r << " " << i << " " << j << " " << a << "\n";
	if (l == j * a and r == l + a) {
		return li[i][j];
	}
	if (l < j * a + a / 2 and r <= j * a + a / 2) {
		return solve(l, r, i - 1, j * 2, a / 2);
	}
	else if (l >= j * a + a / 2 and r > j * a + a / 2) {
		return solve(l, r, i - 1, j * 2 + 1, a / 2);
	}
	else {
		return solve(l, j * a + a / 2, i - 1, j * 2, a / 2) + solve(j * a + a / 2, r, i - 1, j * 2 + 1, a / 2);
	}
}


int main() {
    ios_base::sync_with_stdio(false);
cin.tie(NULL);
cout.tie(NULL);
	cin >> a >> b >> c;

	for (int i = 0; i < a; i++) {
		cin >> li[0][i];
	}

	llint dum = a / 2;
	for (int i = 1; i < 21; i++) {
		fill(li[i], li[i] + dum + 1, 1);
		dum /= 2;
	}
	dum = a / 2;
	llint dumhis = a;
	for (int i = 1; i < 21; i++) {
		li[i - 1][dumhis] = 1;
		for (int j = 0; j < dum + 1; j++) {
			li[i][j] = li[i - 1][j * 2] + li[i - 1][j * 2 + 1];
			//cout << li[i][j] << " ";
		}
		//cout << "\n";
		dum /= 2;
		dumhis = (dumhis % 2 == 0) ? dumhis / 2 : dumhis / 2 + 1;
	}

	for (int i = 0; i < b + c; i++) {
		llint m, inp1, inp2, inp3;
		cin >> m >> inp1 >> inp2;
		if (m == 1) {
			cin >> inp3;
			inp1 -= 1;
			li2.push_back({ inp1,inp2,inp3 });
		}
		else {
			inp1 -= 1;
			llint r;
			r = solve(inp1, inp2, 20, 0, pow(2, 20));
			for (int j = 0; j <li2.size(); j++) {
				if (inp1 >= li2[j][0] and inp1 < li2[j][1]) {
					r += min(inp2 - inp1, li2[j][1] - inp1) * li2[j][2];
				}
				else if (inp2 >= li2[j][0] and inp2 < li2[j][1]) {
					r+= (inp2-li2[j][0]) * li2[j][2];
				}
				else if (li2[j][0] >= inp1 and li2[j][0] < inp2) {
					r += (li2[j][1] - li2[j][0]) * li2[j][2];
				}
			}
			cout << r << "\n";
		}
	}
}
