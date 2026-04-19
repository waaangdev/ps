#include <iostream>
#include <string>
#include <array>
#include <map>
#include <list>

using namespace std;
int a;
long long int b, c, r;
array<int, 100001> poi;
array<int, 100001> way;

int main() {
	cin >> a;
	for (int i = 0; i < a - 1; i++) {
		cin >> way[i];
	}
	for (int i = 0; i < a; i++) {
		cin >> poi[i];
	}
	c = poi[0] + 1;
	b = 0;
	r = 0;
	for (int i = 0; i < a - 1; i++) {

		if (c > poi[i]) {
			r += c * b;
			c = poi[i];
			b = 0;
		}
		b += way[i];
	}
	r += c * b;
	cout << r;
}
