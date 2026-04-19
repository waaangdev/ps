//볼록껍질

#define _USE_MATH_DEFINES

#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int llint;

struct node {
	int x;
	int y;
	double angle;
};


vector<node> li;
int n;
double gijun_angle;


bool compair(node a,node b) {
	return a.angle > b.angle;
}
double angleset(double a, double b) {
	a -= b;
	while (a < 0) a += (2 * M_PI);
	while (a > (2 * M_PI)) a -= (2 * M_PI);
	return a;
}

double anglebetween(int idx1, int idx2) {
	return -atan2(li[idx1].y - li[idx2].y, li[idx1].x - li[idx2].x);;
}

array<int,2> sol(int index,double anglehis) {//검사한거개수, 컨벡스헐갯수
	if (index == n-1) {
		return { 1,1 };
	}

	//cout << li[index].x << " " << li[index].y << "\n";

	int r = 0;
	int gumsa = 1;

	int dum = 0;//개수
	int dum2 = 1;//인덱스
	int dum5 = 0;//ㅇㅇ
	while (dum == 0) {
		if (index + dum >= n) {
			break;
		}
		double dum3 = angleset(anglebetween(index, index + dum2),gijun_angle);
		//cout << index<<" " << index + dum2 << " "<<dum3 << "\n";
		if (dum3 > anglehis) {
			if (abs(anglehis - dum3) == M_PI) {
				dum = 0;
				dum2 +=1;
			}
			else {
				auto dum4 = sol(index + dum2, dum3);
				dum = dum4[1];
				dum2 += dum4[0];
			}
		}
		else{
			if (dum3 < anglehis) {
				break;
			}
			else { //한 변에 점 두개
				auto dum4 = sol(index + dum2, dum3);
				dum = dum4[1];
				dum2 += dum4[0];
				dum5 = 1;
			}
		}
	}
	gumsa = dum2;
	r = dum + 1-dum5;

	if (dum == 0) {
		return { gumsa,0 };
	}

	//cout << index << " " << r << "\n";
	return {gumsa,r};
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	int d_maxx = -40001;
	int d_maxx_i;
	for (int i = 0; i < n; i++) {
		int inp1,inp2;
		cin >> inp1 >> inp2;
		li.push_back({ inp1,inp2 });
		if (inp1 > d_maxx) {
			d_maxx = inp1;
			d_maxx_i = i;
		}
	}

	node gijun = { li[d_maxx_i].x,li[d_maxx_i].y };
	li.erase(li.begin()+ d_maxx_i);
	for (int i = 0; i < n-1; i++) {
		li[i].angle = atan2(gijun.y - li[i].y, gijun.x - li[i].x);
	}


	sort(li.begin(), li.end(), compair);
	li.push_back(gijun);

	//for (int i = 0; i < n ; i++) {
	//	cout << li[i].x << "-" << li[i].y << ", ";
	//}
	//cout << "\n";

	int r = 0;
	gijun_angle = angleset(-atan2(gijun.y - li[0].y, gijun.x - li[0].x), 0);
	cout << sol(0, (double)0)[1];








	//node dp[100000];


	//dp[0] = { li[0].x,li[0].y,angleset(-atan2(gijun.y - li[0].y, gijun.x - li[0].x)) };
	//dp[0] = { li[0].x,li[0].y,-1 };
	//int last = 0;


	//for (int i = 1; i < n; i++) {
	//	double dum = angleset( -atan2(dp[last].y - li[i].y, dp[last].x - li[i].x));
	//	if (dum < dp[last].angle) {

	//		dp[i] = { li[0].x,li[0].y,dum };
	//	}
	//	if (dum != dp[last].angle) {
	//		r += 1;
	//	}
	//	dp[i] = { li[0].x,li[0].y,dum };
	//}



	//node last = { li[0].x,li[0].y,-atan2(gijun.y - li[0].y, gijun.x - li[0].x) };
	//while (last.angle < 0) last.angle += (2 * M_PI);
	//while (last.angle > (2 * M_PI)) last.angle -= (2 * M_PI);
	//for (int i = 0; i < n - 1; i++) {
	//	double dum = -atan2(last.y - li[i + 1].y, last.x - li[i + 1].x);
	//	while (dum < 0) dum += (2 * M_PI);
	//	while (dum > (2 * M_PI)) dum -= (2 * M_PI);
	//	cout << li[i].x << " " << li[i].y << " " << (li[i].angle)/(2*M_PI)*360 << " " << dum / (2 * M_PI) * 360 << " | " << last.x << " " << last.y << " " << last.angle / (2 * M_PI) * 360 << "\n";
	//	if (abs(last.angle - dum) > M_PI - 0.0001 and abs(last.angle - dum) < M_PI + 0.0001) {
	//		cout << "b\n";
	//		continue;
	//	}
	//	if (last.angle <= dum) {
	//		if ((last.angle != dum)) {
	//			r += 1;
	//			cout << "a\n";
	//		}
	//		last = { li[i+1].x,li[i+1].y,dum};;
	//		
	//	}
	//}
	//cout << r;
}






