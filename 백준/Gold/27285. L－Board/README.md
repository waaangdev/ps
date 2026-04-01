# [Gold III] L-Board - 27285 

[문제 링크](https://www.acmicpc.net/problem/27285) 

### 성능 요약

메모리: 224660 KB, 시간: 820 ms

### 분류

다이나믹 프로그래밍, 그리디 알고리즘, 누적 합

### 제출 일자

2026년 4월 1일 23:09:23

### 문제 설명

<p><em>Lord Pooty</em> has a $n$ by $m$ board of integers $A$ and would like to draw an L. However, he would like to maximise the sum of integers on the tiles covered by L. The L can be rotated in all 4 possible orientations such that the sides are parallel to the board. Each side of the L may not necessarily be drawn (a straight line is possible). Some examples of valid Ls are shown below:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/a3a1364a-e675-4008-a50f-8303b6e74c3e/-/preview/" style="width: 265px; height: 65px;"></p>

<p>Formally, you want to choose $3$ points, $(x_1, y_1)$, $(x_2, y_1)$ and $(x_1, y_2)$ (which may not necessarily be distinct) on the board $A$ such that</p>

<p>$$V = \sum_{i = \min{(x_1, x_2)}}^{\max{(x_1, x_2)}}{A_{i,y_1}} + \sum_{j = \min{(y_1, y_2)}}^{\max{(y_1, y_2)}}{A_{x_1,j}} - A_{x_1, y_1} $$</p>

<p>is maximised.</p>

### 입력 

 <p>Your program must read from standard input.</p>

<p>The input starts with a line with two integers $n$ and $m$ where $n$ and $m$ are height and width of the board. This is followed by $n$ lines of $m$ integers, representing the board.</p>

### 출력 

 <p>Your program must print to standard output.</p>

<p>The output should contain a single integer on a single line, the maximum $V$ possible.</p>

