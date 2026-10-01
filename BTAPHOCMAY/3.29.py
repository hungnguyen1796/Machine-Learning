import numpy as np

class Perceptron:
    def __init__(self, lr=0.1, epochs=10):
        self.lr = lr
        self.epochs = epochs

    def fit(self, X, y):
        self.w = np.zeros(X.shape[1])
        self.b = 0

        for _ in range(self.epochs):
            for i in range(len(X)):
                z = np.dot(X[i], self.w) + self.b

                if y[i] * z <= 0:
                    self.w = self.w + self.lr * y[i] * X[i]
                    self.b = self.b + self.lr * y[i]

    def predict(self, X):
        z = np.dot(X, self.w) + self.b
        return np.where(z >= 0, 1, -1)


X = np.array([
    [2, 3],
    [3, 4],
    [1, 1],
    [5, 6]
])

y = np.array([1, 1, -1, 1])

model = Perceptron()

model.fit(X, y)
X_new = np.array([
    [4, 5],
    [1, 2]
])

print(model.predict(X_new))