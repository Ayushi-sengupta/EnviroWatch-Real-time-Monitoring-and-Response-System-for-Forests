# Forest-Fire-Prediction-Website
A website that predicts the probability of a forest fire taking place based on oxygen,temperature and humidity content
Instructions for Pycharm :
1) In project , add the forest html file in the templates folder
2) In the static folder add the css and js file for css js elements to work on webpage.Get it from here : https://materializecss.com/getting-started.html

# Forest Ranger

## Overview
Forest Ranger is a comprehensive solution designed to enhance forest conservation and improve response to forest fires and deforestation. This project integrates data collection and analysis, real-time prediction through a web application, a GSM-based fire alert system, and a CNN-based deforestation detection mechanism.

## Objectives
- Predict forest fire occurrences using real-time data.
- Send immediate alerts in case of detected fires.
- Detect deforestation and pollution probabilities using CNN.

## Components
### 1. Data Collection and Analysis
- **Datasets:** Algerian Forest Fires (UCI) and West Bengal.
- **Data Points:** Over 250 data points including temperature, humidity, and oxygen levels.
- **Storage:** Data securely stored in Firebase.

### 2. Real-Time Prediction via Web Application
- **Tools:** HTML, CSS, Python, Jupyter Notebook.
- **Functionality:** Analyzes real-time data to predict forest fire occurrence percentage.

### 3. GSM-Based Fire Alert System
- **Components:**
  - Arduino UNO
  - SIM800L GSM Module
  - IR Flame Sensor Module
  - Buzzer
  - 18650 3.7v Rechargeable Battery
- **Functionality:** Sends SMS and call alerts when a fire is detected, ensuring immediate action can be taken.

### 4. CNN-Based Deforestation Detection
- **Functionality:** Uses Convolutional Neural Networks to detect deforestation and pollution probabilities in mountains and deserts.

## Methodology
### Data Collection
- Collect data points from the Algerian Forest Fires dataset and a dataset from West Bengal.
- Store data securely in Firebase.

### Web App Development
- Develop a web app using HTML, CSS, and flask.
- Analyze real-time data to predict forest fire occurrences.

### GSM-Based Fire Alert System
- Assemble components: Arduino UNO, SIM800L GSM Module, IR Flame Sensor, Buzzer, and Battery.
- Configure the system to send SMS and call alerts upon fire detection.

### CNN-Based Deforestation Detection
- Develop a CNN-based model to detect deforestation and pollution probabilities.

## Experimental Details
### Hardware Setup for Alerting Messages and Calls
- **Parts Required:**
  - Arduino UNO
  - SIM800L GSM Module
  - IR Flame Sensor Module
  - Buzzer
  - 18650 3.7v Rechargeable Battery(3)

### Software Environment for Web App
- **Tools:** HTML, CSS, Python, Jupyter Notebook
- **Database:** Firebase for storing datasets

### Dataset
- Collect 250+ data points from the Algerian Forest Fires dataset and a forest fire dataset in West Bengal.

### Data Preprocessing
- Process raw data to make it suitable for machine learning models.
- Use feature selection to choose the best-suited features for the model.
- Apply classification to group objects into preset categories.

## Results and Analysis
- **Logistic Regression Model:** Achieved an accuracy of 89% in predicting forest fire occurrences.
- **SVM Model:** Reached an accuracy of approximately 93% in predicting forest fire events.

## Conclusion
Forest Ranger provides an effective solution for forest fire management and deforestation detection. The integration of various technologies enhances forest conservation efforts and improves the response to forest fires.

## Envirowatch_Webapp_Interface(https://github.com/Ayushi-sengupta/EnviroWatch-Real-time-Monitoring-and-Response-System-for-Forests/blob/main/Pictures/webapp1.jpg)


## Contact
For more information, feel free to contact the project contributors:

- Rupantar Chowdhury:(https://github.com/rupantar99)
- Rahul Kumar Gorai(https://github.com/rahulgorai123)
- Ashish Ranjan
- Under the supervision of Dr. Anirban Goswami

## License
This project is licensed under the MIT License. See the LICENSE file for details.


