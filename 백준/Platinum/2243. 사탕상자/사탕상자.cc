//사탕상자

#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;


int li_count[10000001];
int *tree[21];
int n;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int dum = 1;
	for (int i = 0; i < 21; i++) {
		tree[i] = new int[dum];
		for (int j = 0; j < dum; j++) tree[i][j] = 0;
		dum *= 2;
	}

	cin >> n;
	for (int i = 0; i < n; i++) {
		int inp1, inp2;
		cin >> inp1 >> inp2;
		if (inp1 == 1) {
			int dum3 = 0;
			for (int j = 0; j < 20; j++) {
				//cout << dum3 << "aaa\n";
				if (tree[j+1][dum3*2] >= inp2) {
					dum3 = dum3 * 2;
				}
				else {
					inp2 -= tree[j + 1][dum3 * 2];
					dum3 = dum3 * 2+1;
				}
			}

			cout << dum3 + 1<<"\n";

			li_count[dum3] += -1;
			for (int j = 20; j > -1; j--) {
				tree[j][dum3] += -1;
				dum3 /= 2;
			}

		}
		else {

			inp2 -= 1;
			int inp3;
			cin >>inp3;
			li_count[inp2] += inp3;
			for (int j = 20; j > -1; j--) {
				//cout << inp2 <<"\n";
				tree[j][inp2] += inp3;
				
				inp2 /= 2;
			}
		}


		//for (int j = 19; j > 16; j--) {
		//	for (int k = 0; k < 8; k++) cout << tree[j][k]<<" ";
		//	cout << "\n";
		//}
	}
}











//
//struct node {
//	int first;
//	int second;
//};
//
//int n;
//vector<node> s;
//int count_[10000001];
//
//int sortfind(vector<node>* v, node a,int mode) {//insert,delete,edit,find(return index)
//	int p1, p2;
//	p1 = 0; p2 = v->size();
//	while (p1 + 1 != p2 and p2!=0) {
//		if (mode != 3) (*v)[(p1 + p2) / 2].second += a.second;
//		bool dum = (*v)[(p1 + p2) / 2].first > a.first;
//		dum = (*v)[(p1 + p2) / 2].second > a.first;
//		if (dum) {
//			p2 = (p1 + p2) / 2;
//		}
//		else {
//			p1 = (p1 + p2) / 2;
//		}
//	}
//	if (mode == 0) v->insert(v->begin() + p2, a);
//	if (mode == 1) v->erase(v->begin() + p1);
//
//	if (mode == 3) {
//		return p1;
//	}
//
//	return 0;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//	cout.tie(0);
//	
//	cin >> n;
//	for(int i = 0;i < n; i++){
//		int inp1, inp2;
//		cin >> inp1 >> inp2;
//		if (inp1 == 1) {
//			int dum = sortfind(&s, {inp2,0},3);
//			cout << s[dum].first << "\n";
//			count_[dum] -= 1;
//			sortfind(&s, { dum,-1 }, 2);
//			if (s[dum].second == 0) {
//				sortfind(&s, { inp2,0 }, 1);
//			}
//		}
//		else {
//			int inp3;
//			cin >> inp3;
//			int dum = count_[inp2];
//			bool dum2 = false;
//			if (count_[inp2] == 0) {
//				sortfind(&s, { inp2,inp3 }, 0);
//				dum2 = true;
//
//			}
//			count_[inp2] += inp3;
//			if (!dum2) {
//				if (count_[inp2] == 0) {
//					sortfind(&s, { inp2,inp3 }, 1);
//				}
//				else {
//					sortfind(&s, { inp2,dum + inp3 }, 2);
//				}
//			}
//		}
//		for (int j = 0; j < s.size(); j++) {
//			cout << "(" << s[j].first <<","<< s[j].second << ")" << "-";
//		}
//		cout << "\n";
//	}
//	
//	return 0;
//}
//


//
//void sortinsert(vector<int> *v,int a) {
//	int p1, p2;
//	p1 = 0; p2 = v->size();
//	while (p1 + 1 != p2 and p2!=0) {
//		if ((*v)[(p1 + p2) / 2] > a) {
//			p2 = (p1 + p2) / 2;
//		}
//		else {
//			p1 = (p1 + p2) / 2;
//		}
//	}
//	v->insert(v->begin() + p2, a);
//}
//void sortdel(vector<int>* v, int a) {
//	int p1, p2;
//	p1 = 0; p2 = v->size();
//	while (p1 + 1 != p2 and p2 != 0) {
//		if ((*v)[(p1 + p2) / 2] > a) {
//			p2 = (p1 + p2) / 2;
//		}
//		else {
//			p1 = (p1 + p2) / 2;
//		}
//	}
//	v->erase(v->begin() + p1);
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//	cout.tie(0);
//
//	cin >> n;
//	for(int i = 0;i < n; i++){
//		int inp1, inp2;
//		cin >> inp1 >> inp2;
//		if (inp1 == 1) {
//			auto dum = s[inp2-1];
//			cout << dum << "\n";
//			count_[dum] -= 1;
//			if (count_[dum] == 0) {
//				s.erase(s.begin()+inp2 - 1);
//			}
//		}
//		else {
//			int inp3;
//			cin >> inp3;
//			if (count_[inp2] == 0) {
//				sortinsert(&s, inp2);
//			}
//			count_[inp2] += inp3;
//			if (count_[inp2] == 0) {
//				sortdel(&s, inp2);
//			}
//		}
//		for (int j = 0; j < s.size(); j++) {
//			cout << s[j] << "-";
//		}
//		cout << "\n";
//	}
//
//	return 0;
//}