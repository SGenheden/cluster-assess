from .utils import size_at_min


class CIndex:
    def __init__(self):
        self._scores = dict()

    def update(self, n_clusters, distances, clusters):
        dsum = 0.0
        dmin = None
        dmax = None
        pair_count = 0
        for icluster in range(n_clusters):
            cluster_index = clusters == icluster
            nobs = sum(cluster_index)
            if nobs <= 1:
                continue
            idistances = distances[cluster_index][:, cluster_index]
            dsum += idistances.sum() / 2
            imin = idistances.min()
            imax = idistances.max()
            if dmin is None or imin < dmin:
                dmin = imin
            if dmax is None or imax > dmax:
                dmax = imax
            pair_count += nobs * (nobs - 1) / 2
        if dmin == dmax:
            return
        self._scores[n_clusters] = (dsum - pair_count * dmin) / (
            dmax * pair_count - dmin * pair_count
        )

    def optimal(self):
        return size_at_min(self._scores)
