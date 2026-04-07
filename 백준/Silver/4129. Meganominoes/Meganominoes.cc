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


//void print(vector<llint> li) {
//	for (int i = 0; i < li.size(); i++) {
//		cout << li[i] << " ";
//	}
//	cout << "\n";
//}

llint n,m;
llint li[10000][2];
multiset<llint> sets;

int sol() {
	cin >> n>>m;
	for (int i = 0;i<n;i++){
		cin >>li[i][0]>>li[i][1];
	}
	for (int i = 0;i<n;i++){
		for (int j = 0;j<n;j++){
			if(i!=j){
				if(li[i][1] == li[j][0]){
					sets.insert(li[i][0]+li[j][1]);
				}
				
			}
		}
	}	
	for (int i = 0;i<n;i++){
		for (int j = i+1;j<n;j++){
            if(li[i][1] == li[j][1]){
					sets.insert(li[i][0]+li[j][0]);
				}
            if(li[i][0] == li[j][0]){
					sets.insert(li[i][1]+li[j][1]);
				}
        }
    }
	for (int i = 0;i<m;i++){
		llint dum;
		cin >> dum;
		cout << sets.count(dum) << '\n';
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






