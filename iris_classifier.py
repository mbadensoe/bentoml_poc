# https://github.com/bentoml/BentoML/blob/master/guides/quick-start/iris_classifier.py
from bentoml import env, artifacts, api, BentoService
from bentoml.handlers import DataframeHandler
from bentoml.artifact import SklearnModelArtifact


@env(auto_pip_dependencies=True)
@artifacts([SklearnModelArtifact("model")])
class IrisClassifier(BentoService):
    @api(DataframeHandler)
    def predict(self, df):
        # Mapping between predicted value and actual name
        iris_mapping = {0: "setosa", 1: "versicolor", 2: "virginica"}
        inference_list = self.artifacts.model.predict(df)
        output = [iris_mapping[element] for element in inference_list]
        return output
