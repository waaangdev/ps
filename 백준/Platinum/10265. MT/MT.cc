//A Plus Equals B

#define _USE_MATH_DEFINES

#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

struct node {
	int first;
	int second;
};

llint n,k;
int li[1000];
bool li_bang[1000];
int group_count;
int group_num[1000][2];//groupID,index(in group)
int group[1000][3];//enable,min,max
int group_union[1000];

int groups_count;
int groups[1000][2];//min,max


int unionFind(int groupIndex) {
	int dum = group_union[groupIndex];
	if (dum == groupIndex) {
		return groupIndex;
	}
	else {
		int dum2 = unionFind(dum);
		group_union[groupIndex] = dum2;
		return dum2;
	}
}


void dfs(int index,int groupnum,int ingroupIndex) {
	li_bang[index] = true;
	group_num[index][0] = groupnum;
	group_num[index][1] = ingroupIndex;

	int index2 = li[index];

	ingroupIndex += 1;
	if (li_bang[index2]) {
		if (group_num[index2][0] == groupnum) {
			//사이클 발견
			group[groupnum][1] = ingroupIndex - group_num[index2][1];
			group[groupnum][2] = ingroupIndex;
		}
		else {
			//다른 그룹의 사이클 발견
			int groupnum2 = unionFind(group_num[index2][0]);
			group_union[groupnum] = groupnum2;
			group[groupnum][0] = 1;//우리 그룹 비활성화
			group[groupnum2][2] += ingroupIndex;
		}
	}
	else {
		dfs(index2, groupnum, ingroupIndex);
	}
}


int sol(int m, int index) {
	if (m == 0) { return 0; }
	int r = 0;
	for (int i = index+1; i < groups_count; i++) {
		if (groups[i][0] <= m) {
			int dum = sol(m - groups[i][0], i);
			if (dum + groups[i][1] >= m) {
				return m;
			}
			else {
				r = max(r, dum + groups[i][1]);
			}
		}
	}
	return r;
}


int main() { 
	for (int i = 0; i < 1000; i++) {
		group_union[i] = i;
	}
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> li[i];
		li[i] -= 1;
	}
	for (int i = 0; i < n; i++) {
		if (!li_bang[i]) {
			dfs(i, group_count, 0);
			group_count += 1;
		}
	}
	//for (int i = 0; i < n; i++) {
	//	cout << group_num[i][0] << " ";
	//}
	//cout << "\n---group---\n";
	//for (int i = 0; i < group_count; i++) {
	//	cout << group[i][0] << " " << group[i][1] << " "<< group[i][2] << "\n";
	//}
	for (int i = 0; i < group_count; i++) {
		if (group[i][0] == 0) {
			groups[groups_count][0] = group[i][1];
			groups[groups_count][1] = group[i][2];
			groups_count += 1;
		}
	}
	//for (int i = 0; i < groups_count; i++) {
	//	cout << groups[i][0] << " " << groups[i][1] << "\n";
	//}

	cout << sol(k, -1);
}






