# [Platinum V] Marinada - 25478 

[문제 링크](https://www.acmicpc.net/problem/25478) 

### 성능 요약

메모리: 287396 KB, 시간: 4708 ms

### 분류

너비 우선 탐색, 비트마스킹, 다이나믹 프로그래밍, 비트필드를 이용한 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 외판원 순회 문제

### 제출 일자

2026년 04월 19일 22:59:58

### 문제 설명

<p>Da bi spoznao kako se pravi marinada<sup>1</sup> za mladu janjetinu, Krešo mora proći kroz magični labirint. Labirint se sastoji od zidova, praznog prostora i namirnica od kojih se pravi marinada.</p>

<p>Točnije, labirint možemo prikazati kao matricu s $N \times M$ polja. Neka su polja zid (znak ‘<code>#</code>’), neka su prazan prostor (znak ‘<code>.</code>’), neka su namirnice (znak ‘<code>N</code>’), jedno polje je ulaz (znak ‘<code>U</code>’), a jedno izlaz (znak ‘<code>I</code>’). Polja na kojima su namirnice ima $K$. Krešo se po labirintu kreće od ulaza do izlaza, a jedina polja kojima se ne smije kretati su zidovi. Sva polja osim zidova smije posjetiti koliko god puta želi. U jednom koraku, Krešo s polja na kojem se nalazi može otići na neko polje njemu susjedno gore, dolje, lijevo ili desno.</p>

<p>Napiši program koji će za tako opisan labirint ispisati <strong>najmanji broj koraka</strong> potreban da Krešo dođe od ulaza do izlaza, a da pritom pokupi sve namirnice za slavnu marinadu.</p>

<p><em>I onda zapeče komad mlade janjetine za autore ovog zadatka.</em></p>

### 입력 

 <p>U prvom retku su prirodni brojevi $N$, $M$ ($1 ≤ N, M ≤ 1000$) i $K$ ($1 ≤ K ≤ 16$).</p>

<p>U sljedećih $N$ redaka je po $M$ znakova iz skupa {<code>#</code> <code>.</code> <code>N</code> <code>U</code> <code>I</code>}. Znak ‘<code>N</code>’ pojavit će se ukupno K puta.</p>

### 출력 

 <p>U prvi i jedini redak ispiši traženi najmanji broj koraka iz teksta zadatka.</p>

