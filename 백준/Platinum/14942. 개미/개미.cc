//개미

#include <array>
#include <iostream>
#include <string>
#include <deque>
using namespace std;

int poisu;
int duma, dumb, dumc;
int qpop;
array<int,100000> anthp;
array<deque<pair<int,int>>, 100000> way;
array<pair<int, int>, 100000> bang;
array<bool, 100000> bang2;
deque<int>q;

int main() {
	cin >> poisu;
	for (int i = 0; i < poisu; i++) {
		cin >> anthp[i];
	}
	for (int i = 0; i < poisu-1; i++) {
		cin >> duma >> dumb >> dumc;
		way[duma-1].push_front(make_pair(dumb-1,dumc));
		way[dumb-1].push_front(make_pair(duma-1, dumc));
	}
	q.push_back(0);
	bang2[0] = true;
	while (!q.empty()) {
		qpop = q.front();
		q.pop_front();
		for (int i = 0; i < way[qpop].size(); i++) {
			duma = way[qpop].front().first;
			dumb = way[qpop].front().second;
			way[qpop].pop_front();
			if (!bang2[duma]) {
				bang[duma] = make_pair(qpop, dumb);
				q.push_back(duma);
				bang2[duma] = true;
			}
			way[qpop].push_back(make_pair(duma, dumb));
		}
	}
	for (int i = 0; i < poisu; i++) {
		duma = i;
		dumb = anthp[i];
		while (duma != 0 && dumb > 0) {
			dumb -= bang[duma].second;
			//cout << bang[duma].second;
			if (dumb < 0) {
				break;
			}
			duma = bang[duma].first; 
		}
		cout << duma + 1<<"\n";
		
	}
}