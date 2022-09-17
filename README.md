<h1 align="center">Multiple Linear Regression From Scratch</h1>


<br/>
<div align="center">
  <a href="https://i.imgur.com/tDee6dv.png">
    <img src="https://i.imgur.com/tDee6dv.png" alt="Logo" >
  </a>

<br/>
</div>

## Details

* A very simple Multiple Linear Regression (MLR) algorithm from Scratch. I did not use Scikit-Learn or any similar libraries. <br/> The main point from this is to understand how the linear and multivariable regression work in thr backgroud. Understand the math and the concept of it is much important using a library with 2 lines to train the model! At least for a beginner like me :) 

* I have used dataset found on __Kaggle__ or __Github__, it is very simple! 2 features with 1 output as it is a house prediction problem. The concept remains the same. However, with diferent features' number you will have to edit __Equation__ part in the code but the rest are the same. I used __Mean Square Error__ __(MSE)__. Also,  I uploaded the 3 graphs, the first Feature with the output, the second feature with the output ,and finally, the loss function or the error vs iterations.

* When you change your dataset and change the number of iterations and alpha value you might find the output as NaN or an Overflow Error. To solve this, do a __Normalization__ for the dataset or multiply the dataset by 0.01 for example (This depends on the dataset). However, this may solve the problem.

* For all the equation I used, why it is like this? How could you derive them also? Please check the References.

<br/>

## Figures
* [Figure 1 - X1 vs. Y Fit Line - High Quality](https://i.imgur.com/yQJNlTT.png) 
* [Figure 2 - X2 vs. Y Fit Line -  High Quality](https://i.imgur.com/xftAjMn.png) 
* [Figure 3 - Error vs. Number of Iterations - High Quality](https://i.imgur.com/yhKwZuq.png) 

 <div align="center">
 
  <a href="https://i.imgur.com/yQJNlTT.png">
    <img src="https://i.imgur.com/yQJNlTT.png" alt="Figure 1" width="488" height="500">
    
  <a href="https://i.imgur.com/xftAjMn.png">
    <img src="https://i.imgur.com/xftAjMn.png" alt="Figure 1" width="488" height="500">
    
  <a href="https://i.imgur.com/yhKwZuq.png">
    <img src="https://i.imgur.com/yhKwZuq.png" alt="Figure 1" width="488" height="500">
  </a>
</div>


## Tech Stack

* **Python:** Version 3.10

* **Spyder IDE**: Version 5.3.2

* **Pandas**: Version 1.4.3

* **Matplotlib**: Version 3.5.3


## Contributing
Contributions are what makes the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Do not forget to give the project a star! Thanks again!

<br/>

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


## References

*  This is important [Article](https://www.analyticsvidhya.com/blog/2021/04/gradient-descent-in-linear-regression/), as it illustrates how to deal the partial dervatives.

*  Very explained resource on which I depended a lot to develop this algorithm [Helpful Video](https://www.youtube.com/watch?v=V4H8M_78u80&list=PL6-3IRz2XF5UJE2PbY7UU4SHi7UpV1mXo&index=19)

## Contacts
* Via Email : Mahmoud.Nady@Ejust.edu.eg
* [Via FaceBook]( https://www.facebook.com/MND919/ ).







