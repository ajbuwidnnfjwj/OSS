import numpy as np
from sklearn import (datasets, tree, model_selection, ensemble)
from xgboost import XGBClassifier

if __name__ == '__main__':
    # Load a dataset
    wdbc = datasets.load_breast_cancer()

    # Train a model
    model = XGBClassifier(    
        learning_rate=0.1,  # controls the step size during optimization
        n_estimators=1000,   # number of boosting rounds
        max_depth=3,        # maximum depth of a tree
        min_child_weight=1, # minimum sum of instance weight (hessian) needed in a child
        subsample=0.8,      # fraction of samples used for training trees
        colsample_bytree=0.8, # fraction of features used for training trees
        objective='binary:logistic',  # binary classification problem
        random_state=42 ) # TODO
    cv_results = model_selection.cross_validate(model, wdbc.data, wdbc.target, cv=5, return_train_score=True)

    # Evaluate the model
    acc_train = np.mean(cv_results['train_score'])
    acc_test = np.mean(cv_results['test_score'])
    print(f'* Accuracy @ training data: {acc_train:.3f}')
    print(f'* Accuracy @ test data: {acc_test:.3f}')
    print(f'* Your score: {max(10 + 100 * (acc_test - 0.9), 0):.0f}')