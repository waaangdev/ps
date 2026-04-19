//배열 알아맞히기

#define _USE_MATH_DEFINES

#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

struct node {
	int first;
	int second;
};

llint n, a, b, k;
llint li[200];
vector<llint> li2;
bool bang[500001];
bool bang2[200];
map<double, llint> m;

int main() {
	cin >> n;
	bang[0] = true;
	for (int i = 0; i < min((llint)200, n); i++) {
		llint random = 0;
		while (bang[random]) random = rand() % (n)+1;
		bang[random] = true;
		//cout << random << "\n";
		li2.push_back(random);

	}
	sort(li2.begin(), li2.end());
	llint hapdum[3] = { 0,0,0 };
	cout << "? " << li2[0] << " " << li2[1] << "\n";
	cin >> hapdum[0];
	cout << "? " << li2[0] << " " << li2[2] << "\n";
	cin >> hapdum[1];
	cout << "? " << li2[1] << " " << li2[2] << "\n";
	cin >> hapdum[2];

	llint chai = hapdum[0] - hapdum[1];//1-2
	llint hap = hapdum[2];//1+2
	li[1] = (chai + hap) / 2;
	li[2] = hap - li[1];
	li[0] = hapdum[0] - li[1];

	for (int i = 3; i < min((llint)200, n); i++) {
		cout << "? " << li2[0] << " " << li2[i] << "\n";
		llint dum;
		cin >> dum;
		li[i] = dum - li[0];
	}
	// for (int i = 0; i < min((llint)200, n); i++) {
	// 	cout << li2[i] << " " << li[i]<<"\n";
	// }

	llint giulgimax_c = 0;
	llint giulgimax_anyy = 0;
	llint giulgimax_anyy_x = 0;
	double giulgimax = 0;
	for (int i = 1; i < min((llint)200, n); i++) {
		double dum = (double)(li[i] - li[0]) / (double)(li2[i] - li2[0]);
		m[dum] += 1;
		if (m[dum] > 1) {
			giulgimax = dum;
			giulgimax_c = m[dum];
			giulgimax_anyy = li[i];
			giulgimax_anyy_x = li2[i];
		}
	}

	bang2[0] = false;
	llint nongiulgimax_anyy = 0;
	llint nongiulgimax_anyy_x = 0;
	for (int i = 1; i < min((llint)200, n); i++) {
		double dum = (double)(li[i] - li[0]) / (double)(li2[i] - li2[0]);
		if (dum == giulgimax) {
			bang2[i] = false;
		}
		else {
			nongiulgimax_anyy = li[i];
			nongiulgimax_anyy_x = li2[i];
		}
	}

	
	llint gongcha = (giulgimax_anyy - li[0]) / (giulgimax_anyy_x - li2[0]);
	llint chohang = li[0] - (li2[0] - 1) * gongcha;

	llint kdum = (nongiulgimax_anyy_x - 1) * gongcha + chohang;
	llint kdum_chai = nongiulgimax_anyy - kdum;
	//cout<< giulgimax_c;
	if(giulgimax_c == 0){
		gongcha = (li[2] - li[1]) / (li2[2] - li2[1]);
		chohang = li[1] - (li2[1] - 1) * gongcha;
		kdum = (li2[0] - 1) * gongcha + chohang;
		kdum_chai = li[0] - kdum;
	}

	if (kdum_chai > 0) {
		cout << "! " << gongcha << " " << chohang << " " << kdum_chai << "\n";
	}
	else {
		cout << "! " << gongcha << " " << chohang + kdum_chai << " " << -kdum_chai << "\n";
	}
}






