//행렬 연산 (행렬 계산하기)

#include <iostream>
#include <array>
#include <deque>
#include <string>

using namespace std;

int a, b, c,d,e,f,dum,dum2;

int li[500000];
int li2[500000];

int main() {
	cin >> a;
	cin >> b;
	cin >> c;
	for (int i = 0; i < c; i++) {
		cin >> d >> e >> f;
		if (d == 1) {
			li[e - 1] += f;
		}
		else if (d == 2) {
			li2[e - 1] += f;
		}
		/*
		if (d == 1) {
			for (int j= 0; j < b; j++) {
				li[(e - 1) *b + j] += f;
			}
		}
		else if (d == 2) {
			for (int j = 0; j < a; j++) {
				li[(e - 1) + j*b] += f;
			}
		}*/
	}
	for (int i = 0; i < a; i++) {
		dum = li[i];
		for (int j = 0; j < b; j++) {
			dum2 = li2[j];
			cout << dum+dum2 << " ";
		}
		cout << "\n";
	}

	return 0;
}