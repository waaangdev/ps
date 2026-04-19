#include <iostream>
#include <string>
#include <array>
#include <map>
#include <list>
#include <deque>
#include <cmath>

using namespace std;

int a,r;

int factorial_dp[50];
int r_dp[13][50];

int factorial(int num) {
    if (num <= 1) {
        return 1;
    }

    if (factorial_dp[num] == 0) {
        factorial_dp[num] = factorial(num - 1) * num %10007 + 1;
    }
    return factorial_dp[num]-1;
}

int nm(int m, int n) {
    unsigned long long int dam = 1;
    for (int i = 0; i < n; i++)
    {
        dam *= m - i;
        dam /= 1 + i;
    }
    return dam%10007;
}

int dp(int cardsize, int drowsu) {  // cardsize>drowsu  cardsize/4는 정수
    if (drowsu < 4) {
        return 0;
    }

    int rr = r_dp[cardsize][drowsu];

    if (rr != 0) {
        return rr;
    }

    for (int i = cardsize-1; i > -1; i--) {
        long long int r1 = 0;
        int dum = ((cardsize - i - 1) * 4);
        int dum2 = (i * 3);
        int dum3 = (i * 4);
        for (int j = 0; j < drowsu - 4+1; j++) {
            int j2 = (drowsu - 4) - j;
            if (j <= dum and j2 <= dum2) {
                long long int r2 = 1;
                if (j != 0) {
                    r2 = 0;
                    r2 += nm(dum, j);
                    //r2 += factorial(dum) / (factorial(dum - j) * factorial(j));// % 10007;
                }

                long long int r3 = 1;
                if (j2 != 0) {
                    r3 = 0;
                    r3 += nm(dum3, j2);
                    //r3 += factorial(dum3) / (factorial(dum3 - j2) * factorial(j2)); // % 10007;
                    r3 += 10007;
                    r3 -= dp(i, j2);
                    r3 %= 10007;
                }
                r1 += r2 * r3;
            }

        }
        rr += r1 % 10007;
    }
    r_dp[cardsize][drowsu] = rr % 10007;
    return rr % 10007;
}


int main() {
    cin >> a;
    //cout << nm(48, 13);
    cout << dp(13, a);
}