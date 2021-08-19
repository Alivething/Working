
# Use scikit-learn to grid search the batch size and epochs
import numpy
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
# Function to create model, required for KerasClassifier
def create_model():
	# create model
	model = Sequential()
	model.add(Dense(12, input_dim=8, activation='relu'))
	model.add(Dense(1, activation='sigmoid'))
	# Compile model
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
# create model
model = KerasClassifier(build_fn=create_model, verbose=0)
# define the grid search parameters
batch_size = [10, 20, 40, 60, 80, 100]
epochs = [10, 50, 100]
param_grid = dict(batch_size=batch_size, epochs=epochs)
grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=3)
grid_result = grid.fit(X, Y)
# summarize results
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))




# 0.348958 (0.024774) with: {'epochs': 10, 'batch_size': 10}
# 0.348958 (0.024774) with: {'epochs': 50, 'batch_size': 10}
# 0.466146 (0.149269) with: {'epochs': 100, 'batch_size': 10}
# 0.647135 (0.021236) with: {'epochs': 10, 'batch_size': 20}
# 0.660156 (0.014616) with: {'epochs': 50, 'batch_size': 20}
# 0.686198 (0.024774) with: {'epochs': 100, 'batch_size': 20}
# 0.489583 (0.075566) with: {'epochs': 10, 'batch_size': 40}
# 0.652344 (0.019918) with: {'epochs': 50, 'batch_size': 40}
# 0.654948 (0.027866) with: {'epochs': 100, 'batch_size': 40}
# 0.518229 (0.032264) with: {'epochs': 10, 'batch_size': 60}
# 0.605469 (0.052213) with: {'epochs': 50, 'batch_size': 60}
# 0.665365 (0.004872) with: {'epochs': 100, 'batch_size': 60}
# 0.537760 (0.143537) with: {'epochs': 10, 'batch_size': 80}
# 0.591146 (0.094954) with: {'epochs': 50, 'batch_size': 80}
# 0.658854 (0.054904) with: {'epochs': 100, 'batch_size': 80}
# 0.402344 (0.107735) with: {'epochs': 10, 'batch_size': 100}
# 0.652344 (0.033299) with: {'epochs': 50, 'batch_size': 100}
# 0.542969 (0.157934) with: {'epochs': 100, 'batch_size': 100}