# Sublette

[![Sublette](https://img.shields.io/badge/theme-sublette-%2358f.svg?style=flat-square)](https://github.com/sublee/sublette)
[![Build Status](https://img.shields.io/travis/sublee/sublette.svg?style=flat-square)](https://travis-ci.org/sublee/sublette)

![](showcase/logo.png)

I've always loved coloring. Now it's time to design my color schemes.

## Tool Configurations

- [Hyper](configs/Hyper)
- [PuTTY](configs/PuTTY)
- [iTerm2](configs/iTerm2)
- [PyCharm or IntelliJ IDEA](configs/IntelliJ)
- [Slack](configs/Slack)
- [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=minmul117.sublette) by [Park GiSung](https://github.com/minmul117)

## For Terminal (base)

Color          | Hex       | RGB                  | HSL                   |🎨
-------------- | --------- | -------------------- | --------------------- | --------------------------
Foreground     | `#ccced0` | `rgb(204, 206, 208)` | `hsl(210, 2%, 82%)`   | ![](plates/foreground.png)
Background     | `#202535` | `rgb(32, 37, 53)`    | `hsl(226, 40%, 21%)`  | ![](plates/background.png)
Black          | `#253045` | `rgb(37, 48, 69)`    | `hsl(219, 46%, 27%)`  | ![](plates/black.png)
Red            | `#e57`    | `rgb(238, 85, 119)`  | `hsl(347, 64%, 93%)`  | ![](plates/red.png)
Green          | `#5e7`    | `rgb(85, 238, 119)`  | `hsl(133, 64%, 93%)`  | ![](plates/green.png)
Yellow         | `#fd8`    | `rgb(255, 221, 136)` | `hsl(43, 47%, 100%)`  | ![](plates/yellow.png)
Blue           | `#58f`    | `rgb(85, 136, 255)`  | `hsl(222, 67%, 100%)` | ![](plates/blue.png)
Magenta        | `#f7c`    | `rgb(255, 119, 204)` | `hsl(322, 53%, 100%)` | ![](plates/magenta.png)
Cyan           | `#4ee`    | `rgb(68, 238, 238)`  | `hsl(180, 71%, 93%)`  | ![](plates/cyan.png)
White          | `#f5f5da` | `rgb(245, 245, 218)` | `hsl(60, 11%, 96%)`   | ![](plates/white.png)
Bright Black   | `#405570` | `rgb(64, 85, 112)`   | `hsl(214, 43%, 44%)`  | ![](plates/bright-black.png)
Bright Red     | `#e65`    | `rgb(238, 102, 85)`  | `hsl(7, 64%, 93%)`    | ![](plates/bright-red.png)
Bright Green   | `#9e7`    | `rgb(153, 238, 119)` | `hsl(103, 50%, 93%)`  | ![](plates/bright-green.png)
Bright Yellow  | `#ff7`    | `rgb(255, 255, 119)` | `hsl(60, 53%, 100%)`  | ![](plates/bright-yellow.png)
Bright Blue    | `#7bf`    | `rgb(119, 187, 255)` | `hsl(210, 53%, 100%)` | ![](plates/bright-blue.png)
Bright Magenta | `#a8f`    | `rgb(170, 136, 255)` | `hsl(257, 47%, 100%)` | ![](plates/bright-magenta.png)
Bright Cyan    | `#5fb`    | `rgb(85, 255, 187)`  | `hsl(156, 67%, 100%)` | ![](plates/bright-cyan.png)
Bright White   | `#ffe`    | `rgb(255, 255, 238)` | `hsl(60, 7%, 100%)`   | ![](plates/bright-white.png)

Use "Foreground" and "Background" for the cursor and cursor text respectively.

### Showcase

<table>
  <tr>
    <td><img src="showcase/colors.ansi.png" /></td>
    <td><img src="showcase/subl.ee.html.png" /></td>
  </tr>
</table>
<table>
  <tr>
    <td><img src="showcase/gpustat.ansi.png" /></td>
    <td><img src="showcase/subpptx.go.png" /></td>
    <td><img src="showcase/torchgpipe.py.png" /></td>
  </tr>
</table>

## For IDEs

Usually, IDEs have configurations of highlight colors to indicate hints. The
highlight colors should be dimmer than the text colors. Here I define dim
colors for the use.

Color       | Hex       | RGB                  | HSL                   |🎨
----------- | --------- | -------------------- | --------------------- | -------------------
Dim         | `#96a0aa` | `rgb(150, 160, 170)` | `hsl(210, 12%, 67%)`  | ![](plates/dim.png)
Dim Red     | `#534`    | `rgb(85, 51, 68)`    | `hsl(330, 40%, 33%)`  | ![](plates/dim-red.png)
Dim Green   | `#454`    | `rgb(68, 85, 68)`    | `hsl(120, 20%, 33%)`  | ![](plates/dim-green.png)
Dim Yellow  | `#555045` | `rgb(85, 80, 69)`    | `hsl(41, 19%, 33%)`   | ![](plates/dim-yellow.png)
Dim Blue    | `#347`    | `rgb(51, 68, 119)`   | `hsl(225, 57%, 47%)`  | ![](plates/dim-blue.png)
Dim Magenta | `#546`    | `rgb(85, 68, 102)`   | `hsl(270, 33%, 40%)`  | ![](plates/dim-magenta.png)
Dim Cyan    | `#356`    | `rgb(51, 85, 102)`   | `hsl(200, 50%, 40%)`  | ![](plates/dim-cyan.png)

## For Slides

The purpose of a color scheme for Terminal and Slides is different. I need only
4 grayscale colors for text and background, and 6 hues--Blue, Red, Green,
Yellow, Violet, Teal--for clear semantics.

I prefer Black as the background color on projection screens to erase the
bezel. Also, I prefer White as the text color for the best readability.

The brightness of 6 hues should be normalized to be recognized at the same
level. If they are not, some hues look like more important than other hues. By
the way, some colors in the terminal color scheme are slightly brighter than
other colors. Here I adjust them for brightness normalization.

Color               | Hex       | RGB                  | HSL                   |🎨
------------------- | --------- | -------------------- | --------------------- | ---------------------------------
Slides Foreground   | `#fff`    | `rgb(255, 255, 255)` | `hsl(0, 0%, 100%)`    | ![](plates/slides-foreground.png)
Slides Foreground 2 | `#808080` | `rgb(128, 128, 128)` | `hsl(0, 0%, 50%)`     | ![](plates/slides-foreground-2.png)
Slides Foreground 3 | `#404040` | `rgb(64, 64, 64)`    | `hsl(0, 0%, 25%)`     | ![](plates/slides-foreground-3.png)
Slides Background   | `#000`    | `rgb(0, 0, 0)`       | `hsl(0, 0%, 0%)`      | ![](plates/slides-background.png)
Slides Blue         | `#58f`    | `rgb(85, 136, 255)`  | `hsl(222, 67%, 100%)` | ![](plates/slides-blue.png)
Slides Red          | `#e57`    | `rgb(238, 85, 119)`  | `hsl(347, 64%, 93%)`  | ![](plates/slides-red.png)
Slides Green        | `#5d7`    | `rgb(85, 221, 119)`  | `hsl(135, 62%, 87%)`  | ![](plates/slides-green.png)
Slides Yellow       | `#fc7`    | `rgb(255, 204, 119)` | `hsl(37, 53%, 100%)`  | ![](plates/slides-yellow.png)
Slides Violet       | `#a8f`    | `rgb(170, 136, 255)` | `hsl(257, 47%, 100%)` | ![](plates/slides-violet.png)
Slides Teal         | `#4dd`    | `rgb(68, 221, 221)`  | `hsl(180, 69%, 87%)`  | ![](plates/slides-teal.png)

Use "Slides Foreground" for the link but with underline.

### Showcase

<table>
  <tr>
    <td><img src="showcase/slides-title.png" /></td>
    <td><img src="showcase/slides-people.png" /></td>
    <td><img src="showcase/slides-pie-chart.png" /></td>
  </tr>
</table>
