# [Silver II] Happy Hookup - 35091 

[문제 링크](https://www.acmicpc.net/problem/35091) 

### 성능 요약

메모리: 129400 KB, 시간: 236 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

### 제출 일자

2026년 04월 19일 22:59:58

### 문제 설명

<p>It has happened! You found a match! Excitedly, your match Hannah and you have decided to have a morning stroll together. Since the two of you live in different cities, you decide to meetup at a train station.</p>

<p>Getting to your respective cities' train station is no problem. However, the ongoing renovations of the national train network heavily impact the available connections. Some of them are not available at all, and some others are only one-way. This makes it uncertain whether you can meet up at all.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 300px; height: 127px;"></p>

<p style="text-align: center;">Figure H.1: Visualization of the third sample. Hannah starts from station $4$, and you start from station $1$. You can both reach station $3$ for your meet-up.</p>

<p>You have found a list of the available train connections online. A train station is suitable for your meet-up if both Hannah and you can reach it. Determine whether there is a suitable train station or whether it is necessary to move the morning stroll to another day.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
<li>One line with two integers $n$ and $m$ ($2 \leq n \leq 10^5$, $0 \leq m \leq 10^5$), the number of train stations and train connections, respectively.</li>
<li>$m$ lines, each with two integers $x$ and $y$ ($1 \leq x, y \leq n$, $x \neq y$), denoting a direct train connection from train station $x$ to train station $y$.</li>
<li>One line with two integers $a$ and $b$ ($1 \leq a,b \leq n$, $a \neq b$), the train stations you and Hannah start from, respectively.</li>
</ul>

<p>It is guaranteed that no train connection is listed multiple times.</p>

### 출력 

 <p>If no suitable train station exists, output "<code>no</code>".</p>

<p>Otherwise, output "<code>yes</code>", followed by the train station. If there are multiple valid solutions, you may output any one of them.</p>

