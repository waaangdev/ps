//벽

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

#define swap(a,b,t) ((t=a),(a=b),(b=t));
#define max2(a,b) (a=max(a,b));
#define min2(a,b) (a=min(a,b));

int case_;

struct node {
    int max_;
    int min_;
    bool updated;
};

node tree[5000022];
int ili[22];
int ili2[22];

node nodeMerge(node a,node b) {
    return { max(a.max_,b.max_),min(a.min_,b.min_) };
}


void treeSet(int l, int r,int i,int j,int num,int height,int mode) {
    if (i != 0) {
        for (int i2 = 0; i2 < 1 + 1 * (ili2[i - 1] > ((j << 1) + 1)); i2++) {
            max2(tree[ili[i - 1] + (j << 1) + i2].min_, tree[ili[i] + j].min_);
            max2(tree[ili[i - 1] + (j << 1) + i2].max_, tree[ili[i] + j].min_);
            min2(tree[ili[i - 1] + (j << 1) + i2].min_, tree[ili[i] + j].max_);
            min2(tree[ili[i - 1] + (j << 1) + i2].max_, tree[ili[i] + j].max_);
        }
    }


    if (l == j * num and r == l + num) {
        if (mode == 1) {
            max2(tree[ili[i] + j].max_, height);
            max2(tree[ili[i] + j].min_, height);
        }
        else {
            min2(tree[ili[i] + j].max_, height);
            min2(tree[ili[i] + j].min_, height);
        }
        //cout << i << " " << j << "(" << tree[ili[i] + j].min_ << "," << tree[ili[i] + j].max_ << ")(" << ili[i] + j << ") set\n";
        return;
    }
    int dum = j * num + (num >>1);
    if (l < dum and r <= dum) {
        treeSet(l, r, i - 1, (j << 1), num >> 1, height ,mode);
    }
    else if (l >= dum and r > dum) {
        treeSet(l, r, i - 1, (j << 1) +1, num >> 1, height, mode);
    }
    else {
        treeSet(l, dum, i - 1, (j << 1), num >> 1, height, mode);
        treeSet(dum, r, i - 1, (j << 1) + 1, num >> 1, height, mode);
    }
    if (i != 0) {
        if (ili[i - 1] + (j << 1) + 1 == ili[i]) {
            tree[ili[i] + j] = tree[ili[i - 1] + (j << 1) + 0];
            //cout << i << " " << j << "(" << tree[ili[i] + j].min_ << "," << tree[ili[i] + j].max_ << ")(" << ili[i] + j << ") end\n";
        }
        else {
            tree[ili[i] + j] = nodeMerge(tree[ili[i - 1] + (j << 1) + 0], tree[ili[i - 1] + (j << 1) + 1]);
            //cout << i << " " << j << "(" << tree[ili[i] + j].min_ << "," << tree[ili[i] + j].max_ <<")(" << ili[i] + j << ") not\n";
        }
    }

    //cout << tree[15].max_ << "\n";
}


void sol() {
    int n, m;
    cin >> n>>m;

    int dum =n;
    int dum2 = 0;
    for (int i = 0; i < 22; i++) {
        ili[i] = dum2;
        ili2[i] = dum;
        dum2 += dum;
        dum = dum / 2 + dum % 2;
    }


    int inp[4];
    for (int i = 0; i < m; i++) {
        cin >> inp[0] >> inp[1] >> inp[2] >> inp[3];
        treeSet(inp[1], inp[2] + 1, 21, 0, 1 << 21, inp[3], inp[0]);
        //cout << tree[15].max_ << "\n";

    //cout << tree[ili[21]].min_ << " "<< tree[ili[21]].max_ << "\n";
    }
    for (int i = 21; i > 0; i--) {
        for (int j = 0; j < ili2[i]; j++) {
            //cout << j << "("<< tree[ili[i] + j].min_<<","<< tree[ili[i] + j].max_<<")("<< ili[i] + j << ") ";
            for (int i2 = 0; i2 < 1+1*(ili2[i-1] > ((j << 1) + 1)); i2++) {
                max2(tree[ili[i - 1] + (j << 1) + i2].min_, tree[ili[i] + j].min_);
                max2(tree[ili[i - 1] + (j << 1) + i2].max_, tree[ili[i] + j].min_);
                min2(tree[ili[i - 1] + (j << 1) + i2].min_, tree[ili[i] + j].max_);
                min2(tree[ili[i - 1] + (j << 1) + i2].max_, tree[ili[i] + j].max_);
            }
        }
        //cout << "\n";
    }
    //}


    for (int i = 0; i < n; i++) {
        //int r = 0;
        //dum = i;
        //for (int j = 0; j < 22; j++) {
        //    r = max(r, tree[ili[j] + dum].min_);
        //    r = min(r, tree[ili[j] + dum].max_);
        //    dum = dum>>1;
        //}
        //cout << r << "\n";
        cout << tree[i].min_ << "\n";
    }
    //cout << "\n";

    
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