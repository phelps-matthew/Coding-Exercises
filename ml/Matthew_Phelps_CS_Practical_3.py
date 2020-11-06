import numpy as np
from matplotlib import pyplot as plt


class KMeans:
    # initialize and fit
    # Find the current cluster each data belongs to
    # Update cluster centers
    # new_cluster
    def __init__(self, data: np.ndarray):
        self.data = data
        self.dim = self.data.shape[1]
        self.numel = self.data.shape[0]

    def initialize(self, k: int) -> None:
        """Select k random points as centroids"""
        # Match dimension of `self.data`
        self.k = np.random.normal(size=(k, self.dim))

    def euclidian_batch_pt(self, batch: np.ndarray, pt: np.ndarray):
        """Find euclidian distance between data and point"""
        return np.sum(np.square(batch - pt), axis=1, keepdims=True)

    def euclidian_batch_stack(self):
        cluster_distances = []
        for i in range(self.k.shape[0]):
            dist = self.euclidian_batch_pt(self.data, self.k[i])
            cluster_distances.append(dist)
        return np.hstack(cluster_distances)

    def classify(self):
        cluster_distances = self.euclidian_batch_stack()
        return np.argmin(cluster_distances, axis=1).reshape(self.numel, 1)

    def find_new_cluster(self):
        """Take average of assigned points"""
        class_lists = [[] for _ in range(self.k.shape[0])]
        classes = self.classify()
        clusters = [[] for _ in range(self.k.shape[0])]
        for i in range(self.numel):
            class_lists[int(classes[i])].append(self.data[i])
        for i in range(self.k.shape[0]):
            clusters[i] = sum(class_lists[i])/len(class_lists[i])
        return clusters



    def elbow(self):
        """Determine optimal number of clusters, k """
        ...

    def fit(self):
        """Find final cluster assignment"""
        ...

    def plot(self):
        """Plot data and cluster assignments"""
        ...


class DataGeneration:
    def __init__(self):
        self.data = self.ambers_random_data()

    def ambers_random_data(self):
        np.random.seed(1)
        x = 2
        data1 = np.random.normal(size=(100, 2)) + [x, x]
        data2 = np.random.normal(size=(100, 2)) + [x, -x]
        data3 = np.random.normal(size=(100, 2)) + [-x, -x]
        data4 = np.random.normal(size=(100, 2)) + [-x, x]
        data = np.concatenate((data1, data2, data3, data4))
        np.random.shuffle(data)
        return data


def tests():
    k_means = KMeans(DataGeneration().data)
    k_means.initialize(4)
    print(k_means.data[:3, :])
    print("-" * 20)
    print(k_means.k[0])
    print("-" * 20)
    # print(k_means.euclidian_batch_pt(k_means.data, k_means.k[0])[:3])
    print("-" * 20)
    print(k_means.euclidian_batch_stack()[:3])
    print("-" * 20)
    print(k_means.classify()[:3])
    print("-" * 20)
    print(k_means.find_new_cluster())


if __name__ == "__main__":
    tests()
# generator = DataGeneration()
# k_means = KMeans(generator.data)
# k_means.initialize(4)
# print(generator.data)
# print(k_means.k)
# k_means.elbow()
# k = input("Choose number of clusters: ")
# k_means.fit()
# k_means.plot()
