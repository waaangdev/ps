# [Gold I] A Game with Grundy - 19611 

[문제 링크](https://www.acmicpc.net/problem/19611) 

### 성능 요약

메모리: 131924 KB, 시간: 504 ms

### 분류

수학, 정렬

### 제출 일자

2026년 04월 19일 22:59:58

### 문제 설명

<p>Grundy is playing his favourite game - hide and seek.</p>

<p>His N friends stand at locations on the x-axis of a two-dimensional plane - the i-th one is at coordinates (x<sub>i</sub>, 0). Each friend can see things in a triangular wedge extending vertically upwards from their position – the i-th friend’s triangular wedge of vision will be specified by two lines: one with slope of v<sub>i</sub>/h<sub>i</sub> and the other with slope −v<sub>i</sub>/h<sub>i</sub>. A friend cannot see a point that lies exactly on one of these two lines.</p>

<p>Grundy may choose to hide at any location (a, Y), where a is an integer satisfying L ≤ a ≤ R, and L, R, and Y are given integer constants.</p>

<p>Each possible location may be in view of some of Grundy’s friends (namely, strictly within their triangular wedge of vision).</p>

<p>Grundy would like to know in how many different spots he can stand such that he will be in view of at most i of his friends, for every possible value of i from 0 to N.</p>

### 입력 

 <p>The first line of input contains the integer N (1 ≤ N ≤ 100 000).</p>

<p>The next line contains three integers: L, R and Y (−1 000 000 000 ≤ L ≤ R ≤ 1 000 000 000, 1 ≤ Y ≤ 1 000 000).</p>

<p>Each of the next N lines contain three integers: the i-th such line contains x<sub>i</sub> (L ≤ x<sub>i</sub> ≤ R), the x-value of the position of friend i followed by two integers vi and hi (1 ≤ v<sub>i</sub>, h<sub>i</sub> ≤ 100). The slopes v<sub>i</sub>/h<sub>i</sub> and −v<sub>i</sub>/h<sub>i</sub> define the triangular wedge of vision for friend i.</p>

### 출력 

 <p>The output is N + 1 lines, where each line i (0 ≤ i ≤ N) contains the integer number of positions in which Grundy can stand and be in view of at most i of his friends.</p>

