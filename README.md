# Bentoml example
Example of using `bentoml` to setup an API for a Machine Learning model, and calling that API to get inferences. 

Example is adapted from the `bentoml` documentation: https://github.com/bentoml/BentoML#getting-started
## Setup project environment
```
> poetry install
```

## Creating bentoml package
Creating the `bentoml` package/api, the `main.py` needs to be executed, such that the model gets trained and saved in the proper format.
```
> python main.py
```
This results in the BentoService being created, and saved to a default location (`~/bentoml`):
```
[2020-05-16 19:18:28,559] INFO - BentoService bundle 'IrisClassifier:20200516191817_11B87D' saved to: ~/bentoml/repository/IrisClassifier/20200516191817_11B87D
```
The created package can be listed by running `bentoml` with the `list` option:
```
> bentoml list
BENTO_SERVICE                         AGE                         APIS                       ARTIFACTS
IrisClassifier:20200516191817_11B87D  2 minutes and 8.06 seconds  predict<DataframeHandler>  model<SklearnModelArtifact>
```
## Getting inferences via the created bentoml service
The `BENTO_SERVICE` with the name `IrisClassifier:20200516191817_11B87D` is an API, that can be deployed, or simply started directly from a local computer. To start (or serve) the newly created `BENTO_SERVICE`, use the `serve` option:
```
> bentoml serve IrisClassifier:latest
INFO - Getting latest version IrisClassifier:20200516191817_11B87D
 * Serving Flask app "IrisClassifier" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
The API is now online and available for requests:
```
> curl \   
  --header "Content-Type: application/json" \
  --request POST \
  --data '[[5.1, 3.5, 1.4, 0.2], [10,10,10,10]]' \
  http://127.0.0.1:5000/predict

["setosa", "virginica"]
```
Using the input in the data part of the request above, the predicted Iris classification is setosa and virginica, respectively.

In the terminal where the `BENTO_SERVICE` got started, contains additional information, e.g. a `POST` for each request it has received:
```
127.0.0.1 - - [16/May/2020 19:26:18] "POST /predict HTTP/1.1" 200 -
```