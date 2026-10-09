import math

def ndcg(relevance_scores: list, k: int) -> float:
    """
    Returns NDCG as a float.
    """
    # Write code here
    if k<=0:
        return 0.0
    def dcg(scores):
        return sum(
            (2**rel -1)/math.log2(i+2)
            for i,rel in enumerate(scores[:k])
        )
    actual_dcg=dcg(relevance_scores)
    ideal_dcg=dcg(sorted(relevance_scores,reverse=True))
    if ideal_dcg==0:
        return 0.0
    return actual_dcg/ideal_dcg
    pass