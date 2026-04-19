#include <iostream>
#include <string>
#include <array>
#include <map>
#include <list>
#include <deque>
#include <cmath>
#include <set>
#include <vector>
#include <algorithm>
#include <fstream>
#include <iterator>
#include <fstream>

using namespace std;

int n;
deque<pair<int, int>> li1;
deque<pair<int, int>> li2;

bool sorting(pair<int, int> a, pair<int, int> b) {
    return a.second < b.second;
}

int main()
{
    cin >> n;
    for (int i = 0; i < n; i++) {
        int dum1,dum2,dum3;
        cin >> dum1 >> dum2 >> dum3;
        li1.push_back(make_pair(dum1, dum2));
        li2.push_back(make_pair(dum1, dum3));
    }

    sort(li1.begin(), li1.end(),sorting);
    sort(li2.begin(), li2.end(), sorting);

    int r = 0;
    int r2 = 0;
    while (not li2.empty()) {
        if (li1.empty() or li2.front().second <= li1.front().second) {
            r2 -= 1;
            li2.pop_front();
        }
        else {
            r2 += 1;
            r = max(r2, r);
            li1.pop_front();
        }
    }

    cout << r;

}