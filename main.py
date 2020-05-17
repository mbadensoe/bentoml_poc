# https://github.com/bentoml/BentoML/blob/master/guides/quick-start/main.py
from sklearn import svm
from sklearn import datasets

from iris_classifier import IrisClassifier

if __name__ == "__main__":
    # Load training data
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # Mapping between target and target name
    iris_mapping = dict()
    for index, name in enumerate(iris.target_names):
        iris_mapping[index] = name

    # Model Training
    clf = svm.SVC(gamma="scale")
    clf.fit(X, y)

    # Create a iris classifier service instance
    iris_classifier_service = IrisClassifier()

    # Pack the newly trained model artifact
    iris_classifier_service.pack("model", clf)

    # Save the prediction service to disk for model serving
    saved_path = iris_classifier_service.save()
