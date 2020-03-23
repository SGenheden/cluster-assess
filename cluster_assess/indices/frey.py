class Frey:
    def __init__(self):
        self._within = dict()
        self._without = dict()

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

        self._within[n_clusters] = within_dist_sum / nwithin
        self._without[n_clusters] = without_dist_sum / nwithout

    def optimal(self):
        n_clusters = list(self._within.keys())
        size = None
        for c1, c2 in zip(n_clusters[:-1], n_clusters[1:]):
            score = (self._without[c2] - self._without[c1]) / (
                self._within[c2] - self._within[c1]
            )
            if score < 1:
                size = c1 - 1
        return size
