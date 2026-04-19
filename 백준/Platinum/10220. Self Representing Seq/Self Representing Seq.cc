#include <iostream>
#include <string>
#include <array>
#include <map>
#include <list>

using namespace std;
int a,b;
array<int, 100> li;
array<int, 101> su;

int main() {
	cin >> a;
	for (int i = 0; i < a; i++) {
		cin >> b;
		if (b <= 6) {
			if (b == 4) {
				cout << "2\n";
			}
			else if (b == 5) {
				cout << "1\n";
			}
			else {
				cout << "0\n";
			}
		}
		else {
			cout << "1\n";
		}
	}
}
