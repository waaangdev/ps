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

int n,m,qi;
int li[500001];
multiset<int,greater<int>> q;
string rl;
string inp;

int sol() {
    cin >> n >> m;
    cin >> inp;
    for (int i = 0; i < n;i++){
        li[i]=inp[i]-'0';
    }
    for (int i = 0; i < m+1;i++){
        q.insert(li[i]);
    }
    int m2 =m;
    qi = m;
    for (int i = 0; i < n;i++){
        int maxs=*(q.begin());
        //cout << maxs <<" "<<qi<<" "<<m<<" "<<i<<"\n";
        for (int j = 0; j< m+1;j++){
            q.erase(q.find(li[i+j]));
            //cout << "e" << li[i+j] <<" " << q.size()<<"\n";
            if(li[i+j] == maxs){
                if(rl.size() < (n-m2)) rl+=to_string(maxs);
                m-=(j);
                i = i+j;
                break;
            }
        }
        while(qi<i+m+1 and qi != n-1){
            qi+=1;
            //  cout << "i " << li[qi]<<"\n";
            q.insert(li[qi]);
        }
    }
    cout << rl;

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






