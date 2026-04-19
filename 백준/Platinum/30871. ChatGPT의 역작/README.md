# [Platinum III] ChatGPT의 역작 - 30871 

[문제 링크](https://www.acmicpc.net/problem/30871) 

### 성능 요약

메모리: 5144 KB, 시간: 96 ms

### 분류

애드 혹, 매개 변수 탐색

### 제출 일자

2026년 04월 19일 22:59:58

### 문제 설명

<p>대회가 다가오는데도 문제를 만들지 못한 하이비는 결국 AI의 힘을 빌려 다음과 같은 문제를 만들었다.</p>

<p>정수 $x$, 길이 $N$의 정수로 이루어진 수열 $L$과 $R$에 대해, 다음과 같은 함수 $f$를 정의해 보자.</p>

<pre><code>f(x, L[1..N], R[1..N]):
    value = x
    for i = 1 to N
        l = L[i]
        r = R[i]
        if l ≤ x ≤ r
           value = value^(((x|l)+(x&r)*(l^r)) mod (2**64))
    return (value >= 0x0123456789ABCDEF)</code></pre>

<p>코드에 적힌 <span style="color:#e74c3c;"><code>|</code></span>, <span style="color:#e74c3c;"><code>&</code></span>, <span style="color:#e74c3c;"><code>^</code></span>, <span style="color:#e74c3c;"><code>**</code></span>, <span style="color:#e74c3c;"><code>0x</code></span>, <span style="color:#e74c3c;"><code>mod</code></span>연산에 대해서는 노트를 참고하자.</p>

<p>$L$과 $R$이 주어질 때, $f(x,L,R) =\text{False}$이면서 $f(x+1,L,R) =\text{True}$인 $x$를 찾으면 된다.</p>

<p>하지만 AI가 만들어 준 이 문제가 너무 어려웠던 하이비는 이 문제를 풀지도 못한 채로 내야 할 위기에 처하게 되었다! 하이비를 위해 위 문제의 답을 찾아주자.</p>

### 입력 

 <p>첫 번째 줄에는 수열의 길이 $N$이 주어진다. $(1\le N\le 200\, 000)$</p>

<p>두 번째 줄에는 수열 $L_1,L_2,\ldots ,L_N$이 공백으로 구분되어 주어진다.</p>

<p>세 번째 줄에는 수열 $R_1,R_2,\ldots ,R_N$이 공백으로 구분되어 주어진다. $(1\le L_i\le R_i\le 10^{18})$</p>

### 출력 

 <p>첫 번째 줄에 문제의 답으로 가능한 $x$의 값을 출력한다. $(0\le x\le 10^{18})$</p>

<p>만약 가능한 답이 여러 가지라면, 그중 아무거나 하나를 출력한다.</p>

<p>만약 가능한 답이 없다면, $-1$을 출력한다.</p>

