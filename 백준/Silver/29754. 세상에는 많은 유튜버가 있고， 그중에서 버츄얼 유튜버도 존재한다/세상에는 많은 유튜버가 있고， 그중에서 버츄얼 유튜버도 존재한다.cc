#include <iostream>
#include <string>
#include <array>
#include <map>
#include <list>

using namespace std;
int a, b,date,st,et,poi,dum,dum2,dum3;
string name,t1,t2;
map<string, array<pair<int,array<bool,7>>, 52>> vtuber;
list<string> vtuber_name;

int main() {
	cin >> a >> b;
	poi = 0;
	for (int i = 0; i < a; i++) {
		cin >> name >> date>>t1>>t2;
		st = stoi(t1.substr(0, 2))*60+ stoi(t1.substr(3, 2));
		et = stoi(t2.substr(0, 2)) * 60 + stoi(t2.substr(3, 2));
		date -= 1;
		if (vtuber.find(name) == vtuber.end()) {
			vtuber_name.push_back(name);
		}
		vtuber[name][date / 7].first += et-st;
		vtuber[name][date / 7].second[date % 7] = true;
	}
	vtuber_name.sort();
	dum3 = 1;
	for (int i = 0; i < vtuber.size(); i++) {
		name = vtuber_name.front();
		vtuber_name.pop_front();
		dum = 1;
		for (int j = 0; j < b/7; j++) {
			if (vtuber[name][j].first < 60*60) {
				//cout << name << "br1 " << vtuber[name][j].first << "\n";
				dum = 0;
				break;
			}
			dum2 = 0;
			for (int k = 0; k < 7; k++) {
				if (vtuber[name][j].second[k]) {
					dum2 += 1;
				}
				
			}
			if (dum2 < 5) {
				//cout << name << "br2\n";
				dum = 0;
				break;
			}
		}
		if (dum) {
			cout << name << "\n";
			dum3 = 0;
		}

	}
	if (dum3) {
		cout << "-1\n";
	}
}

