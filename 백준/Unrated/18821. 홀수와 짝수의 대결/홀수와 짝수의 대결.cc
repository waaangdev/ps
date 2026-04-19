#include <iostream>
#include <string>
#include <set>
using namespace std;

using ll = long long;


ll a = 0;
ll b = 0;
string st = "37E1O13E3O3E1O1201E1O59E3007O3E19O1E3O149E5O1E5O1E19O1E1O1E1O1E31O1E3O1E7O1E19O1E7O17E3O1E1O1E1O1E1O1E1O1E1O13E1O3E3O13E19O3E25409O3E1O1E1O1E1O3E1O3E1O1E15O127E1O1E5O9E3O17E1O12143E149O19E1O37E1O1E1O59E5O1E7O5E1O243E1O5E11O1E1O1E55O1E115O1E45O1E9O1E1O1E1453O1E1O13E3O1E1O17E11O1E119O1E9O41E1O1E145O1E1O687E3O1E19O1E1O3E1O1E29O7E1O3E1O15E5O3E1O1E1O9E7O12613E1O1E17O1E309O23E3O1E1O1E1O153E3O1E5O3E1O1E3O1E1O29E11O1E1O268417E33O77E55O1E1O1E1O29E1O1E1O3E23O3E1O1E1O1E1O8703E165O1E1O1E9O1E1O1E1O11E11O11E1O1E53O5E3O57E1O27E3O59E1O1E3O1E1O1E1O5E7O1E1O15E83O1E1O3E1O1E1O1E1O9E1O1E53O1E1O1E1O1E7O17E645O1E3O1E11O25E1O19E1O7E1O1E3O1E1O1E13O3E1O39E1O1E9O";
set<int> li;

int main() {
    int poi = 0;
    int poi3 = 0;
    string poi2 = "";
    int dum = 0;
    for (int j = 0; j < st.size(); j++) {
        if (st[poi] == 'E' or st[poi] == 'O') {
            dum = stoi(poi2);
            for (int i = 0; i < dum; i++) {
                if (st[poi] == 'E') {
                    li.insert(poi3 + i+ 906150257);
                }

            }
            poi3 += dum;
            poi2 = "";
        }
        else {
            poi2 += st[poi];
        }
        poi += 1;
    }
    for (int i = 0; i < dum; i++) {
        li.insert(poi3 + i + 906150257);

    }
    string st = "";
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> a;
    for (int i = 0; i < a; i++) {
        cin >> b;
        if (b > 1) {
            if (b >= 906150257 && b <= 906488079) {
                if (li.find(b) != li.end()) {
                    cout << "E\n";
                }
                else {
                    cout << "O\n";
                }
            }
            else {
                cout << "O\n";
            }
        }
        else {
            cout << "E\n";
        }
    }
}
