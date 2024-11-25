# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# %%
df = pd.read_csv('data.csv')
df

# %%
df.columns = df.columns.str.lower().str.replace(' ', '_')
df


# %%
df.isnull().any()

# %%
df.duplicated().sum()

# %%
df.drop_duplicates()

# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df.powder_factor, y=df.mean_fragment_sizes)

# Add title and labels
plt.title('Powder Factor vs. Mean Fragment Size')
plt.xlabel('Powder Factor')
plt.ylabel('Mean Fragment Size')

# Show plot
plt.show()

# %%
from sklearn.pipeline import Pipeline
X = df.drop('mean_fragment_sizes', axis=1)
y = df.mean_fragment_sizes




# %%
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', RandomForestRegressor(random_state=20))
])

param_grid = {
    'regressor__n_estimators': [50, 100, 200],
    'regressor__max_depth': [None, 10, 20, 30],
    'regressor__min_samples_split': [2, 5, 10],
    'regressor__min_samples_leaf': [1, 2, 4]
}
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.2, random_state=20)

# %%
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search.fit(X_train, y_train)
best_pipeline = grid_search.best_estimator_

# %%
# Predict on the test data
y_pred = best_pipeline.predict(X_test)


from sklearn.metrics import mean_squared_error, r2_score, root_mean_squared_error
# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mse)


print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
print(f'Root Mean Squared Error: {rmse}')

# %%
import pickle
# Save the trained pipeline to a file

with open('best_pipeline.pkl', 'wb') as f:
    pickle.dump(best_pipeline, f)





