// https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
class Solution {
  public:
    stack<int>st;
    set<int>vis;

    void topo(int cur,vector<vector<pair<int,int>>>&adj){
        if(vis.find(cur)!=vis.end()){
            return;
        }
        vis.insert(cur);
        for(auto it:adj[cur]){
            topo(it.first,adj);
        }
        st.push(cur);

    }
    vector<int> shortestPath(int V, int E, vector<vector<int>>& edges) {
        vector<vector<pair<int,int>>>adj(V,vector<pair<int,int>>());
        for(int i=0;i<E;i++){
            adj[edges[i][0]].push_back({edges[i][1],edges[i][2]});
        }

        vector<int>ans(V,1e9);
        topo(0,adj);

        ans[0]=0;
        
       

        while(st.size()){
            /* TopoSort এর কারনে make sure হচ্ছে  যে বর্তমানে আমরা যে cur এ আছি তাতে reach করার সব possible way আমরা explore করছি , 
            মানে বর্তমানে cur এর মধ্যে আমাদের এটা পর্যন্ত আসার min distance আছে ।  */
            int cur=st.top();
            st.pop();

            for(pair<int,int>temp:adj[cur]){
                int cost=temp.second+ans[cur];
                ans[temp.first]=min(ans[temp.first],cost);
            }
        }
        
        for(int i=0;i<V;i++){
            if(ans[i]==1e9){
                ans[i]=-1;
            }
        }
        return ans;
    }
};
