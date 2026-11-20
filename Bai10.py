from collections import Counter

n, m = map(int, input().split())
votes = list(map(int, input().split()))
counts = Counter(votes)

unique = sorted(set(counts.values()), reverse = True)

if len (unique) < 2:
    print("NONE")
else:
    second_votes = unique[1]
    candidates = [cand for cand, vote in counts.items() if vote == second_votes]
    print(min(candidates))
                
