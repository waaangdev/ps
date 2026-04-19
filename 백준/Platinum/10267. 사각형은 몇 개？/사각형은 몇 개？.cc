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


struct int_pair {
	int first;
	int second;
};

struct moja {
	int mo;
	int ja;
	int m = 1;//1,-1,2,3:무한
};
struct position {
	moja x;
	moja y;
};

struct line {
	moja angle;//분모,분자
	//int pos[2];//무조건 통과하는 점
	position xy;//x,y 절편
};

int n, r, tmp;
unordered_map<int, vector<int>> li;
unordered_map<int, unordered_map<int, int>> li2;
line lines[2000];//분모,분자,절편

int mojastr(moja a);

int GCD(int a, int b) {
	//cout << a << " " << b << "\n";
	int tmp;
	while (1) {
		if (b == a or b == 0) return a;
		if (a > b) swap(b, a, tmp);
		b %= a;
	}
}

moja mojaset(moja a) {
	if (a.m == 3) return { 0,0,3 };
	if (a.m == 2) return { 0,0,2 };
	if (a.ja == 0) return { 0,0,2 };
	if (a.mo == 0) return { 0,0,3 };
	if ((a.ja < 0 and a.mo > 0) or a.ja > 0 and a.mo < 0) a.m *= -1;
	//cout <<"set!: " << mojastr(a)<< " ->";
	a.ja = abs(a.ja);
	a.mo = abs(a.mo);
	int d = GCD((a.ja), (a.mo));
	a.ja /= d;
	a.mo /= d;
	//cout << mojastr(a) << "\n";
	return a;
}
moja mojaadd(moja a, moja b, int m) {
	if (a.m == 3) {
		return { 0,0,3 };
	}if (b.m == 3) {
		return { 0,0,3 };
	}if (a.m == 2) {
		b.m *= m;
		return mojaset(b);
	}if (b.m == 2) {
		return a;
	}
	//cout << "add!: " << mojastr(a) << ((m < 0)?" - ":" + ") << mojastr(b);
	a.ja = a.ja * (b.mo);
	//cout << " = " << a.mo <<" asd "<< b.mo << "\n";
	int dum = a.ja * a.m + b.ja * m * b.m * (a.mo);
	a.mo = a.mo * (b.mo);
	a.ja = abs(dum);
	if (dum < 0) {
		a.m = -1;
	}
	else {
		a.m = 1;
	}
	//cout << " = " << mojastr((a))<< "\n";
	//cout << "add!: " << abs(a.ja) << " " << a.mo << "\n";
	return mojaset(a);
}
moja mojamulti(moja a, moja b) {//a*b
	if (a.m == 2) {
		return { 0,0,2 };
	}if (b.m == 2) {
		return { 0,0,2 };
	}
	if (a.m == 3) {
		return { 0,0,3 };
	}if (b.m == 3) {
		return { 0,0,3 };
	}
	//cout << "multi!: " << mojastr(a) << " * " << mojastr(b);
	a.mo *= b.mo;
	a.ja *= b.ja;
	a.m *= b.m;
	//cout << " = " << mojastr(mojaset(a))<< "\n";
	//cout << "mojamulti!: " << abs(a.ja) << " " << a.mo << "\n";
	return mojaset(a);
}
moja mojareverse(moja a) {
	if (a.m == 3) {
		return { 0,0,2 };
	}
	if (a.m == 2) {
		return { 0,0,3 };
	}
	return mojaset({ a.ja,a.mo,a.m });
}
moja moja90(moja a) {
	if (a.m == 3) {
		return { 0,0,2 };
	}
	if (a.m == 2) {
		return { 0,0,3 };
	}
	a.m *= -1;
	return mojareverse(a);
}
int mojastr(moja a) {
	if (a.m == 3) {
		return 100000001;
	}
	if (a.m == 2) {
		return 0;
	}
	a = mojaset(a);
	return (a.ja+(a.mo*10000)) * a.m;
}
moja str2moja(int a) {
	if (a == 100000001) {
		return { 0,0,3 };
	}
	if (a == 0) {
		return { 0,0,2 };
	}
	return mojaset({ abs(a/10000),abs(a % 10000),(a < 0) ? -1 : 1});
}

