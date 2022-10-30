### Vidoe Explanation
* [Neetcode](https://www.youtube.com/watch?v=1pkOgXD63yU)

### Steps to solve
1. Initialize a default value of maxProfit with 0.
2. Initialize left and right value where left = price of buy , right = price of sell.
   * l = 0
   * r = 1
3. Then While r < len(prices).
   * If profitable (prices[l] < prices[r]) :
     * profit = prices[r] - prices[l].
     * set the profit to maxProfit with :: max(profit,maxProfit).
   * If not profitable (prices[r] < prices[l]) :
     * which means i have to change buying prize as it is not profitable with l=r.
   * and always change selling price with r+=1.  
4. Return the maxProfit after end of iteration in prices and it will be the result.
5. Time O(N) | Space O(1).
