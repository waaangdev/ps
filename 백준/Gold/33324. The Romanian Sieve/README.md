# [Gold II] The Romanian Sieve - 33324 

[문제 링크](https://www.acmicpc.net/problem/33324) 

### 성능 요약

메모리: 113544 KB, 시간: 1328 ms

### 분류

수학, 정수론, 이분 탐색, 조화수

### 제출 일자

2026년 04월 19일 22:59:58

### 문제 설명

<p>Ionuț Cercel (the son of Petrică Cercel) achieved everything there was to achieve in music after the absolute hit "Made in Romania".</p>

<p>Now he got an interest in competitive programming. In his preparation for the training camp in Phapos, he came across a concept called "The Romanian Sieve", which can be summarized by the following piece of code:</p>

<pre>    int64_t iters = 0;
    for (int64_t i = 1; i ≤ n; i++) {
        for (int64_t j = i; j ≤ n; j += i) {
            max_div[j] = i;
            iters++;
        }
    }
</pre>

<p>As a curious individual, Ionuț asks himself: "Given an integer $t$, what is the largest value of $n$ such that <code>iters</code> $\leq t$ after running the Romanian Sieve algorithm?" Please help him answer this question.</p>

### 입력 

 <p>The first line contains an integer $t$ ($1 \leq t \leq 3 \cdot 10^{13}$).</p>

### 출력 

 <p>Print one integer: the maximum $n$ such that <code>iters</code> $\leq t$ after running the algorithm.</p>

