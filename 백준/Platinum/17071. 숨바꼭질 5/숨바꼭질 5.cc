#include <iostream>
#include <string>
#include <array>
#include <map>
#include <list>
#include <deque>
#include <cmath>

using namespace std;

array<array<bool,2>, 500001> dp;
array<int, 500001> dp2;
deque<int> q;
int a, b,t,minr;


int main() {
    cin >> a >> b;

    int dum4 = 0;
    while (true) {
        dp2[b + dum4 * (dum4 + 1) / 2] = dum4;
        dum4++;
        if (b + dum4 * (dum4 + 1) / 2 > 500000) {
            break;
        }
    }

    t = 0;
    minr = 10000000;

    dp[a][0] = true;
    q.push_back(a);
    if (dp2[a] != 0 and (dp2[a]) % 2 == 0) {
        minr = dp2[a];
    }

    if (a != b) {
        while (true) {
            t += 1;
            int dum = q.size();
            if (t > minr) break;
            if (dum == 0) break;

            int dum5 = 0;

            for (int i = 0; i < dum; i++) {
                int dum2 = q.front();
                q.pop_front();

                dum5 = dum2 + 1;
                if (dum5 <= 500000 and dum5 >= 0) {
                    if (!dp[dum5][t%2]) {
                        q.push_back(dum5);
                        dp[dum5][t % 2] = true;
                        if (dp2[dum5] >= t and (dp2[dum5] - t)%2 == 0) {
                            minr = (minr > dp2[dum5]) ? dp2[dum5] : minr;
                        }
                    }
                }
                dum5 = dum2 - 1;
                if (dum5 <= 500000 and dum5 >= 0) {
                    if (!dp[dum5][t % 2]) {
                        q.push_back(dum5);
                        dp[dum5][t % 2] = true;
                        if (dp2[dum5] >= t and (dp2[dum5] - t) % 2 == 0) {
                            minr = (minr > dp2[dum5]) ? dp2[dum5] : minr;
                        }
                    }
                }
                dum5 = dum2 + dum2;

                if (dum5 <= 500000 and dum5 >= 0) {
                    if (!dp[dum5][t % 2]) {
                        q.push_back(dum5);
                        dp[dum5][t % 2] = true;
                        if (dp2[dum5] >= t and (dp2[dum5] - t) % 2 == 0) {
                            minr = (minr > dp2[dum5]) ? dp2[dum5] : minr;
                        }
                    }
                }


            }
        }
    }
    else {
        minr = 0;
    }
    if (minr == 10000000) {
        cout << -1;
    }
    else {
        cout << minr;
    }
}