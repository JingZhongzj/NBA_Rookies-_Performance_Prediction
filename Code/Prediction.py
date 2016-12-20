
from __future__ import print_function

from pyspark.ml.classification import MultilayerPerceptronClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession\
        .builder.appName("multilayer_perceptron_classification_example").getOrCreate()

    # Load training data
    data = spark.read.format("libsvm")\
        .load("/Path_to_Training_data/Training_data.txt")
    rookie = spark.read.format("libsvm")\
        .load("/Path_to_Data_for_Prediction/Prediction_data.txt")
    # Split the data into train and test
    splits = data.randomSplit([0.8, 0.2], 1234)
    train = splits[0]
    test = splits[1]
    # specify layers for the neural network:
    # input layer of size 21 (features), four intermediate of size 22, 17, 13 and 8
    # and output of size 4 (classes)
    layers = [21, 22, 17, 13, 8, 4]
    # create the trainer and set its parameters
    trainer = MultilayerPerceptronClassifier(maxIter=100, layers=layers, blockSize=128, seed=1234)
    # train the model
    model = trainer.fit(train)
    # compute accuracy on the test set
    result = model.transform(test)
    predictionAndLabels = result.select("prediction", "label")
    evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
    print("Accuracy: " + str(evaluator.evaluate(predictionAndLabels)))

    result01 = model.transform(rookie)
    result01.select("prediction", "label").show(20)

    spark.stop()
