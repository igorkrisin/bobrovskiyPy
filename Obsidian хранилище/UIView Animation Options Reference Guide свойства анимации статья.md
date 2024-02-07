In Swift block-based animations give developers a great platform to create functional and effective animations. For example, using animate(withDuration:delay:options:animations:completion) gives developers the ability to craft a great user experience with easy built in tools. There is bound to be one animation in the provided animation options that will satisfy a developer, however there are many options to choose from, and it can be a time consuming to build your project every time you change an animation option while looking for the right fit. I found myself a little overwhelmed by the choices so I made a reference guide that illustrates the effects of all the provided options. While this isn’t an exhaustive list it can help save time by narrowing down the animation options to choose from, and it also gives a good frame of reference for someone with regards to which animations do what, making us all a little more efficient.

These animation options can be used for a wide array of different movements. This guide isn’t meant to show each possible scenario for a given animation. Rather, it is meant to give a baseline understanding of the animation option, so you can understand how it would apply to your given use case. For the first portion of this guide I use the example of a block moving across the screen. I constrained the box to start on the left side of the screen and move across to the right side. Below is the code for the animation I began with.

UIView.animate(withDuration: 3.0, delay: 0.0, options: [], animations: {self.customBoxLeftConstraint.isActive = falseself.customBoxRightConstraint = self.customBox.rightAnchor.constraint(equalTo: self.view.rightAnchor)self.customBoxRightConstraint.isActive = trueself.view.layoutIfNeeded()}, completion: nil)

As a baseline this is what my project looked like with no animations included (so options section looked like: options: []).

![](https://miro.medium.com/v2/resize:fit:960/1*_OCZFZKlib58D_S8Y7YGnQ.gif)

# **.autoreverse**

Combined with .repeat this will loop the animation indefinitely. Just using autoreverse will do the initial animation but in reverse, and then snap back to the end position of the initial animation. For the options section of the animation block the code looked like this:

![](https://miro.medium.com/v2/resize:fit:1208/1*wk5cbw7rkKl2DFDhQt6xHw.png)

And this was the result.

![](https://miro.medium.com/v2/resize:fit:960/1*9Sbq3vfHcdvpd8WcY0HOfQ.gif)

# **.curveEaseIn**

It may be hard to see in this one but when you compare it to the next .gif it is more obvious. This one is moving slowly at first and then speeds up towards the end of the animation.

![](https://miro.medium.com/v2/resize:fit:960/1*z5To3UtFfrk-Kf-FJN_iDw.gif)

# **.curveEaseOut**

Much easier to see than .curveEaseOut this option begins with the animation moving quickly and then slows down at the end.

![](https://miro.medium.com/v2/resize:fit:960/1*uBeES2RitlbQf_uQihyS8w.gif)

# **.curveEaseInOut**

Moves slowly at first, speeds up over middle portion, then slows down at the end of the animation.

![](https://miro.medium.com/v2/resize:fit:960/1*BDyg6HdtXzHTJyZem8iPSw.gif)

# **.curveLinear**

Animation occurs evenly across the whole duration.

![](https://miro.medium.com/v2/resize:fit:960/1*gNhE3KV6X0UXvfe9iiN8tg.gif)

# **.repeat**

Simply repeats the animation, which means it is sent back to the starting position of the animation.

![](https://miro.medium.com/v2/resize:fit:960/1*ysQe5TjOueOYXSdgaxYowA.gif)

# **.autoreverse with .repeat**

Autoreverse sends the animation back to its original position, .repeat then repeats that process so it looks like the image is moving in an infinite loop.

![](https://miro.medium.com/v2/resize:fit:960/1*ThDhgTUXIblXtKjhZv1nTg.gif)

For the rest of the animations I switched from using a block to transitioning animations on a text field. I did this to better illustrate the properties of these options, but like I previously stated the purpose is to show what these animation options can do for your project.

The following animations were triggered when the user left a textfield. The animation changes the color of the text that was input, and the type of animation determines how that is displayed. I slowed the duration down to an excruciating four seconds so all the details of the animation could be seen. This was the code:

For this example I started off using .transitionCrossDissolve as you can see in the options portion of the code block. For reference this is what it looks like with no animation options that changes how the animation looks.

# **No animation options**

![](https://miro.medium.com/v2/resize:fit:960/1*2Q5CdWAyBOtm7S8ifL9hvA.gif)

Very boring transition

The animation simply switches color. Thankfully thats not our last resort.

# **.transitionCrossDissolve**

![](https://miro.medium.com/v2/resize:fit:960/1*LH2bitXh8fdnCN2hfdZ7Hw.gif)

A slow transitioned fade.

# **.transitionCurlDown**

![](https://miro.medium.com/v2/resize:fit:960/1*bRm_jTviPldghcpiTbPE1g.gif)

# **.transitionCurlUp**

![](https://miro.medium.com/v2/resize:fit:960/1*hB0wsJHpfVaDtK_i9dpzRQ.gif)

# **.transitionFlipFromBottom**

![](https://miro.medium.com/v2/resize:fit:960/1*5hExMiWwc5cqMojjeyMWQQ.gif)

# **.transitionFlipFromLeft**

![](https://miro.medium.com/v2/resize:fit:960/1*f1U_Z3gY2BFseYFLa88qDg.gif)

# **.transitionFlipFromRight**

![](https://miro.medium.com/v2/resize:fit:960/1*Dp_2p0Nwl7uhfYDWApe43g.gif)

# **.transitionFlipFromTop**

![](https://miro.medium.com/v2/resize:fit:960/1*rmT-9ObHphExJAc2iLsHzQ.gif)

And that wraps up the animation options! Thanks to GIPHY for the great gif-making tool. Happy animating!

![](https://miro.medium.com/v2/resize:fit:1400/1*mCszKTe-ioyBuEPweNxz-A.gif)


[[Создание Анимаций Animation]] 