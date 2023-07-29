本題解轉自本人之洛谷博客，並對其規範性及可讀性作出了一些修改。

題解旨在詳細講解有關題中幾何性質的證明過程。

## 題目大意

平面上有$N$個圓柱形的大釘子，半徑都爲$R$，所有釘子組成一個**凸多邊形**。現在要求用一條繩子把這些釘子圍起來，繩子直徑忽略不計，求繩子的長度。



## 提示

本題比較著重對幾何性質的挖掘，而編程難度相對較低。故在閱讀題解前，不妨再花十分鐘作圖（或使用下方圖示）考慮線段與角度間的幾何關係，化繁為簡，逐一觀察。



### 證明

![](C:\Users\lenovo\Desktop\Programming\CS50-Web%20Programming%20with%20Python%20and%20JavaScript\Project\blog\post\static\blog\test.jpg)

## 結論

繩子的長度為**凸多邊形的周長**加上**一個釘子的周長**。

#### 1. 考慮式中凸多邊形周長的部分

需要證明：$O_1O_2=AB$。即說明，把 $O_1O_2$ 看作是原來 $N$ 邊形（此時釘子半徑無窮小）的一條邊，那麼 $AB$ 是由 $O_1O_2$ 沿兩圓半徑平移所得。

由題意可知，$AB$ 是 $\bigodot O_1, \bigodot O_2$ 的公切線。因為繩子在圓上繃緊，於兩圓之間分別只有一個交點，可判斷為與圓相切。

故此，$O_1\perp A$, $O_2 \perp B$，可立即由同位角相等推出 $O_1A\parallel O_2B$。

由於我們已知所有釘子半徑相同為 $R$，故我們有 $O_1A=O_2B$。

故此，$O_1 O_2 BA$ 是長方形，可得對邊 $O_1O_2$ 與 $AB$ 平行且相等。



#### 2. 考慮式中釘子（一個完整的圓）周長的部分

我們要求出關於繩子黏連圓弧 $\overset{\frown}{EF}$ 長度的式子。基本上，就是要找出每個圓弧佔了圓周長的份額比例多少。

繼而關注 $\angle CO_1A$。由於我們發現四邊形 $O_1 C F A$中有兩個角為直角，所以我們考慮 $\angle AFC$。注意到 $\angle AFC=\angle O_2O_1O_3$。

一個嚴謹的證明可以如此進行：

> 延長 $O_1O_2$ 交於 $DF$，由平行的性質將同位角轉移到 $O_1O_2$ 所在的直線之上（即 $O_1O_2$ 與 $DF$ 所形成之夾角）。
> 
> 連接 $O_2O_3$，再使用同位角的性質說明 $\angle O_2O_1O_3 = \angle BFD (\angle AFC)$。

一個簡而有力的說明可以繞過繁重的證明：

> 由於多邊形各邊均向外平移 $R$ 個單位，故顯然是由中心向外放大常數倍。
> 
> 故此放大後的多邊形與原多邊形相似，多邊形內角不變。

如此便有一個對多邊形內角對應關係的觀察。

所有形如 $\angle AFC$ 的夾角，它們都分別對應一個 $N$ 邊形的內角 $\theta_i$。

因此，我們考慮多邊形內角和得到關係 $\sum\limits_{i=1}^n \theta_i = (n-2)\times 180^{\circ}$。

此外，所有形如 $\angle AO_1C$ 的夾角 $\varphi_i$ 之和，為 $\sum\limits_{i=1}^{n} ( 360^{\circ}-90^{\circ}-90^{\circ}-\theta_i)$。

簡化式子，首先將 $n$ 個 $180^{\circ}$ 從式中脫出，然後只需應用多邊形內角和關係減去 $(n-2)$ 個 $180^{\circ}$。

故此，圓弧組成了一個整圓，我們將圓弧這一部分加入答案中。



## 代碼

```cpp
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
using namespace std;
const double pi=3.1415926535;
int n;
struct pos
{
    double x,y;
}coor[101];
double ans,r;
double len(pos a,pos b)
{
    return sqrt(pow(a.x-b.x,2)+pow(b.y-a.y,2));
}
int main(void)
{
    scanf("%d%d",&n,&r);
    for (int i=1;i<=n;i++)
        scanf("%lf%lf",&coor[i].x,&coor[i].y);
    ans+=2*r*pi;
    for (int i=1;i<n;i++)
        ans+=len(coor[i],coor[i+1]);
    ans+=len(coor[1],coor[n]);
    printf("%.2lf",ans);
}
```


