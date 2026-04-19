# [Platinum I] Word - 6345 

[문제 링크](https://www.acmicpc.net/problem/6345) 

### 성능 요약

메모리: 2332 KB, 시간: 36 ms

### 분류

분류 없음

### 제출 일자

2026년 04월 19일 22:59:58

### 문제 설명

<p>Dr. R. E. Wright's class was studying modified L-Systems. Let us explain necessary details. As a model let us have words of length n over a two letter alphabet {a, b}. The words are cyclic, this means we can write one word in any of n forms we receive by cyclic shift, whereby the first and the last letters in the word are considered to be neighbours.</p>

<p>Rewriting rules rewrite a letter at a position i, depending on letters at the positions i - 2, i, i+1. We rewrite all letters of the word in one step. When we have a given starting word and a set of rewriting rules a natural question is: how does the word look after s rewriting steps?</p>

<p>Help Dr. R. E. Wright and write a program which solves this task.</p>

### 입력 

 <p>There are several blocks in the input, each describing one system. There is an integer number n, 2 < n < 16 the length of the input word in the first line. There is a word in the next line. The word contains only lowercase letters <code>a</code> and <code>b</code>. There are four characters c<sub>1</sub>c<sub>2</sub>c<sub>3</sub>c<sub>4</sub> in the next eight lines. Each quadruple represents one rewriting rule with the following meaning: when the letter at the position i - 2 is c<sub>1</sub> and the letter at the position i is c<sub>2</sub> and the letter at the position i + 1 is c<sub>3</sub> then the letter at the position i after rewriting will be c<sub>4</sub>. Rewriting rules are correct and complete. There is an integer number s, 0 ≤ s ≤ 2000000000, in the last line of the block.</p>

### 출력 

 <p>There is one line corresponding to each block of the input. The line contains a word which we receive after s rewriting steps from the corresponding starting word using given rewriting rules. As we mentioned above, the word can be written in any of n cyclic shifted forms. The output file contains the lexicographically smallest word, assuming that a < b.</p>

