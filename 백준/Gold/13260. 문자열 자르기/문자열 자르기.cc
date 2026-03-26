#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));

int case_ = 1;


struct llint_pair {
    int first;
    int second;
    int idx;
};


bool compare(llint_pair i, llint_pair j) {
    if (i.first == j.first) {
        return i.second < j.second;
    }
    return i.first < j.first;
}

//struct cmp {
//	bool operator()(llint_pair a, llint_pair b) {
//		return a.first < b.first; 큰게 top
//	}
//};


//void print(vector<llint> li) {
//	for (int i = 0; i < li.size(); i++) {
//		cout << li[i] << " ";
//	}
//	cout << "\n";
//}

llint n,m;
llint li[1000];
llint dp[1000][1000];

llint sol2(int l, int r, int sl, int sr) {
    if (l == r) return 0;
    if (dp[l][r] != 0) return dp[l][r];
    int s = sr - sl;

    llint mins = -1;

    for (int i = l; i < r; i++) {
        if (mins == -1) mins = sol2(l, i, sl, li[i]) + sol2(i + 1, r, li[i], sr);
        else mins = min(mins, sol2(l, i, sl, li[i]) + sol2(i + 1, r, li[i], sr));
    }
    dp[l][r] = mins + s;
    return dp[l][r];
}

int sol() {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> li[i];
    }
    sort(li, li + m);

    cout << sol2(0, m, 0, n);
    return 0;
}

int main() {
    // ios_base::sync_with_stdio(false);
    // cin.tie(0);
    // cout.tie(0);

    //cin >> case_;

    for (int i = 0; i < case_; i++) {
        if (sol()) break;
    }

    //while (!sol()) {

    //}


}






