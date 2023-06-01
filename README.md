# ChairAngles
A few calculations for a folding chair project.

**Language: Python**

**Start: 2023**

## Why
I found a [woodworking project](https://canadianwoodworking.com/project/folding-chair/) for a folding chair. The chair is composed by two pieces:

![chair](/images/chair1.jpg)
![chair](/images/chair2.jpg)

I made a few calculations to adjust the angle between the two pieces, and wrote a python program to display a schematic of the chair.

## Calculations
To explain the calculations it's necessary to define a few variables. First of all, the name of the four key blocks involved in red:

![chair](/images/drawing2.jpg)

Each block is characterized by a key length with the same name:

![chair](/images/drawing3.jpg)

Other relevant measurements:

![chair](/images/drawing4.jpg)

Keeping in mind that the block l and m have the same depth h, and the blocks b, c, d have the same dimension e, f.

We define also a few variables zooming in where the block _l_ and _m_ meet:

![chair](/images/drawing5.jpg)

$$t = 2 \cdot f + h$$

$$u = m - d - 2 \cdot e - b$$

$$u = w + s$$

### Finding &theta;
&theta; can be defined with two formulas:

$$cos \theta = \frac{h}{s}$$

$$tan \theta = \frac{w}{t} = \frac{u - s}{t}$$

To solve for &theta; we must remember a property of the tangent:

$$tan \theta = \frac{\sqrt{1-cos^2 \theta}}{\cos \theta}$$

With this we can write:

$$\frac{\sqrt{1-cos^2 \theta}}{\cos \theta} = \frac{1}{t} \cdot (u - \frac{h}{cos \theta})$$

$$\sqrt{1-cos^2 \theta} = \frac{u}{t} \cdot \cos \theta - \frac{h}{t}$$

$$1-cos^2 \theta = \frac{u^2}{t^2} \cdot \cos^2 \theta + \frac{h^2}{t^2} - 2 \cdot \frac{u}{t} \cdot \cos \theta \cdot \frac{h}{t}$$

$$\frac{u^2}{t^2} \cdot \cos^2 \theta + cos^2 \theta - 2 \cdot \frac{u \cdot h}{t^2} \cdot \cos \theta + \frac{h^2}{t^2} - 1 = 0$$

$$(\frac{u^2}{t^2} + 1) \cdot \cos^2 \theta - 2 \cdot \frac{u \cdot h}{t^2} \cdot \cos \theta + \frac{h^2}{t^2} - 1 = 0$$

We can now solve this quadratic equation for _cos_ &theta;:

$$\cos \theta = \frac{2 \cdot \frac{u \cdot h}{t^2} \pm \sqrt{4 \cdot \frac{u^2 \cdot h^2}{t^4} - 4 \cdot (\frac{u^2}{t^2} + 1) \cdot (\frac{h^2}{t^2} - 1)}}{2 \cdot (\frac{u^2}{t^2} + 1)}$$

### Finding &gamma;, _m1_ and _l1_
With this we can calculate &gamma;, m1 and l1:

$$\gamma = \theta + 90°$$

$$m_1 = b + e + (f + h) \cdot tan \theta$$

$$l_1 = l - e - c - \frac{h}{\cos \theta} + h \cdot \tan \theta$$

### Finding &alpha;, &beta; and _a_
Finally, we can calculate &alpha; and &beta; by first calculating _a_ using the [law of cosines](https://en.wikipedia.org/wiki/Law_of_cosines):

$$a = \sqrt{l_1^2 + m_1^2 - 2 \cdot l_1 \cdot m_1 \cdot \cos \gamma}$$

$$\alpha = \arcsin \frac{m_1 \cdot \sin \gamma}{a}$$

$$\beta = 180° - \gamma - \alpha$$