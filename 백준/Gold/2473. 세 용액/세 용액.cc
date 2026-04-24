#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;

int case_ = 1;


struct llint_pair {
	llint first;
	int second;
};


bool compare(llint_pair i, llint_pair j) {
	return i.first+i.second < j.first+j.second;
}

//struct cmp {
//	bool operator()(llint_pair a, llint_pair b) {
//		return a.first < b.first;
//	}
//};


//void print(vector<llint> li) {
//	for (int i = 0; i < li.size(); i++) {
//		cout << li[i] << " ";
//	}
//	cout << "\n";
//}

llint n;
llint rr=10000000000000;
llint li[5000];
llint rr2[3];

int sol() {
	cin >>n;
    for(int i=0;i<n;i++){
        cin >>li[i];
    }
    sort(li,li+n);
    for(llint i=0;i<n;i++){
        for(llint j2=0;j2<i;j2++){

            llint l= i+1;
            llint r = n;
            while(l+1<r){
                llint mid=(l+r)/2;
                if(li[mid] <= -(li[i]+li[j2])){
                    l=mid;
                }
                else{
                    r=mid;
                }
            }
            for(llint j=max(i+1,l-2);j<min(n,r+2);j++){
                llint d= abs(li[i]+li[j2]+li[j]);
                if(d < rr){
                    rr=d;
                    rr2[0] = li[i];
                    rr2[1] = li[j];
                    rr2[2] = li[j2];
                }
            }

        }
    }
    sort(rr2,rr2+3);
    cout << rr2[0]<<" "<< rr2[1]<<" "<< rr2[2]<<"\n";

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






