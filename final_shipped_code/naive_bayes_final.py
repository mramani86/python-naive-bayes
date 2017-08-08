import csv	
import random

DELTA = 0.01
	
"""
preparing data
"""
def loadCsv(filename):
	lines = csv.reader(open(filename, "r"))
	dataset = list(lines)
	# for i in range(len(dataset)):
	# 	dataset[i] = [x for x in dataset[i]]
	
	#remove spaces
	for i in range(len(dataset)):
		dataset[i] = [x.strip() for x in dataset[i]]
	return dataset

def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]

"""
calculate class-attribute-value counter
{ class-name : {"atr-val1: count1, "atr-val2": count2...}... }
"""
def get_class_attribute_counter(dataset):
	class_atrribute_counter = {}
	
	for instance in dataset:
		if not instance[-1] in class_atrribute_counter:
			class_atrribute_counter[instance[-1]] = [{}, {}, {}, {}, {}]
		
		#add count of each attribute by 1
		for i in range(0, len(instance) -1):
			counter = class_atrribute_counter[instance[-1]][i]
			
			if not instance[i] in counter:
				counter[instance[i]] = 1
			else:
				counter[instance[i]] += 1
								
			class_atrribute_counter[instance[-1]][i] = counter
	return class_atrribute_counter

"""
calculate attribute probability given a class and input vector
"""
def attributes_probabilities(class_atrribute_counter, class_name, input_vector):
	atr_probablities = []
	
	#if not training data for a given class name return 0 probability
	if class_name not in class_atrribute_counter:
		return [0.0, 0.0, 0.0, 0.0, 0.0]
	
	for i in range(0, len(input_vector) - 1):
		#for unknow attribute marked by ? it will return 0
		
		if input_vector[i] in class_atrribute_counter[class_name][i]:
			atr_count = class_atrribute_counter[class_name][i][input_vector[i]]
		else:
			atr_count = 0
		total = sum(class_atrribute_counter[class_name][i].values())
		
		atr_probablities.append(atr_count/total + DELTA)
	return atr_probablities	
	
"""
calculate class probability given an input vector and a class name
"""
def class_probability_given_attributes_and_classname(class_atrribute_counter, class_name, input_vector):
	prob = 1.0
	for p in attributes_probabilities(class_atrribute_counter, class_name, input_vector):
		# print(p)
		prob *= p

	return prob

"""
calculate class probability given an input vector
"""
def class_probabilities(class_atrribute_counter, input_vector):
	probabilities = {}
	
	for cls in class_atrribute_counter:
		prob = class_probability_given_attributes_and_classname(class_atrribute_counter, cls, input_vector)
		probabilities[cls] = prob
		
	total = sum(probabilities.values())
	for cls in probabilities:
		probabilities[cls] = probabilities[cls]/total
	return probabilities
		
"""
Make a prediction
"""
def predict(class_atrribute_counter, input_vector):
	probabilities = class_probabilities(class_atrribute_counter, input_vector)
	
	best_label, best_prob = None, -1
	for cls, probability in probabilities.items():
		if best_label is None or probability > best_prob:
			best_prob = probability
			best_label = cls
	return best_label

"""
Make Predictions"
"""
def get_predictions(class_atrribute_counter, test_set):
	predictions = []
	for i in range(len(test_set)):
		result = predict(class_atrribute_counter, test_set[i])
		predictions.append(result)
		# print(result, test_set[i])
	return predictions

"""
Get Accuracy
"""
def get_accuracy(test_set, predictions):
	correct = 0
	for x in range(len(test_set)):
		if test_set[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(test_set))) * 100.0

if __name__ == '__main__':	
	pass