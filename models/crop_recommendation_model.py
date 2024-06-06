import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def crop_recommendation(input_data):
    file_path = 'G:\pilask\models\Crop_recommendations.csv'
    
    data = pd.read_csv(file_path)

    X = data.drop(columns=["crop_name"]).values
    y = data["crop_name"].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize models
    dt = DecisionTreeClassifier()
    svm = SVC(kernel="linear")
    rf = RandomForestClassifier(n_estimators=100)
    gnb = GaussianNB()

    # Fit models
    dt.fit(X_train, y_train)
    svm.fit(X_train, y_train)
    rf.fit(X_train, y_train)
    gnb.fit(X_train, y_train)

    # Preprocess input data
    input_data = np.array(input_data).reshape(1, -1)
    input_data = scaler.transform(input_data)

    # Make predictions
    dt_pred = dt.predict(input_data)
    svm_pred = svm.predict(input_data)
    rf_pred = rf.predict(input_data)
    gnb_pred = gnb.predict(input_data)

    # Determine common recommendation from all models
    crop_recommendations = [dt_pred, svm_pred, rf_pred, gnb_pred]
    common_crop = max(set(crop_recommendations[0]), set(crop_recommendations[1]), set(crop_recommendations[2]), set(crop_recommendations[3]))

    # Return the recommended crop
    return common_crop
