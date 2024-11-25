# Problem Title
Predicting Fly Rock in Blasting

# Problem Statement

Fly rock, an unintended ejection of rock fragments during blasting, poses significant risks to safety, equipment, and surrounding infrastructure. Predicting its occurrence can help mitigate these risks by optimizing blasting parameters. This project leverages machine learning techniques to predict fly rock events based on rock and blasting data.

## Dataset

The dataset used in this project contains critical parameters related to blasting operations and rock fragmentation:

| Column Name               | Description                                                        |
|---------------------------|--------------------------------------------------------------------|
| Burden                    | Distance between the charge hole and the nearest free face.        |
| Spacing                   | Distance between adjacent charge holes.                            |
| UCS                       | Uniaxial Compressive Strength of the rock.                         |
| Bench Height              | Height of the bench being blasted.                                 |
| Hole Diameter             | Diameter of the blasting hole.                                     |
| Initial Stemming Height   | Height of the initial stemming material in the charge hole.        |
| Final Stemming Height     | Final height of stemming material used in the charge hole.         |
| Charge Length             | Length of the explosive charge in the hole.                        |
| Charge Hole               | Total depth of the charge hole.                                    |
| Powder Factor             | Explosive energy used per unit volume of rock.                     |
| Mean Fragment Sizes       | Average size of rock fragments


Example Dataset Row:

| Burden | Spacing | UCS | Bench Height | Hole Diameter | Initial Stemming Height | Final Stemming Height | Charge Length | Charge Hole | Powder Factor | Mean Fragment Sizes |
|--------|---------|-----|--------------|---------------|-------------------------|-----------------------|---------------|-------------|---------------|---------------------|
| 3.5    | 4.0     | 250 | 12.5         | 150           | 1.5                     | 2.0                   | 10.0          | 12.0        | 0.8           | 50.0                |


## Setup

1. Clone the repository.
git clone https://github.com/your_username/predicting-fly-rock.git
cd predicting-fly-rock

2. Create a virtual environment:
    ```sh
    python -m venv env
    ```
3. Activate the virtual environment:
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source env/bin/activate
        ```
4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

...

- To train the model, run:
    ```sh
    python train.py
    ```
- To make predictions, run:
    ```sh
    python predict.py

- To start the Docker container, run:
    ```sh
    docker build -t my-flask-app .
    docker run -p 5000:5000 my-flask-app
    ```
    ```

## Files

- [train.py](http://_vscodecontentref_/11): Script to train the model.
- [predict.py](http://_vscodecontentref_/12): Script to make predictions using the trained model.
- [send_request.py](http://_vscodecontentref_/13): Script to send requests to the prediction API.
- [blast.ipynb](http://_vscodecontentref_/14): Jupyter notebook for exploratory data analysis.
- [test_predict.ipynb](http://_vscodecontentref_/15): Jupyter notebook for testing predictions.
- [data.csv](http://_vscodecontentref_/16): Dataset used for training and testing.
- [best_pipeline.pkl](http://_vscodecontentref_/17): Serialized model pipeline.
- [Dockerfile](http://_vscodecontentref_/18): Docker configuration file for containerizing the application.
- [requirements.txt](http://_vscodecontentref_/19): List of required Python packages.

Machine Learning Workflow
Exploratory Data Analysis (EDA):

Visualized relationships between variables (e.g., Powder Factor vs. Mean Fragment Sizes).
Identified patterns, outliers, and correlations.
Data Preprocessing:

Handled missing values, normalized data, and engineered features like ratios (e.g., Burden-to-Spacing).
Model Training:

Trained multiple regression models (e.g., Random Forest, Gradient Boosting).
Evaluated using metrics like RMSE and R².
Prediction:

Provided actionable insights into the likelihood of fly rock events.


Contribution
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (feature-branch).
Commit your changes.
Submit a pull request.


## License

This project is licensed under the MIT License.

Acknowledgments
Special thanks to the contributors of this project and the organizations providing insights into safe blasting practices.

If you have any questions, feel free to reach out or open an issue in the repository.
