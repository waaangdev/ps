# [Platinum V] Folding a Cube - 17876 

[문제 링크](https://www.acmicpc.net/problem/17876) 

### 성능 요약

메모리: 108384 KB, 시간: 104 ms

### 분류

구현, 기하학, 시뮬레이션, 3차원 기하학

### 제출 일자

2026년 04월 19일 22:59:58

### 문제 설명

<p>It is well known that a set of six unit squares that are attached together in a “cross” can be folded into a cube.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 579px; height: 164px;"></p>

<p>But what about other initial shapes? That is, given six unit squares that are attached together along some of their sides, can we form a unit cube by folding this arrangement?</p>

### 입력 

 <p>Input consists of 6 lines each containing 6 characters, describing the initial arrangement of unit squares. Each character is either a <code>.</code>, meaning it is empty, or a <code>#</code> meaning it is a unit square.</p>

<p>There are precisely 6 occurrences of <code>#</code> indicating the unit squares. These form a connected component, meaning it is possible to reach any <code>#</code> from any other <code>#</code> without touching a <code>.</code> by making only horizontal and vertical movements. Furthermore, there is no 2 × 2 subsquare consisting of only <code>#</code>. That is, the pattern</p>

<pre>##
##</pre>

<p>does not appear in the input.</p>

### 출력 

 <p>If you can fold the unit squares into a cube, display can fold. Otherwise display cannot fold.</p>

