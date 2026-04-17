#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
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


//void print(vector<llint> li) {
//	for (int i = 0; i < li.size(); i++) {
//		cout << li[i] << " ";
//	}
//	cout << "\n";
//}

size_t nn;
ullint n,n2,n3;
char strs[50000000];

int sol() {
	n=fread(strs,sizeof(char),50000000-1,stdin);

    
	for (int i = 0; i < 50000000;i++){
		if(strs[i]=='\n'){
            n+=n2; n2 = 0;
            if(n3==0){
                n3=1;
                n=0;
            }
        }
		else if(strs[i]<'0' or strs[i]>'9') break;
		else {n2= (strs[i]-'0')+n2*10;}

	}

	cout << "5000000\n"<<n+n2;
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






