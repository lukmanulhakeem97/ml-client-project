## Project Overview
### Engine Oil Stock Inventory Forecast
This is an ML timeseries forecasting project. This repo contain only model deployement part of the trained model using flask. Detailed files and docs of Machine Learning part can be found on my [drive](https://drive.google.com/drive/folders/1Th8lBTQDZkOp5kBOW-t5eRuaQXHbwAcu?usp=share_link).

Note: Procfile (This project is deployed on Heroku)

### Project Analysis:
The project goal of this work is to build a predictive model for spare-parts inventory forecast. As dataset is has many output class names of spare-parts, it seems to be complicated to build model including all spare-parts categories. Therefore we had build individual forecasting models only for top 3 spare-parts category using Auto Regressive (AR) statistical estimator. These models will forecast spare-part count or quantity required for a given day. Engine oil forecasting model have AIC score 1659.68, Chain Lubrication forecasting model have AIC score 1675.19 and General Service forecasting model have AIC score 1466.41.

### Workflow:
For this project we use data from a given database using SQL. This dataset is somewhat complicated to build a model upon it. So we tried with two approaches to achieve project goal. In first approach we tried to build a multi-class classifier model for the top seven mostly repeated spare-parts categories. In second approach we tried to build three time-series forecast models for top three mostly repeated categories. For the two approaches, prepared different sets of dataset accordingly from the loaded dataset.
In first approach, dataset consists of top seven classes were used. Tried with different scikit-learn, ensemble learning and ANN techniques by using several feature preprocessing and feature selection methods. But none of these give a good performance score. All we got 0.25 accuracy score.

Since first approach is bad, tried to do second approach. Here we use time-series dataset of top three classes where variables are date and counts (or quantity). For each dataset, tried with AR, ARIMA, SARIMA and FB-Prophet. All models are not good enough as the dataset doesn’t have any significant correlation coefficient at the lower lags. But AR model with higher order that have lower AIC and BIC measures able to generate new output (counts of spare-part) with given dates. So we choose Auto Regressive time-series model for the three classes. 

## Required Development Tools & Setup
- Python 3
- Environment and Editor: Anaconda, Juputer Notebook, PyCharm.
- Data loading and preprocessing: Nnumpy, Pandas, Scipy 
- Analysis and Visualiztion: Matplotlib, Seaborn and Sweetviz
- Model training and evaluation: Sklearn, Tensorflow, Statsmodel, fbprophet, LSTM.
- Model serialization: Pickle, Tensorflow

## Step-by-step launch instructions
Inorder to deploy trained model using Flask framework:
1. Clone this repo
   <pre>
   ! git clone https://github.com/lukmanulhakeem97/ml-client-project.git
   </pre>
2. Install recessary packages given in [requirements.txt](requirements.txt):
   <pre>
   ! pip install -r requirements.txt
   </pre>
   for conda, use new or existing environment. Then install packages:
   <pre>
   ! conda create --name myenv --file requirements.txt
   </pre>
   Avtivate conda environment:
   <pre>
      ! conda activate myenv
   </pre>
4. Go to directory where repo installed.
5. In terminal, enter
   <pre>
      ! python flaskapp.py
   </pre>
   This will run flaskapp.py and launch webpage 
   



## Workflow of the application
1. Webpage ask Date as input data till which forecast need to be done. Input would either number of days or last Date in Date format.
2. Input values from html request form will feed as input to the model for making prediction of engine oil quantities.
3. Prediction will be push into webpage as output.
