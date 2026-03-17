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

    bool operator<(const llint_pair& a) const{
        if(first == a.first) return second < a.second;
		return first < a.first;
	}
};


int n,a,b;
int tree[300000];
int li[300000][2];
int bang[300000];
deque<int> q;
vector<int> ways[300000];
multiset<llint_pair> sets;

int offq[1200000][3];
int offq2[1200000];
int offqr[1200000];
int qpop;

bool compare(int i, int j) {
	if (li[i][0] == li[j][0]) {
		return li[i][1] < li[j][1];
	}
	return li[i][0] < li[j][0];
}

bool compare2(int i, int j) {
	if (offq[i][0] == offq[j][0]) {
		return offq[i][1] < offq[j][1];
	}
	return offq[i][0] < offq[j][0];
}



void arrayset(int idx, int a,int b,int c){
    offq[idx][0] = a;
    offq[idx][1] = b;
    offq[idx][2] = c;
    offq2[idx] = idx;

}

int sol() {
    cin >> n>>a>>b;
    for(int i = 0;i<n;i++){
        cin >> li[i][0]>>li[i][1];
        bang[i]=0;
        tree[i]=i;
        ways[i].clear();
        //unionfind[i]=i;
    }
    sort(tree,tree+n,compare);

    for(int i = 0;i<n;i++){
        if(li[tree[i]][1] <= b){
            q.push_back(tree[i]);
            bang[tree[i]]=1;
        }
    }

    for(int i = 0;i<n;i++){
        qpop = tree[i];

        arrayset(i*4+0,li[qpop][0]-a,li[qpop][0],li[qpop][1]+b);
        arrayset(i*4+1,li[qpop][0],li[qpop][0]+a,li[qpop][1]+b);
        arrayset(i*4+2,li[qpop][0]-a,li[qpop][0],li[qpop][1]);
        arrayset(i*4+3,li[qpop][0],li[qpop][0]+a,li[qpop][1]);

    }
    sort(offq2,offq2+(n*4),compare2);

    int l = 0;
    int r = 1;
    sets.clear();
    sets.insert((const llint_pair) {li[tree[l]][1],tree[0]});
    for(int i = 0;i<n*4;i++){
        
        if(r !=n){
            while(li[tree[r]][0] <= offq[offq2[i]][1]){
                sets.insert((const llint_pair){li[tree[r]][1],tree[r]});
                //cout <<"insert "<< tree[r] << "\n";
                r+=1;
                if(r==n) break;
            }
        }

        while(li[tree[l]][0] < offq[offq2[i]][0]){
            sets.erase((const llint_pair){li[tree[l]][1],tree[l]});
            //cout <<"erase "<< tree[l] << "\n";
            l+=1;
        }
        //cout<<tree[offq2[i]/4]<<":" <<  offq[offq2[i]][0]<<" "<< offq[offq2[i]][1]<<' '<< offq[offq2[i]][2]<<" - ";

        //int dum = bsearch(l,r,offq[offq2[i]][2],1, tree, 1)-1;

        offqr[offq2[i]] = -1;
        if(!sets.empty()){
            auto dum = sets.lower_bound((const llint_pair){offq[offq2[i]][2],100000000});
            if(dum==sets.end()) dum--;
            //cout <<" ("<<sets.size()<<") ";
            if((*dum).first > offq[offq2[i]][2]){
                if(dum != sets.begin()){
                    dum--;
                }
            }


            if((*dum).second == tree[offq2[i]/4]){
                if(dum != sets.begin()){
                    //cout <<"asd";
                    dum--;
                }
            }

            if(li[(*dum).second][1] <= offq[offq2[i]][2]){
                offqr[offq2[i]] = (*dum).second;
            }

            //cout <<offqr[offq2[i]]<<"\n";
        }
    }

    for(int i = 0;i<n;i++){
        qpop = tree[i];
        for(int j = 0;j<4;j++){
            if(offqr[i*4+j] !=-1){
                ways[qpop].push_back(offqr[i*4+j]);
                //cout << qpop <<" -> "<<offqr[i*4+j]<<"\n";
            }
        }

    }



    //cout << "3 ok\n";


    while(!q.empty()){
        qpop = q.front();
        q.pop_front();

        for (auto i = ways[qpop].begin();i!=ways[qpop].end();i++){
            if(bang[*i]==0){
                q.push_back(*i);
                bang[*i]=1;
            }
        }
    }
    // for(int i = 0; i < n;i++){
    //     cout << bang[tree[i]]<<" ";
    // }
    // cout <<"\n";



    if(bang[n-1]){
        cout << "YES\n";
    }
    else{
        cout << "NO\n";
    }


	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);


	cin >> case_;

	for (int i = 0; i < case_; i++) {
		if (sol()) break;
	}

	//while (!sol()) {

	//}


}






