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

 

long long int base, length, r,r2;

vector<int> basecount(10);

string num;

 

long long int mn(int m, int n) { //m개 중에서 n개를 고르는 경우의 수

    long long dum = 1;

    for (int i = 0; i < n; i++) {

        dum *= m - i;

        dum /= 1 + i;

    }

    return dum;

}

 

void result() {

    int dum = r2;

    for (int i = length - 1; i > -1; i--) {

        int dum2 = 0;

        int dum3 = 0;

        for (int j = 0; j < base; j++) {

            if (j < num[i] - '0') {

                dum3 += basecount[j];

            }

            dum2 += basecount[j];

        }

        r += dum * dum3 / dum2;

        dum = dum * basecount[(num[i] - '0')] / dum2;

        basecount[(num[i] - '0')] -= 1;

    }

 

}

 

signed main()

{

    cin >> length >> num;
base =2;
 

    for (int j = 0; j < length; j++) {

        basecount[(num[j] - '0')] += 1;

    }

 

    r = 0;

    int dum = 0;

    

    for (int i = base - 1; i > -1; i--) {

        int dum4 = 0;

        int dum3 = 1;

        for (int k = base-1; k > i; k--) {

            dum3 *= mn(length - dum4, basecount[k]) / mn(basecount[k], basecount[k]);

            dum4 += basecount[k];

        }

        if (i==0) {

            r2 = dum3;

            break;

        }

 

        for (int j = 0; j < basecount[i]; j++) {

            r += dum3 * mn(length - dum4, j) / mn(j, j) * pow(i, length - (dum + j));

        }

        dum += basecount[i];

    }

 

    result();

 

    cout << r << "\n";

 

}