//히스토그램에서 가장 큰 직사각형

#include <bits/stdc++.h>
#include <sstream>

using namespace std;

typedef long long int llint;

vector<pair<llint, llint>> li(0);

int main(){
	
	while (1) {
		string inp;
		getline(cin, inp);
		if (inp == "0") break;

		stringstream ss(inp);


		string inp2;
		llint r = 0;
		int i = 0;
		ss >> inp2;
		while (ss >> inp2) {
			int num = stoi(inp2);
			//cout << num << "\n";

			//for (int j = 0; j < li.size(); j++) {
			//	cout << "[" << li[j].first << "," << li[j].second << "]" << ",";
			//}
			//cout << "\n";
			pair<llint, llint> dum;
			llint dum2 = i;
			while (!li.empty()) {
				dum = li.back();
				if (dum.first <= num) {
					break;
				}
				r = max(r, dum.first * (i - dum.second));
				dum2 = min(dum.second, dum2);
				li.pop_back();
			}
			if (dum.first != num) {
				li.push_back(make_pair(num, dum2));
			}
			i += 1;
		}

		while (!li.empty()) {
			pair<llint, llint> dum = li.back();
			r = max(r, dum.first * (i - dum.second));
			li.pop_back();
		}
		cout << r << "\n";
	}

}
