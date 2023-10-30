import os 
import sys 

from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
# from sklearn.metrics import roc_curve, auc


from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = ( 
                train_array[:, :-1], 
                train_array[:,-1],
                test_array[:, :-1],
                test_array[:, -1],
            )

            models = {
                "Logistic Regression": LogisticRegression(),
                "KNN": KNeighborsClassifier(),
                "Naive Bayes": GaussianNB(),
                "Decision Tree": DecisionTreeClassifier(),
                "SVM": SVC(kernel='linear'),
                "Random Forest Classifier": RandomForestClassifier(),
                "Gradient Boosting Classifier": GradientBoostingClassifier(),
            }

            params = {
                "Logistic Regression": {
                    "C": [0.001, 0.01, 0.1, 1, 10],
                    "penalty": ['l1', 'l2']
                },
                "KNN": {
                    "n_neighbors": [3, 5, 7, 9],
                    "weights": ['uniform', 'distance'],
                    "p": [1, 2]
                },
                "Naive Bayes": {
                    # No major hyperparameters for GaussianNB
                },
                "Decision Tree": {
                    "max_depth": [5, 10, None],
                    "min_samples_split": [2, 5, 10],
                    "min_samples_leaf": [1, 2, 4]
                },
                "SVM": {
                    "C": [0.001, 0.01, 0.1, 1, 10],
                    # "kernel": ['linear', 'poly', 'rbf', 'sigmoid'],
                    "degree": [2, 3, 4, 5],
                    # "gamma": ['scale', 'auto'] + [0.001, 0.01, 0.1, 1],
                    # "loss": ['hinge', 'squared_hinge']
                },
                "Random Forest Classifier": {
                    "n_estimators": [100, 200, 500],
                    "max_depth": [10, 20, None],
                    "min_samples_split": [2, 5, 10],
                    "min_samples_leaf": [1, 2, 4]
                },
                "Gradient Boosting Classifier": {
                    "n_estimators": [50, 100, 200],
                    "learning_rate": [0.01, 0.1, 0.2],
                    "max_depth": [3, 4, 5],
                    "min_samples_split": [2, 5, 10]
                }
            }

            model_report:dict = evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models, param=params)
            
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]
            print(best_model)

            if best_model_score < 0.8:
                raise CustomException('No best model found')
            
            logging.info('Best model found on both training and testing dataset.')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj = best_model    
            )

            predicted = best_model.predict(X_test)
            
            accuracy_Score = accuracy_score(y_test, predicted)

            return accuracy_Score

        except Exception as e:
            raise CustomException(e, sys)