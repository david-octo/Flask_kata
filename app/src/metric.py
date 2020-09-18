def compute_accuracy(actual: list, predicted: list) -> float:
    if len(actual) != len(predicted):
        raise ValueError("Not same len")
    correctly_predicted = 0
    for actual_elt, predicted_elt in zip(actual, predicted):
        if actual_elt == predicted_elt:
            correctly_predicted += 1
    return correctly_predicted / len(actual)


