def size_at_max(scores):
    size = None
    max_score = None
    for n_clusters, score in scores.items():
        if size is None or score > max_score:
            max_score = score
            size = n_clusters
    return size


def size_at_min(scores):
    size = None
    min_score = None
    for n_clusters, score in scores.items():
        if size is None or score < min_score:
            min_score = score
            size = n_clusters
    return size
