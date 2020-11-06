import random
import math
import operator
import pandas as pd


class DataLoader:
    def __init__(
        self, path: str = "iris.csv", test_split: float = 0.2, rescale: bool = True
    ):
        """Load Iris dataset"""
        self.df = pd.read_csv(path)
        if path == "iris.csv":
            self.df.columns = ["seplen", "sepwid", "petlen", "petwid", "label"]
        self.features = self.df.columns[:-1]
        self.test_split = test_split
        self.train = self._gen_train_set()
        self.test = self._gen_test_set()

        if rescale:
            self._rescale()

    def _rescale(self):
        """Rescale features to range [0,1]"""
        col = self.features
        self.df[col] = (self.df[col] - self.df[col].min()) / (
            self.df[col].max() - self.df[col].min()
        )

    def _gen_train_set(self):
        """Generate test set. May need stratification"""
        train = self.df.sample(frac=1 - self.test_split).reset_index(drop=True)
        return train

    def _gen_test_set(self):
        """Generate test set. May need stratification"""
        test = self.df.sample(frac=self.test_split).reset_index(drop=True)
        return test

    def get_df(self):
        return self.df


class KNN:
    def __init__(self, data, k):
        """Initialize with training dataset and k nearest neighbors"""
        self.df = data
        self.k = k
        self.features = self.df.columns[:-1]
        self.target = self.df.columns[-1]

    def _euclidean(self, row, cols, pt):
        """Calculate euclidean distance to a given pt"""
        sq_dist = 0
        for i in cols:
            sq_dist += (row[i] - pt[i]) ** 2
        return math.sqrt(sq_dist)

    def get_k_euclidean(self, pt):
        """Get k smallest distances near point as df"""
        fn = lambda x: self._euclidean(x, self.features, pt)
        return self.df.apply(fn, axis=1).nsmallest(self.k)

    def get_knn(self, pt):
        """Get k nearest classes to pt and return most frequent"""
        idxs = self.get_k_euclidean(pt).index.values
        nn_labels = self.df[self.target].iloc[idxs]
        nn_label = nn_labels.value_counts().idxmax()
        return nn_label

    def get_knn_batch(self, test):
        labels = []
        for i in range(len(test)):
            labels.append(self.get_knn(test.iloc[i]))
        return labels




if __name__ == "__main__":

    data = DataLoader(test_split=0.2)
    
    knn = KNN(data.train, 3)
    ke = knn.get_k_euclidean(data.test.iloc[1])
    kke = knn.get_knn(data.test.iloc[10])
    kb = knn.get_knn_batch(data.test)

# print("Accuracy: %.3f%%" % (correct / len(knn.valData)))
