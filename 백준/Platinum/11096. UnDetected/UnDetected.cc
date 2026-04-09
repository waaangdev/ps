#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;

#define swap(a,b,t) ((t=a),(a=b),(b=t))
#define ipow2(a) ((a)*(a))

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


//void print(vector<llint> li) {
//	for (int i = 0; i < li.size(); i++) {
//		cout << li[i] << " ";
//	}
//	cout << "\n";
//}

int n;
int li[200][5];//x,y,r,p,lr

int find(int idx){
    if(li[idx][3]==idx){
        return idx;
    }
    li[idx][3]=find(li[idx][3]);
    return li[idx][3];
}
bool unions(int idx1,int idx2){
    int tmp;
    idx1 = find(idx1);
    idx2 = find(idx2);

    if(idx1 > idx2) swap(idx1,idx2,tmp);

    li[idx1][4]|=li[idx2][4];
    li[idx2][3]=idx1;

    return ( li[idx1][4]==3);
}

int sol() {
	cin >>n;
    for(int i = 0;i < n;i++){
        li[i][3]=i;
    }
    for(int i = 0;i < n;i++){
        cin >> li[i][0]>> li[i][1]>> li[i][2];

        if(li[i][0] < li[i][2]){
            li[i][4]|=1;
        }
        if(200- li[i][0] < li[i][2]){
            li[i][4]|=2;
        }
        if(li[i][4]==3){
            cout << i<<"\n";
            break;
        }

        for(int j = 0;j < i;j++){
            if(ipow2(li[i][0]-li[j][0])+ipow2(li[i][1]-li[j][1]) < ipow2(li[i][2]+li[j][2])){
                if(unions(i,j)){
                    cout << i<<"\n";
                    return 0;
                }
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






