# [Platinum V] Combination Lock - 31591 

[문제 링크](https://www.acmicpc.net/problem/31591) 

### 성능 요약

메모리: 130380 KB, 시간: 432 ms

### 분류

수학, 다이나믹 프로그래밍, 정수론, 비트마스킹, 소수 판정, 비트필드를 이용한 다이나믹 프로그래밍, 역추적

### 제출 일자

2026년 04월 19일 22:59:58

### 문제 설명

<p>Your house is protected by a combination lock containing $n$ rotating discs, numbered from $1$ to $n$. On a typical combination lock, each rotating disc has $10$ symbols, represented by integers between $0$ to $9$, inclusive. Since you are a mathematician, your combination lock is not typical. Instead, each rotating disc on your combination lock may have a different number of symbols. In particular, rotating disc $i$ has $b_i - a_i + 1$ symbols, represented by integers between $a_i$ to $b_i$, inclusive.</p>

<p>The combination lock is unlocked when each rotating disc displays one integer, and any pair of two integers displayed by the rotating disc are coprime. Two integers are coprime if they do not have any common positive factors other than $1$.</p>

<p>You want to unlock the combination lock, so you want to determine what integer to be displayed on each combination lock to satisfy the requirement above. It is possible that your combination lock was sabotaged when you were gone so it might be impossible to unlock your combination lock.</p>

### 입력 

 <p>The first line of input contains one integer $n$ ($2 ≤ n ≤ 50$). Each of the next $n$ lines contains two integers. The $i$-th line contains $a_i$ and $b_i$ ($1 ≤ a_i ≤ b_i ≤ 50$).</p>

### 출력 

 <p>Output one line containing $n$ integers, where the $i$-th integer represents the integer to be displayed by rotating disc $i$ to unlock the combination lock. If there are multiple solutions, you can output any of them. If there is no solution, output just the integer <code>-1</code>.</p>

