'''
Problem:
Given predicted probabilities and labels, compute binary cross entropy loss:

preds = [0.9, 0.2, 0.1]
labels = [1, 0, 0]
'''

import math
def binary_log_loss_entropy(preds, labels):
    loss = 0.0
    for p, l in zip(preds, labels):
        loss += - (l * math.log(p) + (1 - l) * math.log(1 - p))
    return loss / len(preds)


# Example usage
preds = [0.9, 0.2, 0.1]
labels = [1, 0, 0]
loss = binary_log_loss_entropy(preds, labels)
print(f"Binary Log Loss (Cross Entropy): {loss:.4f}")