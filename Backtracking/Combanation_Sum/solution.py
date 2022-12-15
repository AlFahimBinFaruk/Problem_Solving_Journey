class Solution:
    # Time O(2^t) | Space O(N)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # we gonna use DFS and desicion tree(takes two decision) concept to solve this
        result = []

        def dfs(i,curr,total):
            if total == target:
                result.append(curr.copy())
                return

            # handle outof bound
            if (i >= len(candidates)) or total > target:
                return
            
            # first decision
            curr.append(candidates[i])
            dfs(i,curr,(total+candidates[i]))

            # second decision
            curr.pop()
            dfs(i+1,curr,total)

        dfs(0,[],0)

        return result    
                  
