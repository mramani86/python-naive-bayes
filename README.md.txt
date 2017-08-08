DELTA = 0.01 (smoothing factor)
---


Assumption: Prior probabilities for low, med, high are same
---



How to run the code?
1. accuracies
Copy paste the accuracy.txt code in the main area of naive_bayes_final.py to get the accuracy of train and test data
---


2. probabilities
To get probability of a class given attributes copy paste probabilities.txt code into main area and run

Here, you can change input vector in order to change the attributes you want.

For e.g. if you want P(LOW|(EMOR, NON, NORTH, RES, 2)) theny chnage class_name and input_vector as below
input_vector = ["EMOR","NON", "NORTH", "RES", "2", "?"]
class_name = "LOW"

For e.g. if you want P(LOW|(EMOR, NORTH)) theny chnage class_name and input_vector as below (note the question marks)
input_vector = ["EMOR","?", "NORTH", "?", "?", "?"]
class_name = "LOW"

For e.g. if you want P(MED|(EMOR, RES, 2)) theny chnage class_name and input_vector as below (note the question marks)
input_vector = ["EMOR","?", "?", "RES", "2", "?"]
class_name = "MED"
---