#include <iostream>
#include <string>
#include <array>
#include <map>
#include <list>

using namespace std;
int a,p1,p2;
long long int dum;
long long int r;
list<long long int> li;

int main() {
	r = 0;
	cin >> a;
	for (int i = 0; i < a; i++) {
		cin >> dum;
		li.push_back(dum);
	}
	li.sort();
	if (a % 2 == 1) {
		r = li.back();
		li.pop_back();
	}
	for (int i = 0; i < a/2; i++) {
		r = max(r, li.back() + li.front());
		//cout << (li.back() + li.front()) << "\n";

		li.pop_back();
		li.pop_front();

	}
	cout << r;
}
