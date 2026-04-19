# [Bronze II] Fading Wind - 27579 

[문제 링크](https://www.acmicpc.net/problem/27579) 

### 성능 요약

메모리: 109544 KB, 시간: 96 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2026년 04월 19일 22:59:58

### 문제 설명

<p>You're competing in an outdoor paper airplane flying contest, and you want to predict how far your paper airplane will fly. Your design has a fixed factor $k$, such that if the airplane's velocity is at least $k$, it will rise. If its velocity is less than $k$ it will descend.</p>

<p>Here is how your paper airplane will fly:</p>

<ul>
	<li>You start by throwing your paper airplane with a horizontal velocity of $v$ at a height of $h$. There is an external wind blowing with a strength of $s$.</li>
	<li>While $h > 0$, repeat the following sequence:
	<ul>
		<li>Increase $v$ by $s$. Then, decrease $v$ by $\max(1, \left\lfloor \frac{v}{10} \right\rfloor)$. Note that $\left\lfloor \frac{v}{10} \right\rfloor$ is the value of $\frac{v}{10}$, rounded down to the nearest integer if it is not an integer.</li>
		<li>If $v \ge k$, increase $h$ by one.</li>
		<li>If $0 < v < k$, decrease $h$ by one. If $h$ is zero after the decrease, set $v$ to zero.</li>
		<li>If $v \le 0$, set $h$ to zero and $v$ to zero.</li>
		<li>Your airplane now travels horizontally by $v$ units.</li>
		<li>If $s > 0$,    decrease it by $1$.</li>
	</ul>
	</li>
</ul>

<p>Compute how far the paper airplane travels horizontally.</p>

### 입력 

 <p>The single line of input contains four integers $h$, $k$, $v$, and $s$ $(1 \le h, k, v, s \le 10^3)$, where $h$ is your starting height, $k$ is your fixed factor, $v$ is your starting velocity, and $s$ is the strength of the wind.</p>

### 출력 

 <p>Output a single integer, which is the distance your airplane travels horizontally. It can be shown that this distance is always an integer.</p>

