from sklearn.cluster import AgglomerativeClustering
import inflection


class OptimizeClusterSize:
    def __init__(self, data, indices=None, distance_func=None):
        if distance_func is not None and callable(distance_func):
            data = distance_func(data)
        elif distance_func is not None:
            raise ValueError(
                "If distance_func argument is given it needs to be a callable"
            )
        self._data = data

        if not indices:
            raise ValueError("The indices argument need to contain at least one index")
        if not isinstance(indices, list):
            indices = [indices]
        self._indices = indices

        self._optimize()

    def _optimize(self):
        for n_clusters in range(2, min(8, len(self._data))):
            model = AgglomerativeClustering(
                n_clusters=n_clusters, affinity="precomputed", linkage="single"
            )
            model.fit(self._data)
            for index in self._indices:
                index.update(
                    n_clusters=n_clusters, distances=self._data, clusters=model.labels_
                )
        for index in self._indices:
            print(
                f"{inflection.underscore(index.__class__.__name__)} suggest {index.optimal()} clusters"
            )
