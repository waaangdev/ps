#include "monkey.h"
#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int n,m;
long long int bananas[500000];
int P2[500000];
pair<int, int> gP[500000];
pair<int, int> gP2[500000];
int nidxl[500000][2];

bool compare(int i2, int j2) {
    pair<int, int> i = gP[i2];
    pair<int, int> j = gP[j2];
	if (i.second == j.second) {
		return i.first < j.first;
 	}
 	return i.second < j.second;
}
bool compare2(int i2, int j2) {
    pair<int, int> i = gP[i2];
    pair<int, int> j = gP[j2];
	if (i.first == j.first) {
		return i.second < j.second;
 	}
 	return i.first < j.first;
}


long long int sol(int idx){
    if(bananas[idx]==-1){
        bananas[idx] = gP2[idx].first+gP2[idx].second;
        if(nidxl[idx][0]!=-1){
            bananas[idx]= max(sol(nidxl[idx][0]) + gP2[idx].second,bananas[idx]);
        }
        if(nidxl[idx][1]!=-1){
            bananas[idx]= max(bananas[idx],sol(nidxl[idx][1]) + gP2[idx].first);
        }
    }
    return bananas[idx];
}


long long max_bananas(std::vector<int> A, std::vector<int> B,std::vector<std::pair<int, int> > P) {
    n = A.size();
    m = P.size();

    for (int i = 0;i < m;i++){
        bananas[i] = -1;
        P2[i]=i;
        gP[i].first = P[i].first;
        gP[i].second = P[i].second;
        gP2[i].first = A[P[i].first-1];
        gP2[i].second = B[P[i].second-1];
        nidxl[i][0]=-1;
        nidxl[i][1]=-1;
    }

    
    sort(P2,P2+m,compare2);
    for (int j = 0;j < m-1;j++){
        if (P[P2[j]].first ==P[P2[j+1]].first){
            nidxl[P2[j]][0] = P2[j+1];
        }
    }
    sort(P2,P2+m,compare);
    for (int j = 0;j < m-1;j++){
        if (P[P2[j]].second ==P[P2[j+1]].second){
            nidxl[P2[j]][1] = P2[j+1];
        }
    }



    long long int rr = 0;
    for (int i = 0;i < m;i++){
        rr = max(rr,sol(i));
    }
    return rr;

}