line pos2line(int x1, int y1, int x2, int y2) {
	int tmp;

	if (x1 == x2) {
		return { {0,0,3},{mojaset({1,x1,1}),{0,0,3}} };
	}
	if (y1 == y2) {
		return { {0,0,2},{{0,0,3},mojaset({1,y1,1})} };
	}
	if (x1 > x2) {
		swap(x1, x2, tmp);
		swap(y1, y2, tmp);
	}
	//cout << x2 - x1 << " " << y2 - y1 << "\n";
	moja d = mojaset({ x2 - x1, y2 - y1 ,1 });
	//y = (x) = -2/-1
	//cout << mojamulti(mojaset({ 1,y1 }), mojareverse(d)).ja << "/" << mojamulti(mojaset({ 1,y1 }), mojareverse(d)).mo << "\n";

	moja xx = mojaadd(mojaset({ 1,x1 ,1 }), mojamulti(mojaset({ 1,y1 ,1 }), mojareverse(d)), -1);//x절편, x1-(y1/ang)
	moja yy = mojaadd(mojaset({ 1,y1 ,1 }), mojamulti(mojaset({ 1,x1 ,1 }), (d)), -1);//y절편, y1-(x1*ang)
	//cout << "yy " << mojamulti(mojaset({ 1,x1 }), (d)).ja << "/" << mojamulti(mojaset({ 1,x1 }), (d)).mo << "\n";
	return { d ,{xx,yy} };

}

moja distance2linex(line a, line b) {
	moja ret;
	if (a.angle.m == 2) {
		return { 0,0,3 };
	}
	else {
		ret = mojaset(mojaadd(a.xy.x, b.xy.x, -1));
		ret.m = 1;
		return ret;
	}
}
moja distance2liney(line a, line b) {
	moja ret;
	if (a.angle.m == 3) {
		return { 0,0,3 };
	}
	else {
		ret = mojaset(mojaadd(a.xy.y, b.xy.y, -1));
		ret.m = 1;
		return ret;
	}
}



int sol() {
	cin >> n;
	r = 0;
	li.clear();
	li2.clear();

	for (int i = 0; i < n; i++) {
		int inp[4];
		cin >> inp[0] >> inp[1] >> inp[2] >> inp[3];
		line dline = pos2line(inp[0], inp[1], inp[2], inp[3]);

		//cout << "dline " << dline.angle.ja << "/" << dline.angle.mo<<" " << dline.xy.x.ja << "/" << dline.xy.x.mo << " " << dline.xy.y.ja << "/" << dline.xy.y.mo << "\n";
		//cout << "dline " << mojastr(dline.angle) << " " << dline.angle.m << " " << mojastr(dline.xy.x) << " " << mojastr(dline.xy.y) << "\n";
		int dstr = mojastr(dline.angle);
		if (li.find(dstr) == li.end()) {
			li.insert({ dstr ,{i} });
		}
		else {
			li[dstr].push_back(i);
		}
		lines[i] = dline;
	}


	for (auto i = li.begin(); i != li.end(); i++) {

		moja dangle = str2moja(i->first);
		//moja dangle90 = moja90(dangle);
		li2.insert({ mojastr(dangle), {} });
		auto li22 = &li2[mojastr(dangle)];
		auto lis = ((*i).second);

		//cout << i->first << " : (";
		//for (auto i3 = lis.begin(); i3 != lis.end(); i3++) {
		//	cout << *i3<< " ";
		//}
		//cout << ")\n";

		//cout << i->first << " " << i2->first << "(";
		for (int j = 0; j < lis.size(); j++) {
			//cout << lines[lis[j]].xy.x.ja << "/" << lines[lis[j]].xy.x.mo << " ";
			for (int k = 0; k < j; k++) {
				//직선두개골랐음
				int dum;
				//두개y절편거리
				if (dangle.m == 2 or dangle.m == -1) {
					dum = mojastr(distance2liney(lines[lis[j]], lines[lis[k]]));
				}
				else {
					//두개x절편거리
					dum = mojastr(distance2linex(lines[lis[j]], lines[lis[k]]));
					
				}
				if (dum != 100000001) {
					if (li22->find((dum)) == li22->end()) {
						li22->insert({ dum,1 });
					}
					else {
						(*li22)[dum] += 1;
					}
				}
			}
		}
		//cout << ")\n";
	}
	for (auto i = li2.begin(); i != li2.end(); i++) {

		moja dangle = str2moja(i->first);

		auto lis = (li2[(i->first)]);

		//cout << i->first << " : (";
		//for (auto i3 = lis.begin(); i3 != lis.end(); i3++) {
		//	cout << i3->first << ":(" << i3->second[0] << " " << i3->second[1] << ") ";
		//}
		//cout << ")\n";
		if (dangle.m == 2 or dangle.m == -1) {

			moja dangle90 = moja90(dangle);
			auto lis2 = li2[mojastr(dangle90)];

			for (auto i3 = lis.begin(); i3 != lis.end(); i3++) {
				if (lis2.find(i3->first) != lis2.end()) {
					r += i3->second * lis2[i3->first];
				}
			}
		}
	}

	cout << r << "\n";
	//if (r / 2 != q[qidx]) {
	//	cout << "f "<<q[qidx]<<"\n";
	//	return 1;
	//}
	//qidx += 1;
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






