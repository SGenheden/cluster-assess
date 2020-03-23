from sklearn.metrics import silhouette_score

from .utils import size_at_max


class Silhouette:
    def __init__(self):
        self._scores = dict()

    def update(self, n_clusters, distances, clusters):
        self._scores[n_clusters] = silhouette_score(
            distances, clusters, metric="precomputed"
        )

    def optimal(self):
        return size_at_max(self._scores)
