#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>



int longnum(int number);


int main() {
    int i, j;
    int n;
    int num[1000][3]; //0인덱스에 숫자,1인덱스에 자릿수,2인덱스에 앞자릿수
    int aa = 0;


    int one1[10] = { 1,11,111,1111,11111,111111,1111111,11111111,111111111,1111111111 };
    long long int tenmul[12];
    tenmul[0] = 1;
    for (i = 1; i < 12; i++) {
        tenmul[i] = tenmul[i - 1] * 10;
    }



    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%d", &num[i][0]);
        num[i][1] = longnum(num[i][0]);
        num[i][2] = num[i][0] / tenmul[(num[i][1] - 1)];
    }
    for (i = 0; i < n; i++) {
        if (num[i][0] != 0) {
            aa = 1;
            break;
        }
    }
    if (aa != 1) {
        printf("%d", 0);
        return 0;
    }

    for (i = n - 1; i > 0; i--) {
        for (j = 0; j < i; j++) {//100 com 100123 ->100111
            long long int c1 = 0, c2 = 0, d;
            d = (num[j + 1][1] > num[j][1] ? num[j + 1][1] : num[j + 1][1]) - (num[j + 1][1] > num[j][1] ? num[j][1] : num[j + 1][1]);

            c1 = num[j + 1][0] * tenmul[num[j][1]] + num[j][0];
            c2 = num[j][0] * tenmul[num[j + 1][1]] + num[j + 1][0];

            if ((num[j + 1][2] > num[j][2]) || ((c1 > c2) && (num[j + 1][2] == num[j][2]))) {
                long long int temp;
                temp = num[j + 1][0];
                num[j + 1][0] = num[j][0];
                num[j][0] = temp;
                temp = num[j + 1][1];
                num[j + 1][1] = num[j][1];
                num[j][1] = temp;
                temp = num[j + 1][2];
                num[j + 1][2] = num[j][2];
                num[j][2] = temp;
            }
        }
    }

    for (i = 0; i < n; i++) {
        printf("%d", num[i][0]);
    }
}

//함수

int longnum(int num) {
    long long int ten = 1, a = 0;
    do {
        a++;
        ten *= 10;
    } while (num / ten >= 1);
    return a;
}