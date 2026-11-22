#define _USE_MATH_DEFINES
#include <bits/stdc++.h>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;

int _case = 1;
int _caseidx = 0;

struct int_pair {
	int first;
	int second;
};

//bool compare(int_pair i, int_pair j) {
//	if (i.first == j.first) {
//		return i.second < j.second;
//	}
//	return i.first < j.first;
//}

//struct cmp {
//	bool operator()(int_pair a, int_pair b) {
//		return a.first < b.first; 큰게 top
//	}
//};
//priority_queue<int_pair, vector<int_pair>, cmp> pq;

//void print(vector<llint> li) {
//	for (int i = 0; i < li.size(); i++) {
//		cout << li[i] << " ";
//	}
//	cout << "\n";
//}

int n,rr,ln,rn,lc,rc;
vector<pair<int,pair<int,int>>> li;
pair<int,int> li2[300000];

set<pair<int,int>> sets;
vector<pair<int,int>> sets2[300000];

bool isit(int x){
    auto p1 = sets.upper_bound({x,n+1});
    if(sets.size() != 0){
        if(p1 != sets.begin()){
            p1--;
            if(x <= li[(*p1).second].first+(rc-li[(*p1).second].second.second)){
                return false;
            }
        }
        auto p2 = sets.lower_bound({x,-1});
        if(p2 != sets.end()){
            if(x >= li[(*p2).second].first-(lc-li[(*p2).second].second.first)){
                return false;
            }
        }
    }
    return true;
}

void cset(int x,int idx){
    auto p1 = sets.upper_bound({x,n+1});
    if(sets.size() != 0){
        if(p1 != sets.begin()){
            p1--;
            int dum = x - (li[(*p1).second].first+(rc-li[(*p1).second].second.second));
            if(dum+lc+rc < 300000)sets2[dum+lc+rc].push_back({(*p1).second,idx});
            //cout << " "<< dum+lc+rc;
        }
        auto p2 = sets.lower_bound({x,-1});
        if(p2 != sets.end()){
            int dum = (li[(*p2).second].first-(lc-li[(*p2).second].second.first))-x;
            if(dum+lc+rc < 300000)sets2[dum+lc+rc].push_back({idx,(*p2).second});
            //cout << " "<< dum+lc+rc;
        }
    }
}


int sol() {
    cin >> n;

    li.push_back({0,{lc,rc}});
    cset(0,li.size()-1);
    sets.insert({0,li.size()-1});
    li2[li.size()-1]={1,1};
    ln+=1;
    rn+=1;
    rr+=1;

    for(int i = 0; i < n;i++){
        string mode;
        cin >> mode;
        if(mode == "C"){
            int q;
            cin >>q;
            if(isit(q) == true){
                //cout << "ok "<< q;
                li.push_back({q,{lc,rc}});
                cset(q,li.size()-1);
                sets.insert({q,li.size()-1});
                li2[li.size()-1]={1,1};
                //cout << "\n";
                ln+=1;
                rn+=1;
                rr+=1;
            }
        }
        else if(mode == "L"){
            lc+=1;
            for(auto i = sets2[lc+rc].begin(); i!= sets2[lc+rc].end(); i++){
                if(li2[(*i).first].second == 1){
                    rn-=1;
                    li2[(*i).first].second=0;
                }
                if(li2[(*i).second].first == 1){
                    ln-=1;
                    li2[(*i).second].first=0;
                }
            }

            rr+=ln;

        }
        else if(mode == "R"){
            rc+=1;
            for(auto i = sets2[lc+rc].begin(); i!= sets2[lc+rc].end(); i++){
                if(li2[(*i).first].second == 1){
                    rn-=1;
                    li2[(*i).first].second=0;
                }
                if(li2[(*i).second].first == 1){
                    ln-=1;
                    li2[(*i).second].first=0;
                }
            }

            rr+=rn;

        }
        else if(mode == "Q"){
            cout << rr<<"\n";
        }
        //cout << "rr: "<<rr<<"\n";
    }

	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//cin >> _case;

	for (_caseidx = 0; _caseidx < _case; _caseidx++) {
		if (sol()) break;
	}

	//while (!sol()) {

	//}
}






