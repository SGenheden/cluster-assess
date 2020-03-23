from .utils import size_at_max


class Dunn:
    def __init__(self):
        self._scores = dict()

    def update(self, n_clusters, distances, clusters):
        min_dist = None
        max_diam = None
        for icluster in range(n_clusters):
            icluster_index = clusters == icluster
            diam = distances[icluster_index][:, icluster_index].max()
            if max_diam is None or diam > max_diam:
                max_diam = diam

            for jcluster in range(icluster + 1, n_clusters):
                jcluster_index = clusters == jcluster
                dist = distances[icluster_index][:, jcluster_index].min()
                if min_dist is None or dist < min_dist:
                    min_dist = dist

        self._scores[n_clusters] = min_dist / max_diam

    def optimal(self):
        return size_at_max(self._scores)
