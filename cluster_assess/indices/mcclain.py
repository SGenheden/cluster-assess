from .utils import size_at_min


class McClain:
    def __init__(self):
        self._scores = dict()

    def update(self, n_clusters, distances, clusters):
        within_dist_sum = 0
        nwithin = 0
        without_dist_sum = 0
        nwithout = 0
        for icluster in range(n_clusters):
            icluster_index = clusters == icluster
            within_dist_sum += distances[icluster_index][:, icluster_index].sum() / 2
            iobs = icluster_index.sum()
            nwithin += iobs * (iobs - 1) / 2

            for jcluster in range(icluster + 1, n_clusters):
                jcluster_index = clusters == jcluster
                without_distances = distances[icluster_index, :][:, jcluster_index]
                without_dist_sum += without_distances.sum()
                nwithout += iobs * jcluster_index.sum()

        nominator = within_dist_sum / nwithin / nwithin
        denominator = without_dist_sum / nwithout / nwithout
        self._scores[n_clusters] = nominator / denominator

    def optimal(self):
        return size_at_min(self._scores)
