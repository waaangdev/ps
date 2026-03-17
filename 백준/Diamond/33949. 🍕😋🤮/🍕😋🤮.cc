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
	int third;
};


//bool compare(llint_pair i, llint_pair j) {
//	if (i.first == j.first) {
//		return i.second < j.second;
//	}
//	return i.first < j.first;
//}

//struct cmp {
//	bool operator()(llint_pair a, llint_pair b) {
//		return a.first < b.first; 큰게 top
//	}
//};


// void print(vector<llint> li) {
// 	for (int i = 0; i < li.size(); i++) {
// 		cout << li[i] << " ";
// 	}
// 	cout << "\n";
// }

int n,m;
llint tree[524288][7]; //좌우중간 좌우중간 전체
multiset<llint> li;

void merge(llint* left, llint* right, llint* updated){
    updated[0] = max(left[0],left[6]+right[0]);
    updated[1] = max(right[1],right[6]+left[1]);
    updated[2] = max(max(right[2],left[2]),left[1]+right[0]);
    
    updated[3] = min(left[3],left[6]+right[3]);
    updated[4] = min(right[4],right[6]+left[4]);
    updated[5] = min(min(right[5],left[5]),left[4]+right[3]);

    updated[6] = left[6]+right[6];

}

void update(int idx){
    int n2 = n;
    for (int i = 1; i < 19;i++){
        //cout << i-1 <<" "<< idx<<" "<<n2<<" "<<tree[(1<<(17-i+1))+(idx)][6]<<"\n";
        idx= (idx>>1);
        
        if((idx<<1)+1 == n2){
            for (int j = 0; j<7;j++){
                tree[(1<<(18-i))+idx][j]=tree[(1<<(18-i+1))+(idx<<1)][j];
            }
            //cout <<tree[(1<<(17-i))+idx][6] <<" " <<tree[(1<<(17-i+1))+(idx<<1)][6]<<"\n";
        }
        else{

            merge(tree[(1<<(18-i+1))+(idx<<1)],tree[(1<<(18-i+1))+(idx<<1)+1],tree[(1<<(18-i))+idx]);
        }
        // for (int j = 0; j<7;j++){
        //     cout << idx;
        // }
        // cout << "\n";
        
        n2=(n2>>1)+(n2%2);
    }
}

int sol() {
    cin >> n>>m;
    for (int i =0;i<n;i++){
        li.insert(0);
    }
    for(int i = 0;i<m;i++){
        int mode;
        cin >> mode;
        if(mode == 1){
            int idx,num;
            cin >> idx>>num;
            li.erase(li.find(tree[(1<<18)+idx-1][0]));
            for (int j = 0; j<7;j++){
                tree[(1<<18)+idx-1][j]+=num;
            }
            li.insert(tree[(1<<18)+idx-1][0]);
            update(idx-1);
        }
        else{
            
            if((*li.rbegin()) < 0){
                cout << (*li.rbegin()) << "\n";
            }
            else{
                cout << max(tree[1][2],tree[1][6]-tree[1][5])<<"\n";
            }
        }
    }

	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//cin >> case_;

	for (int i = 0; i < case_; i++) {
		if (sol()) break;
	}

	//while (!sol()) {

	//}


}






