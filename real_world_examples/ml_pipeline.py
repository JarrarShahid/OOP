# ml_pipeline.py

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris

# Data Preprocessing Class
class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def load_data(self):
        """Loads dataset (Iris dataset for demo)"""
        data = load_iris()
        X = pd.DataFrame(data.data, columns=data.feature_names)
        y = pd.Series(data.target)
        return X, y

    def preprocess(self, X):
        """Scales numerical features"""
        return self.scaler.fit_transform(X)

# Model Training Class
class ModelTrainer:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def train(self, X_train, y_train):
        """Trains the model"""
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        """Makes predictions"""
        return self.model.predict(X_test)

# Model Evaluation Class
class ModelEvaluator:
    @staticmethod
    def evaluate(y_test, y_pred):
        """Evaluates model performance"""
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        print(f"Accuracy: {accuracy:.4f}")
        print("Classification Report:\n", report)

# ML Pipeline Manager
class MLPipeline:
    def __init__(self):
        self.preprocessor = DataPreprocessor()
        self.trainer = ModelTrainer()
        self.evaluator = ModelEvaluator()

    def run(self):
        """Executes the ML pipeline"""
        # Load and preprocess data
        X, y = self.preprocessor.load_data()
        X = self.preprocessor.preprocess(X)

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train and evaluate model
        self.trainer.train(X_train, y_train)
        y_pred = self.trainer.predict(X_test)
        self.evaluator.evaluate(y_test, y_pred)

# Run the pipeline
if __name__ == "__main__":
    pipeline = MLPipeline()
    pipeline.run()
