import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if curDepth == targetDepth:
        return scores[nodeIndex]
    
    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))

# Driver code
def main():
    scores = []
    n = int(input("Enter the number of elements in the scores list: "))
    for i in range(n):
        score = int(input(f"Enter score {i + 1}: "))
        scores.append(score)
    
    treeDepth = math.log(len(scores), 2)
    
    print("The optimal value is:", minimax(0, 0, True, scores, treeDepth))

if __name__ == "__main__":
    main()
