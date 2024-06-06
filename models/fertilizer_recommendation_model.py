import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

def fertilizer_recommendation(input_data1):
    file_path = r'G:\pilask\models\fertilizer_recommendations.csv'
    
    df = pd.read_csv(file_path)

    le_soil = LabelEncoder()
    df['Soil_Type'] = le_soil.fit_transform(df['Soil_Type'])
    le_crop = LabelEncoder()
    df['Crop_Type'] = le_crop.fit_transform(df['Crop_Type'])

    X = df.iloc[:, :8]
    y = df.iloc[:, -1]

    dtc = DecisionTreeClassifier(random_state=0)
    dtc.fit(X, y)

    # Preprocess input data
    soil_type_index = 3  
    crop_type_index = 4   
    soil_enc = le_soil.transform([[input_data1[soil_type_index]]])[0]
    crop_enc = le_crop.transform([[input_data1[crop_type_index]]])[0]
    user_input = [input_data1[0], input_data1[1], input_data1[2], soil_enc, crop_enc, input_data1[5], input_data1[6], input_data1[7]]

    # Predict using Decision Tree
    user_input_array = np.array(user_input)
    fertilizer_name_dtc = dtc.predict(user_input_array.reshape(1, -1))
    ans = fertilizer_name_dtc[0]

    # Return the recommended fertilizer
    return ans