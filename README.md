# Sublette

![](showcase/logo.png)

I've always loved coloring. Now it's time to design my color schemes.

## For Terminal (base)

Color          | Hex       | RGB                  | HSL                   |🎨
-------------- | --------- | -------------------- | --------------------- | --------------------------
Foreground     | `#ccced0` | `rgb(204, 206, 208)` | `hsl(210, 2%, 82%)`   | ![](plates/foreground.gif)
Background     | `#202535` | `rgb(32, 37, 53)`    | `hsl(226, 40%, 21%)`  | ![](plates/background.gif)
Black          | `#253045` | `rgb(37, 48, 69)`    | `hsl(219, 46%, 27%)`  | ![](plates/black.gif)
Red            | `#e57`    | `rgb(238, 85, 119)`  | `hsl(347, 64%, 93%)`  | ![](plates/red.gif)
Green          | `#5e7`    | `rgb(85, 238, 119)`  | `hsl(133, 64%, 93%)`  | ![](plates/green.gif)
Yellow         | `#fd8`    | `rgb(255, 221, 136)` | `hsl(43, 47%, 100%)`  | ![](plates/yellow.gif)
Blue           | `#58f`    | `rgb(85, 136, 255)`  | `hsl(222, 67%, 100%)` | ![](plates/blue.gif)
Magenta        | `#f7c`    | `rgb(255, 119, 204)` | `hsl(322, 53%, 100%)` | ![](plates/magenta.gif)
Cyan           | `#4ee`    | `rgb(68, 238, 238)`  | `hsl(180, 71%, 93%)`  | ![](plates/cyan.gif)
White          | `#f5f5da` | `rgb(245, 245, 218)` | `hsl(60, 11%, 96%)`   | ![](plates/white.gif)
Bright Black   | `#405570` | `rgb(64, 85, 112)`   | `hsl(214, 43%, 44%)`  | ![](plates/bright-black.gif)
Bright Red     | `#e65`    | `rgb(238, 102, 85)`  | `hsl(7, 64%, 93%)`    | ![](plates/bright-red.gif)
Bright Green   | `#9e7`    | `rgb(153, 238, 119)` | `hsl(103, 50%, 93%)`  | ![](plates/bright-green.gif)
Bright Yellow  | `#ff7`    | `rgb(255, 255, 119)` | `hsl(60, 53%, 100%)`  | ![](plates/bright-yellow.gif)
Bright Blue    | `#7bf`    | `rgb(119, 187, 255)` | `hsl(210, 53%, 100%)` | ![](plates/bright-blue.gif)
Bright Magenta | `#a8f`    | `rgb(170, 136, 255)` | `hsl(257, 47%, 100%)` | ![](plates/bright-magenta.gif)
Bright Cyan    | `#5fb`    | `rgb(85, 255, 187)`  | `hsl(156, 67%, 100%)` | ![](plates/bright-cyan.gif)
Bright White   | `#ffe`    | `rgb(255, 255, 238)` | `hsl(60, 7%, 100%)`   | ![](plates/bright-white.gif)

Use "Foreground" and "Background" for the cursor and cursor text respectively.

### Showcase

![](showcase/torchgpipe.py.png)

![](showcase/subl.ee.html.png)

![](showcase/subpptx.go.png)

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
Slides Foreground   | `#fff`    | `rgb(255, 255, 255)` | `hsl(0, 0%, 100%)`    | ![](plates/slides-foreground.gif)
Slides Foreground 2 | `#808080` | `rgb(128, 128, 128)` | `hsl(0, 0%, 50%)`     | ![](plates/slides-foreground-2.gif)
Slides Foreground 3 | `#404040` | `rgb(64, 64, 64)`    | `hsl(0, 0%, 25%)`     | ![](plates/slides-foreground-3.gif)
Slides Background   | `#000`    | `rgb(0, 0, 0)`       | `hsl(0, 0%, 0%)`      | ![](plates/slides-background.gif)
Slides Blue         | `#58f`    | `rgb(85, 136, 255)`  | `hsl(222, 67%, 100%)` | ![](plates/slides-blue.gif)
Slides Red          | `#e57`    | `rgb(238, 85, 119)`  | `hsl(347, 64%, 93%)`  | ![](plates/slides-red.gif)
Slides Green        | `#5d7`    | `rgb(85, 221, 119)`  | `hsl(135, 62%, 87%)`  | ![](plates/slides-green.gif)
Slides Yellow       | `#fc7`    | `rgb(255, 204, 119)` | `hsl(37, 53%, 100%)`  | ![](plates/slides-yellow.gif)
Slides Violet       | `#a8f`    | `rgb(170, 136, 255)` | `hsl(257, 47%, 100%)` | ![](plates/slides-violet.gif)
Slides Teal         | `#4dd`    | `rgb(68, 221, 221)`  | `hsl(180, 69%, 87%)`  | ![](plates/slides-teal.gif)

Use "Slides Foreground" for the link but with underline.

### Showcase

![](showcase/slides-title.png)

![](showcase/slides-people.png)

![](showcase/pie-chart.png)
