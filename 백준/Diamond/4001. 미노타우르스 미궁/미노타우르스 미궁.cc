#define _USE_MATH_DEFINES
#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

int _case = 1;
int _caseidx = 0;


int n,m,nemoc,rr;
pair<int,int> rrnum = {-1,-1};

char maps[1515][1515];
int garo[1515][1515];
int sero[1515][1515];
int nemo[1515][1515];

int garoMax[2][1515][1515];
int seroMax[2][1515][1515];

int group[2][1515][1515];


int sol() {
	cin >> n>>m;
    for(int i = 0; i < m;i++){
        string inp;
        cin >>inp;
        for(int j = 0; j < n;j++){
            maps[i][j] = inp[j];
        }
    }

    maps[0][0] = '#';
    maps[m-1][n-1] = '#';
    for(int i = 0; i < m;i++){
        for(int j = 0; j < n;j++){
            if(maps[i][j] == '.'){
                garo[i][j] = 1;
                if(j > 0) garo[i][j] = garo[i][j-1]+1;
            }
        }
    }
    for(int j = 0; j < n;j++){
        for(int i = 0; i < m;i++){
            if(maps[i][j] == '.'){
                sero[i][j] = 1;
                if(i > 0) sero[i][j] = sero[i-1][j]+1;
            }
        }  
    }
    for(int i = 0; i < m;i++){
        for(int j = 0; j < n;j++){
            if(maps[i][j] == '.'){
                nemo[i][j] = 1;
                if(j > 0 and i > 0) nemo[i][j] = min(nemo[i-1][j-1]+1,min(sero[i][j],garo[i][j]));
            }
        }
    }

    deque<pair<int,int>> q;
    
    rr = n*m;

    for(int k = 0; k < 2;k++){
        q.clear();
        if(k == 0){
            for(int i = 1; i < m;i++){
                q.push_back({i,0});
            }
            for(int i = 1; i < n-1;i++){
                q.push_back({m-1,i});
            }
        }
        else{
            for(int i = 1; i < m-1;i++){
                q.push_back({i,n-1});
            }
            for(int i = 1; i < n;i++){
                q.push_back({0,i});
            }
        }

        while (!q.empty()){
            auto [y,x] = tuple(q.front().first,q.front().second);

            group[k][y][x] = 1;

            if(maps[y][x] == '#'){
                for(int i = 0; i < 8;i++){
                    for (int ny = y-1; ny<y+2;ny++){
                        for (int nx = x-1; nx<x+2;nx++){
                            if(ny > -1 and ny < m and nx > -1 and nx < n){
                                if(group[k][ny][nx] == 0){
                                    q.push_back({ny,nx});

                                    group[k][ny][nx] = 1;
                                }
                            }
                        }
                    }
                }
            }
            q.pop_front();
        }
    }


    for(int k = 0; k < 2;k++){
        for(int i = 0; i < m ;i++){
            garoMax[k][i][0] = -1;
            for(int j = 0; j < n;j++){
                if(j) garoMax[k][i][j]=garoMax[k][i][j-1]; 
                if(group[k][i][j] == 1) garoMax[k][i][j]=j; 
            }
        }


        for(int j = 0; j < n;j++){
            seroMax[k][0][j] = -1;
            for(int i = 0; i < m ;i++){
                if(i) seroMax[k][i][j]=seroMax[k][i-1][j]; 
                if(group[k][i][j] == 1) seroMax[k][i][j]=i; 
            }   
        }

    }



    for(int i = m-1; i >-1;i--){

        for(int j = n-1; j > -1;j--){

            if(nemo[i][j] != 0){
                int size = nemo[i][j];
                for(int k = 0; k < 2;k++){

                    int dd = 0;
                    int gad = garoMax[k][i][j];
                    if(gad < j+1 and gad >= j-size+1){
                        dd += 1;
                    }
                    int sed = seroMax[1-k][i][j];
                    if(sed < i+1 and sed >= i-size+1){
                        dd += 1;
                    }
                    if(dd == 2){
                        int d = max(abs(gad-j),abs(sed - i))+1;
                        if(d < rr){
                            rr = d;
                            rrnum.first = i-rr+1;
                            rrnum.second = j-rr+1;
                        }
                    }
                }

                int dd = 0;
                for(int k = 0; k < 2;k++){
                    int gad = garoMax[k][i][j];
                    if(gad < j+1 and gad >= j-size+1){
                        dd |= k+1;
                    }
                    int sed = seroMax[k][i][j];
                    if(sed < i+1 and sed >= i-size+1){
                        dd |= k+1;
                    }
                    gad = garoMax[k][i-size+1][j];
                    if(gad < j+1 and gad >= j-size+1){
                        dd |= k+1;
                    }
                    sed = seroMax[k][i][j-size+1];
                    if(sed < i+1 and sed >= i-size+1){
                        dd |= k+1;
                    }
                }
                if(dd == 3){
                    int d = size;
                    if(d < rr){
                        rr = d;
                        rrnum.first = i-rr+1;
                        rrnum.second = j-rr+1;
                    }
                }


            }
        }
    }

    

    if(rrnum.first == -1){
        cout << "Impossible\n";
    }
    else{
        cout << rr << " " <<rrnum.second+1 << " "<< rrnum.first+1<<"\n";
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






