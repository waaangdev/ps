#include <iostream>
#include <string>
#include <array>
#include <map>
#include <list>

using namespace std;
int a,b,c,r;
list<int> li;

int main() {
	cin >> a;
	for (int i = 0; i < a; i++) {
		cin >> b;
		li.push_back(b);
	}
	r = -1;
	li.sort();
	li.reverse();
	for (int i = 0; i < a; i++) {
		c = li.front() * (i + 1);
		li.pop_front();
		if (c > r) {
			r = c;
		}
	}
	cout << r;
}
