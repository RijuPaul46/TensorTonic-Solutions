def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    relevant_in_top_k=set(recommended[:k]) & set(relevant)
    precision_at_k=float(len(relevant_in_top_k)/k)
    recall_at_k=float(len(relevant_in_top_k)/len(relevant))
    return [precision_at_k,recall_at_k]
    pass