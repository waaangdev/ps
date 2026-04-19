# [Diamond V] Pixelated Circle - 25291 

[문제 링크](https://www.acmicpc.net/problem/25291) 

### 성능 요약

메모리: 113088 KB, 시간: 112 ms

### 분류

기하학, 수학, 런타임 전의 전처리

### 제출 일자

2026년 04월 19일 22:59:58

### 문제 설명

<p>Typical computer images are matrices of pixels, with each pixel being a small square of a specific color. Drawing lines that are not perfectly parallel to the axes of the pixel matrix results in imperfections. Drawing circles is an extreme example where those imperfections arise.</p>

<p>Suppose we have a picture consisting of $2\mathbf{R}+1$ by $2\mathbf{R}+1$ pixels, and we number the rows and columns of pixels between $-\mathbf{R}$ and $\mathbf{R}$, such that the center pixel is at row $0$ and column $0$. Initially, all pixels are white. Then, a circle of radius $\mathbf{R}$ and centered in the picture can be drawn in black by the following pseudocode, where <code>set_pixel_to_black(x, y)</code> makes the pixel at row $x$ and column $y$ be colored black.</p>

<pre>draw_circle_perimeter(R):
  for x between -R and R, inclusive {
    y = round(sqrt(R * R - x * x))   # round to nearest integer, breaking ties towards zero
    set_pixel_to_black(x, y)
    set_pixel_to_black(x, -y)
    set_pixel_to_black(y, x)
    set_pixel_to_black(-y, x)
  }
</pre>

<p>Notice that some pixels may be set to black more than once by the code, but the operation is idempotent (that is, calling <code>set_pixel_to_black</code> on a pixel that is already black changes nothing).</p>

<p>The following is pseudocode for a function to draw a filled circle (starting from an all-white picture).</p>

<pre>draw_circle_filled(R):
  for x between -R and R, inclusive {
    for y between -R and R, inclusive {
      if round(sqrt(x * x + y * y)) ≤ R:
        set_pixel_to_black(x, y)
    }
  }
</pre>

<p>And finally, the following is pseudocode to incorrectly draw a filled circle:</p>

<pre>draw_circle_filled_wrong(R):
  for r between 0 and R, inclusive {
    draw_circle_perimeter(r)
  }
</pre>

<p>Given $\mathbf{R}$, calculate the number of pixels that would have different colors between a picture in which <code>draw_circle_filled</code>($\mathbf{R}$) is called and another one in which <code>draw_circle_filled_wrong</code>($\mathbf{R}$) is called.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, $\mathbf{T}$. $\mathbf{T}$ test cases follow. Each test case is described in a single line containing a single integer $\mathbf{R}$, the radius of the circle to draw.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where $x$ is the test case number (starting from 1) and $y$ is the number of pixels that would have different colors between a picture in which <code>draw_circle_filled</code>($\mathbf{R}$) is called and another one in which <code>draw_circle_filled_wrong</code>($\mathbf{R}$) is called.</p>

