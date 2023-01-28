# 功能测试

$$
\text{设置快捷键命令}
\newcommand{\D}{\mathrm{d}}
\newcommand{\x}{\mathbf{x}}
\newcommand{\xt}{\mathbf{x}^{\mathsf{T}}}
\newcommand{\T}{{\mathsf{T}}}
\newcommand{\abf}{\mathbf{a}}
\newcommand{\abft}{\mathbf{a}^{\mathsf{T}}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\E}{\mathrm{e}}
\newcommand{\F}{\mathbb{F}}
\newcommand{\X}{\mathbf{X}}
\newcommand{\Y}{\mathbf{Y}}
\newcommand{\y}{\mathbf{y}}
\renewcommand{\l}{\mathcal{l}}
\newcommand{\z}{\mathbf{z}}
\newcommand{\Z}{\mathbf{Z}}
\newcommand{\bfi}{\mathbf{i}}
\newcommand{\bftheta}{\bm{\theta}}
\newcommand{\rmvec}{\mathrm{vec}}
\newcommand{\argmin}{\mathop{\arg\min}}
\newcommand{\argmax}{\mathop{\arg\max}}
\newcommand{\f}{\mathbf{f}}
\newcommand{\U}{\mathbf{u}}
\newcommand{\D}{\mathrm{d}}
\newcommand{\MCG}{\mathcal{G}}
\newcommand{\MCH}{\mathcal{H}}
\newcommand{\MCF}{\mathcal{F}}
\newcommand{\M}{\mathcal{M}}
\newcommand{\W}{\mathbf{W}}
\newcommand{\bfb}{\mathbf{b}}
\newcommand{\MCB}{\mathcal{B}}
\newcommand{\MCT}{\mathcal{T}}
\newcommand{\LL}{\mathcal{L}}
\newcommand{\nullspace}{\mathrm{null}}
\newcommand{\tr}{\mathrm{tr}}
\newcommand{\range}{\mathrm{range}}
\newcommand{\listofalgorithmes}{\tocfile{\listalgorithmcfname}{loa}}
$$

??? note "快捷键设置命令"
    === "符号"
        ``` tex title="config.tex" linenums="1"
        \newcommand{\inner}[2]{{\langle #1,#2\rangle}}
        \newcommand{\D}{\mathrm{d}}
        \newcommand{\x}{\mathbf{x}}
        \newcommand{\xt}{\mathbf{x}^{\mathsf{T}}}
        \newcommand{\T}{{\mathsf{T}}}
        \newcommand{\abf}{\mathbf{a}}
        \newcommand{\abft}{\mathbf{a}^{\mathsf{T}}}
        \newcommand{\R}{\mathbb{R}}
        \newcommand{\E}{\mathrm{e}}
        \newcommand{\F}{\mathbb{F}}
        \newcommand{\X}{\mathbf{X}}
        \newcommand{\Y}{\mathbf{Y}}
        \newcommand{\y}{\mathbf{y}}
        \renewcommand{\l}{\mathcal{l}}
        \newcommand{\z}{\mathbf{z}}
        \newcommand{\Z}{\mathbf{Z}}
        \newcommand{\bfi}{\mathbf{i}}
        \newcommand{\bftheta}{\bm{\theta}}
        \newcommand{\rmvec}{\mathrm{vec}}
        \newcommand{\argmin}{\mathop{\arg\min}}
        \newcommand{\argmax}{\mathop{\arg\max}}
        \newcommand{\f}{\mathbf{f}}
        \newcommand{\U}{\mathbf{u}}
        \newcommand{\D}{\mathrm{d}}
        \newcommand{\MCG}{\mathcal{G}}
        \newcommand{\MCH}{\mathcal{H}}
        \newcommand{\MCF}{\mathcal{F}}
        \newcommand{\M}{\mathcal{M}}
        \newcommand{\W}{\mathbf{W}}
        \newcommand{\bfb}{\mathbf{b}}
        \newcommand{\MCB}{\mathcal{B}}
        \newcommand{\MCT}{\mathcal{T}}
        \newcommand{\LL}{\mathcal{L}}
        \newcommand{\nullspace}{\mathrm{null}}
        \newcommand{\tr}{\mathrm{tr}}
        \newcommand{\range}{\mathrm{range}}
        \newcommand{\listofalgorithmes}{\tocfile{\listalgorithmcfname}{loa}}
        ```
    === "公式"
        ``` tex title="config.tex" linenums="1"
        \definecolor{codegreen}{rgb}{0,0.6,0}
        ```
[https://squidfunk.github.io/mkdocs-material/reference/buttons/#usage](https://squidfunk.github.io/mkdocs-material/reference/buttons/#usage)

!!! danger "test"
    === "OLS"
        $$
        (\X^\prime \X)^{-1} \X^\prime \Y
        $$
    === "Black-Scholes"
        $$
        \begin{cases}
            rf = \frac{\partial f}{\partial t} + r x \frac{\partial f}{\partial x} + \frac{1}{2} \sigma^2 x^2 \frac{\partial^2 f}{\partial x^2}\\
            f(T,x) = (x-K)^{+}
        \end{cases}
        $$
    === "Eular Equation"
        $$
        \E^z = \sum_{k=0}^{+\infty} \frac{z^k}{k!}, \quad \E^{a+ib} = \E^a(\cos{b} + i\sin{b})
        $$
    === "Riesz  Representation Theorem"
        > Suppose $\varphi$ is a **bounded** linear functional on a Hilbert sapce V. Then there exists
        > a unique $h \in V$ such that
        > $$ \varphi(f) = \langle f, h \rangle$$
        > for all $f \in V$. Furthermore, $\Vert \varphi \Vert = \Vert h \Vert$.


## 汇总

!!! note "Theorem"
    this is a tip

!!! abstract "Theorem"
    this is a tip

??? note "theorem"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

> 可以使用attention, caution, danger, error, hint, important, note,
> tip, and warning。


``` py
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```

- 23
- 123

| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |

## Annotations

这个功能似乎和mermaid冲突了
Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.
{ .annotate }

1.  :man_raising_hand: I'm an annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be expressed in Markdown.


## Buttons

[Subscribe to our newsletter](#){ .md-button }

## Code Blocks

加title, 行数, highlight的行数

``` py title="config.py" linenums="1"  hl_lines="2 3"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

## Content tabs

核心语法非常简单, 相当于利用"==="作为选择工具, 但需要注意缩进问题

=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
    printf("Hello world!\n");
    return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
    std::cout << "Hello world!" << std::endl;
    return 0;
    }
    ```

=== "python"

    ``` py
    def main{
        print("Hello World!")
        return 0
    }
    ```

当然还可以用来嵌入其它结构

=== "Unordered list"
    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"
    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

## Data tables

还是有bug

| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |

## Footnotes

用不了
Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]

## Formatting

Text can be {--deleted--} and replacement text {++added++}. This can also be
combined into {~~one~>a single~~} operation. {==Highlighting==} is also
possible {>>and comments can be added inline<<}.

{==

Formatting can also be applied to blocks by putting the opening and closing
tags on separate lines and adding new lines between the tags and the content.

==}

++ctrl+alt+del++

## Grids

还是用不了

<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>

## Images

<figure markdown>
  ![Image title](https://dummyimage.com/600x400/){ width="300" }
  <figcaption>Image caption</figcaption>
</figure>

## Lists

<!-- - [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
- [12 ] Vestibulum convallis sit amet nisi a tincidunt
    * [x] In hac habitasse platea dictumst
    * [x] In scelerisque nibh non dolor mollis congue sed et metus
    * [ ] Praesent sed risus massa
- [12 ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque -->
