// 
#include <iostream>
#include<string>
#include<deque>
#include <tuple>
using namespace std;

int size1;
deque<tuple<int,int>> q;
int r = 0;

int main()
{
	cin >> size1;
	int map[3][3];
	for (int i = 0; i < size1; i++) {
		for (int j = 0; j < size1; j++) {
			cin >> map[i][j];
		}
	}
	q.push_back({ 0,0 });
	while (!(q.empty())) {
		if(get<0>(q[0]) + map[get<0>(q[0])][get<1>(q[0])] < size1 && map[get<0>(q[0])][get<1>(q[0])] != 0 )
			q.push_back({ get<0>(q[0]) +map[get<0>(q[0])][get<1>(q[0])],get<1>(q[0]) });
		if (get<1>(q[0]) + map[get<0>(q[0])][get<1>(q[0])] < size1 && map[get<0>(q[0])][get<1>(q[0])] != 0)
			q.push_back({ get<0>(q[0]),get<1>(q[0]) + map[get<0>(q[0])][get<1>(q[0])] });
		if (get<0>(q[0]) == size1-1 && get<1>(q[0]) == size1-1) {
			r = 1;
			break;
		}
		q.pop_front();
	}
	std::cout << ((r == 0)?"Hing":"HaruHaru");
}


