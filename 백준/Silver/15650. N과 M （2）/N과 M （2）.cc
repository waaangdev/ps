#include <iostream>
#include <stdio.h>
#include <array>
using namespace std;

int n, m, arr[8], use[9] = { 0, };

void f(int choose,int a) {
    if (choose == m) {
        for (int i = 0; i < m; i++)
            printf("%d ", arr[i]);
        printf("\n");
        return;
    }

    for (int i = 1; i <= n; i++) {
        if (use[i] != 1) {
            arr[choose] = i;
            use[i] = 1;

            if (a < i) {
                f(choose + 1,i);
            }

            arr[choose] = 0;
            use[i] = 0;
        }
    }
}

int main() {
    cin >> n >> m;
    f(0,-1);
}