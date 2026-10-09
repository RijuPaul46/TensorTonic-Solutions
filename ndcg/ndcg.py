import math

def ndcg(relevance_scores: list, k: int) -> float:
    """
    Returns NDCG as a float.
    """
    # Write code here
    dcg=0
    n=len(relevance_scores)
    for i in range(0,min(n,k)):
        dcg+=float((2**relevance_scores[i]-1)/math.log2(i+2))
    sorted_scores=sorted(relevance_scores,reverse=True)
    ndcg=0
    for i in range(0,min(n,k)):
        ndcg+=float((2**sorted_scores[i]-1)/math.log2(i+2))
    if ndcg==0:
        return 0
    return float(dcg/ndcg)
    pass