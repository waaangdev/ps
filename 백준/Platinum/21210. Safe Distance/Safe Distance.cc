#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <iostream>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;

int case_ = 1;


struct llint_pair {
	long double first;
	int second;
	int third;
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

int k,w,h;
long double li[1000][2];
int par[1004],upd[1004];
vector<llint_pair> diss;

int getpar(int a){
    if(par[a]!=a) par[a]=getpar(par[a]);
    return par[a];
}
int unions(int a,int b){
    a=getpar(a);
    b=getpar(b);
    if(a > b) swap(a,b);

    if(upd[a] and upd[b]){
        if(upd[a]!=upd[b]){
            return 1;
        }
    }
    else{
        upd[a]=max(upd[a],upd[b]);
    }
    par[b]=a;
    return 0;
}

int sol() {
    cin >>w>>h;
    cin >>k;
    for(int i = 0;i<k;i++){
        cin >> li[i][0]>> li[i][1];
    }
    diss.clear();

    for(int i = 0;i<k;i++){
        diss.push_back({(long double)(li[i][0]),i,k});
        diss.push_back({(long double)(w-li[i][0]),i,k+1});
        diss.push_back({(long double)(li[i][1]),i,k+2});
        diss.push_back({(long double)(h-li[i][1]),i,k+3});
        for(int j = 0;j<k;j++){
            diss.push_back({(long double)(sqrtl(powl(li[i][0]-li[j][0],2)+powl(li[i][1]-li[j][1],2)))/(long double)(2),i,j});
        }
    }
    for(int i = 0;i<k+4;i++){
        par[i]=i;
        upd[i]=0;
    }
    upd[k]=1;
    upd[k+1]=2;
    upd[k+2]=2;
    upd[k+3]=1;

    sort(diss.begin(),diss.end(),compare);

    for (int i = 0;i<diss.size();i++){
        if(unions(diss[i].second,diss[i].third)){
            if(diss[i].first<=0){
                printf("0\n");
            }
            else{
                printf("%.6f\n",(double)((diss[i].first)));
            }
            break;
        }
    }

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






