#include <bits/stdc++.h>

using namespace std;

int n;

int main()
{
    cin >> n;
    int* stdents = new int[n];
    int pointer = 0;
    int late_time = 0;


    for (int i = 0; i < n+1; i++) {
        string dum,dum2;
        int time = 0;
        cin >> dum >> dum2;
        time = (dum[0] * 10 + dum[1]) * 60 + (dum[3] * 10 + dum[4]);
        if (dum2 == "student") {
            stdents[i - pointer] = time;
        }
        else {
            pointer = 1;
            late_time = time;
        }
    }
    string dum;
    int time = 0;
    cin >> dum;
    time = (dum[0] * 10 + dum[1]) * 60 + (dum[3] * 10 + dum[4]);
    late_time = max(time, late_time);

    int r = 0;
    for (int i = 0; i < n; i++) {
        if (stdents[i] >= late_time) {
            r += 1;
        }
    }
    cout << r;
}