#define _USE_MATH_DEFINES
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
#include <array>
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <forward_list>
#include <future>
#include <initializer_list>
#include <mutex>
#include <random>
#include <ratio>
#include <regex>
#include <scoped_allocator>
#include <system_error>
#include <thread>
#include <tuple>
#include <typeindex>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>


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

int n, q;
llint li[500001];
llint li2[500000];
multiset<llint> sets;

int sol() {
	cin >> n >> q;
	for (int i = 0; i < n; i++) {
		cin >> li[i];
	}
	for (int i = 0; i < n-1; i++) {
		li2[i] = li[i+1] - li[i];
		sets.insert(li2[i]);
	}


	for (int i = 0; i < q; i++) {
		llint m = 0;
		cin >> m;
		if (m==2) {
			if (*(sets.begin()) < 0) {
				cout << "NO\n";
			}
			else {
				cout << "YES\n";
			}
		}
		else {
			llint l, r, v;
			cin >> l >> r >> v;
			if (l > 1) {
				sets.erase(sets.find(li2[l - 2]));
				li2[l - 2] += v;
				sets.insert(li2[l - 2]);
			}
			if (r < n) {
				sets.erase(sets.find(li2[r-1]));
				li2[r-1] += -v;
				sets.insert(li2[r-1]);
			}
		}
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






