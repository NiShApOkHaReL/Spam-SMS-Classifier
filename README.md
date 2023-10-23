# Spam SMS Detection Project

Screenshot Added

![Screenshot 2023-10-22 080859](https://github.com/NiShApOkHaReL/Spam-SMS-Classifier/assets/107798171/11d1440f-9bbe-4974-8ebb-e931aaface6d)



![Screenshot 2023-10-22 081032](https://github.com/NiShApOkHaReL/Spam-SMS-Classifier/assets/107798171/3c89c4ea-7589-4269-9505-4159bbd16594)


## Overview
This project is focused on developing a machine learning model for the detection of spam and ham (non-spam) SMS messages. The project covers key steps such as data cleaning, exploratory data analysis (EDA), text preprocessing, model building, evaluation, and performance comparison among various machine learning algorithms.

## Key Steps

### 1. Data Cleaning
- Load the SMS dataset and remove unnecessary columns.
- Rename columns for clarity.
- Remove duplicate values.
- Verify the dataset's integrity, such as checking for missing values.

### 2. Exploratory Data Analysis (EDA)
- Visualize the distribution of spam and ham messages to understand class balance.
- Analyze the statistics of the text data, including character count, word count, and sentence count.
- Visualize common words in spam and ham messages using word clouds.

### 3. Text Preprocessing
- Perform text preprocessing, including lowercasing, tokenization, removing special characters, removing stop words and punctuation, and stemming.
- Prepare the transformed text for model training.

### 4. Model Building
- Build machine learning models using various algorithms, including Naive Bayes, Support Vector Machine, Logistic Regression, Random Forest, AdaBoost, and more.
- Evaluate the models using accuracy and precision.

### 5. Evaluation
- Assess the model performance based on accuracy and precision scores.
- Compare the performance of different algorithms.
- Select the model with the highest precision score, crucial for spam detection to minimize false positives.

### 6. Performance Comparison
- Compare the accuracy and precision of various machine learning algorithms.
- Visualize the performance of different models using bar plots.

## Results
- The project successfully builds and evaluates several machine learning models for spam SMS detection.
- A comparison of algorithms shows the best-performing model based on precision.
- The selected model can be deployed for spam detection in SMS messages.

This project offers a comprehensive approach to building a spam SMS detection system and serves as a valuable guide for similar text classification tasks.


## Usage

To use the SMS Spam Detection application, follow these simple steps:


1. **Clone the project:**  
   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/GarimaPaudel/Spam-SMS-Classifier.git

2. **Navigate to the project directory:**

    Open your Command Prompt or terminal and navigate to the directory where you saved the project.

3. **Run the application:**

    Type the following command to start the application :

    ```bash
    streamlit run app.py
    ```

4. **Explore the application:**
    You will now be redirected to the page in your web browser, where you can see a user-friendly interface.

5. **Enter SMS message:**
    In the text box provided, enter the SMS message that you want to check for spam. You can copy and paste the message from your device.And click on the predict button.

6.  **View the result:**
    You will receive a result that indicates whether the entered SMS message is spam or not. If it's spam, the application will inform you of the spam status.

7. **Repeat as needed:**
You can repeat the process for any SMS message you want to check. The application will quickly and easily determine whether the message is spam.

Enjoy using this application to identify and filter out spam messages from your SMS inbox, helping you maintain a clean and safe messaging experience.