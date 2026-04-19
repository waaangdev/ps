//Factory Balls

#include <deque>
#include <iostream>
#include <array>
#include <string>

using namespace std;

bool bang[6][6][6][6][6][6][6][6][6][6] = {false};
deque<array<int, 11>> q;
bool wall[8][8];
int box2[8][8];
bool mok[8][8];
bool bfsbang[8][8];
int box[4][2];

int pl[2];
int dum2,dum3,dum4,dum5, dum6, dum7,dum8,dum9, dum33, dum44;
int dum;
int dum9mok,r;
bool end_;

int ang1[4] = { 0,1,0,-1 };
int ang2[4] = { -1,0,1,0 };

deque<array<int, 2>> bfs;

string inp;

int main() {

	int j = -1;
	dum = 0;
	dum9mok = 0;
	dum9 = 0;
	r = 0;

	while (getline(cin, inp)) {
		if (inp.empty()) {
			break;
		}
		j += 1;
		for (int i = 0; i < inp.length(); i++) {
			if ((inp.at(i)) == '#') {
				wall[j][i] = 1;
				
			}
			else if ((inp.at(i)) == '.') {
				dum9mok += 1;
				mok[j][i] = 1;
			}
			else if ((inp.at(i)) == '$') {
				box[dum][0] = j;
				box[dum][1] = i;
				dum += 1;
			}
			else if ((inp.at(i)) == '*') {
				box[dum][0] = j;
				box[dum][1] = i;
				dum += 1;
				mok[j][i] = 1;
				dum9mok += 1;
				dum9 += 1;
			}
			else if ((inp.at(i)) == '@') {
				pl[0] = j;
				pl[1] = i;
			}
			else if ((inp.at(i)) == '+') {
				pl[0] = j;
				pl[1] = i;
				mok[j][i] = 1;
				dum9mok += 1;
			}
		}
	}
	q.push_back({ pl[0],pl[1],box[0][0],box[0][1] ,box[1][0],box[1][1],box[2][0],box[2][1] ,box[3][0],box[3][1] ,dum9});
	if (dum9 == dum9mok) {
		end_ = true;
	}
	while (!q.empty() && !end_) {
		

		r += 1;
		dum = q.size();
		for (int i = 0; i < dum; i++) {
			pl[0] = q.front()[0];
			pl[1] = q.front()[1];
			box[0][0] = q.front()[2];
			box[0][1] = q.front()[3];
			box[1][0] = q.front()[4];
			box[1][1] = q.front()[5];
			box[2][0] = q.front()[6];
			box[2][1] = q.front()[7];
			box[3][0] = q.front()[8];
			box[3][1] = q.front()[9];
			dum2 = q.front()[10];

			q.pop_front();

			for (int j = 0; j < 8; j++) {
				for (int k = 0; k < 8; k++) {
					box2[j][k] = 0;
					bfsbang[j][k] = false;
				}
			}

			for (int j = 0; j < 4; j++) {
				box2[box[j][0]][box[j][1]] = j+1;
			}
			
			/*
			cout << r << " " << pl[0] << " " << pl[1] << "\n";
			for (int i = 0; i < 8; i++) {
				for (int j = 0; j < 8; j++) {
					cout << box2[i][j];
				}
				cout << "\n";
			}
			*/

			bfsbang[pl[0]][pl[1]] = true;
			bfs.push_back({ pl[0],pl[1] });
			bang[pl[0] - 1][pl[1] - 1][box[0][0] - 1][box[0][1] - 1][box[1][0] - 1][box[1][1] - 1][box[2][0] - 1][box[2][1] - 1][box[3][0] - 1][box[3][1] - 1] = true;
			
			while (!bfs.empty()) {
				for (int j = 0; j < 4; j++) {
					dum3 = bfs.front()[0] + ang1[j];
					dum4 = bfs.front()[1] + ang2[j];

					if (!wall[dum3][dum4] && !bfsbang[dum3][dum4]) {
						if (box2[dum3][dum4]) {
							dum33 = dum3 + ang1[j];
							dum44 = dum4 + ang2[j];
							if (!box2[dum33][dum44] && !wall[dum33][dum44]) {
								/*
								cout <<"a" << "\n";
								cout << box[0][0] << " " << box[0][1] << " " << box[1][0] << " " << box[1][1] << " " << box[2][0] << " " << box[2][1] << " " << box[3][0] << " " << box[3][1]<<"\n";
								cout << dum3 << " " << dum4 << "\n";
								*/
								dum9 = 0;
								dum5 = box2[dum3][dum4];
								if (mok[dum3][dum4]) {
									dum9 -= 1;
								}
								box[dum5 - 1][0] += ang1[j];
								box[dum5 - 1][1] += ang2[j];
								box2[dum3][dum4] = 0;
								box2[box[dum5 - 1][0]][box[dum5 - 1][1]] = dum5;
								if (mok[dum33][dum44]) {
									dum9 += 1;
								}
								if (!bang[dum3 - 1][dum4- 1][box[0][0] - 1][box[0][1] - 1][box[1][0] - 1][box[1][1] - 1][box[2][0] - 1][box[2][1] - 1][box[3][0] - 1][box[3][1] - 1]) {
									q.push_back({ dum3,dum4,box[0][0],box[0][1] ,box[1][0],box[1][1],box[2][0],box[2][1] ,box[3][0],box[3][1] ,dum2 + dum9 });

									if (dum2 + dum9 == dum9mok) {
										end_ = true;
									}
								}

								box[dum5 - 1][0] -= ang1[j];
								box[dum5 - 1][1] -= ang2[j];
								box2[dum3][dum4] = dum5;
								box2[dum33][dum44] = 0;


							}
						}
						else{

							if (!bang[dum3 - 1][dum4- 1][box[0][0] - 1][box[0][1] - 1][box[1][0] - 1][box[1][1] - 1][box[2][0] - 1][box[2][1] - 1][box[3][0] - 1][box[3][1] - 1]) {
								bang[dum3 - 1][dum4 - 1][box[0][0] - 1][box[0][1] - 1][box[1][0] - 1][box[1][1] - 1][box[2][0] - 1][box[2][1] - 1][box[3][0] - 1][box[3][1] - 1] = true;
							}
							else {
								//cout << "c" << dum3 << " " << dum4 << "\n";
								while (!bfs.empty()) {
									bfs.pop_front();
								}
							}

							bfs.push_back({ dum3,dum4 });
							bfsbang[dum3][dum4] = true;
							//cout << "b" << dum3 << " " << dum4 << "\n";
							
						}
					}
				}
				bfs.pop_front();
			}

		}


	}
	std::cout << r;	

	return 0;
}
