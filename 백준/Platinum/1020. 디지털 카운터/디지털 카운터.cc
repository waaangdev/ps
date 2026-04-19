//디지털 카운터

//디지털 카운터

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));

int case_;

char inpli[16];
int leninp;
int inpsum;
int choi[10] = { 6, 2, 5, 5, 4, 5, 6, 3, 7, 5 };
bool colnum[10] = { 0, 0, 0, 1, 0, 1, 1, 0, 0, 1 };

array<char, 16> dp_lower[106][15][2];
bool dp_lower2[106][15][2];
array<char, 16> dp_upper[106][15][2];
bool dp_upper2[106][15][2];

array<char, 16> DigitDP_lower(int sum, int idx, bool fit) {
    //cout << sum << ' ' << idx << ' ' << fit << '\n';
    array<char, 16> r = { 0, };

    if (dp_lower2[sum][idx][(fit) ? 1 : 0]) {
        return dp_lower[sum][idx][(fit) ? 1 : 0];
    }
    if (idx == leninp or sum >= inpsum) {
        if (sum == inpsum and !fit and idx == leninp) {
            r[idx] = 1;
        }

        return r;
    }

    bool rb = false;
    int rnum = 0;
    int i = 0;
    if (fit)i = inpli[idx];
    for (; i < 10; i++) {
        if (!fit and colnum[i]) continue;
        r = DigitDP_lower(sum + choi[i], idx + 1, (fit and i == inpli[idx]));
        if (r[idx+1] != 0) {
            rb = true;
            rnum = i;
            break;
        }
    }
    if (rb) r[idx] = rnum + 2;
    dp_lower[sum][idx][(fit) ? 1 : 0] = r;
    dp_lower2[sum][idx][(fit) ? 1 : 0] = true;
    return r;
}

array<char, 16> DigitDP_upper(int sum, int idx, bool fit) {
    //cout << sum << ' ' << idx << ' ' << fit << '\n';
    array<char, 16> r = { 0, };

    if (dp_upper2[sum][idx][(fit) ? 1 : 0]) {
        return dp_upper[sum][idx][(fit) ? 1 : 0];
    }
    if (idx == leninp or sum >= inpsum) {
        if (sum == inpsum and idx == leninp) {
            r[idx] = 1;
        }
        return r;
    }

    bool rb = false;
    int rnum = 0;
    int imax = 9;
    if (fit)imax = inpli[idx];
    for (int i = 0; i <= imax; i++) {
        if (!fit and colnum[i]) continue;
        r = DigitDP_upper(sum + choi[i], idx + 1, (fit and i == imax));
        if (r[idx + 1] != 0) {
            rb = true;
            rnum = i;
            break;
        }
    }
    if (rb) r[idx] = rnum + 2;
    dp_upper[sum][idx][(fit) ? 1 : 0] = r;
    dp_upper2[sum][idx][(fit) ? 1 : 0] = true;
    return r;
}



void sol() {
    cin >> inpli;
    for (int i = 0; i < 15; i++) {
        if (inpli[i] == '\0') break;
        inpli[i] -= '0';
        inpsum += choi[inpli[i]];
        leninp += 1;
    }
    //cout << leninp <<"\n";

    array<char, 16> r = DigitDP_lower(0, 0, true);
    array<char, 16> rr;
    bool lowup = false;
    if (r[0] == 0) {
        lowup = true;
        r = DigitDP_upper(0, 0, true);
    }


    for (int i = 0; i < leninp; i++) {
        r[i] = (r[i] - 2);
        //cout << (char)(r[i] + '0');
    }
    //cout << "\n";
    int dum = 0;
    for (int i = 0; i < 16; i++) {
        rr[i] = 0;
    }

    if (lowup) {
        for (int i = leninp - 1; i > -1; i--) {
            rr[16-leninp+i] = (9 - inpli[i]);
        }

        rr[15] += 1;
        for (int i = leninp - 1; i > -1; i--) {

            //for (int i = 0; i < 16; i++) {
            //    cout << (int)rr[i];
            //}
            //cout << "\n";

            int rri = 16 - leninp + i;

            rr[rri] += dum;
            dum = 0;

            rr[rri] += r[i];
            if (rr[rri] >= 10) {
                dum = 1;
                rr[rri] -= 10;
            }
        }
        if (dum) {
            rr[16 - leninp-1] = 1;
        }
    }
    else {
        for (int i = leninp - 1; i > -1; i--) {
            int rri = 16 - leninp + i;
            r[i] -= dum;
            dum = 0;
            if (inpli[i] > r[i]) {
                dum = 1;
                rr[rri] = (10 + r[i]) - inpli[i];
            }
            else {
                rr[rri] = (r[i]) - inpli[i];
            }
        }
    }
    dum = 0;
    for (int i = 0; i < 16; i++) {
        if (dum or rr[i] != 0) {
            dum = 1;
            cout << (int)rr[i];
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    //cin >> case_;
    case_ = 1;
    for (int c = 0; c < case_; c++) {
        sol();
    }
}