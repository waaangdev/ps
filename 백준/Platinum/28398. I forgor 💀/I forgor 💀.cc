#define _USE_MATH_DEFINES
#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

int _case = 1;
int _caseidx = 0;

template<typename T> using MinHeap = priority_queue<T, vector<T>, greater<T>>;

template <typename T> bool minimize(T &target, T candidate) {
    return target > candidate ? (target = candidate, true) : false;
}
template <typename T> bool maximize(T &target, T candidate) {
    return target < candidate ? (target = candidate, true) : false;
}

// struct int_pair {
// 	int first;
// 	int second;
// };

//bool compare(int_pair i, int_pair j) {
//	if (i.first == j.first) {
//		return i.second < j.second;
//	}
//	return i.first < j.first;
//}

//auto [a,b,c] = tuple(1,2,3);
struct st {
	int l;
	int r;
	int res[2][2];
};
int n,q;
pair<int,int> li[402020];
int li2[402020];
int li3[402020][2];
st tree[402020*4];

st segmerge(st a,st b){
    st r;
    r.l = a.l;
    r.r = a.r;
    for (int i = 0; i < 2;i++){
		for (int j = 0; j < 2;j++){
			r.res[i][j] = a.res[i][j];
		}
	}

	if(b.l == 0){
		return a;
	}

	for (int i = 0; i < 2;i++){
		for (int j = 0; j < 2;j++){
			r.res[i][j] += b.res[(i+a.res[i][j])%2][a.r==b.l];
		}
	}
	r.r = b.r;
	return r;
}


void segupdate(int idx){
	idx+=262144*2;
	idx/=2;
	while(idx){
		tree[idx] = segmerge(tree[idx*2],tree[idx*2+1]);
		idx/=2;
	}
}

void seginit(int idx,int num,int right){
	//cout << right << " ";
	idx+=262144*2;
	tree[idx].l = num;
	tree[idx].r = num;
	if(right){
		tree[idx].res[0][0] = 3;
		tree[idx].res[0][1] = 1;
		tree[idx].res[1][0] = 2;
		tree[idx].res[1][1] = 2;
	}
	else{
		tree[idx].res[0][0] = 1;
		tree[idx].res[0][1] = 1;
		tree[idx].res[1][0] = 1;
		tree[idx].res[1][1] = 1;
	}
}



int sol() {
	cin >> n >> q;
	for(int i=  0; i < n*2;i++){
		cin >> li[i].first;
		seginit(i,li[i].first,li2[li[i].first]);

		li[i].second=li2[li[i].first];
		li3[li[i].first][li[i].second] = i;
		li2[li[i].first]=1;
	}
	for(int i=  0; i < n*2;i++){
		segupdate(i);
	}
	cout <<tree[1].res[1][0]/2 <<"\n";

	for(int i= 0; i < q;i++){
		int l,r;
		cin >> l>>r;
		l-=1;
		r-=1;
		swap(li[l],li[r]);

		li3[li[l].first][li[l].second] = l;
		li3[li[r].first][li[r].second] = r;

        int dli[] = {l,r,li3[li[l].first][1-li[l].second],li3[li[r].first][1-li[r].second]};
        for(int j = 0; j<4;j++ ){
            seginit(dli[j],li[dli[j]].first,li3[li[dli[j]].first][li[dli[j]].second] > li3[li[dli[j]].first][1-li[dli[j]].second]);
		    segupdate(dli[j]);
        }
       
		cout <<tree[1].res[1][0]/2 <<"\n";

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