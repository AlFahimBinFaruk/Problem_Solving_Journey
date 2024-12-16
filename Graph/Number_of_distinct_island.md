## Number of distinct island

1. With using node count hasing fails because of this kind of scene
```text
slrtb => s1lrtb
slrtb => s1lr2tb
```
```cpp
class Solution {
  public:
    set<pair<int,int>>vis;
    set<string>ms;
    void dfs(int i,int j,vector<vector<int>>& grid){

        queue<pair<int,int>>q;
        q.push({i,j});

        int n=grid.size(),m=grid[0].size();
        string s="s";
        int cnt=0;
        while(q.size()){
            pair<int,int>temp=q.front();
            q.pop();
            cnt++;
            s+=cnt;
            int a=temp.first,b=temp.second;
            if(a-1>=0 and grid[a-1][b]==1 and vis.find({a-1,b})==vis.end()){
                vis.insert({a-1,b});
                q.push({a-1,b});
                s+='l';
            }
            if(a+1<n and grid[a+1][b]==1 and vis.find({a+1,b})==vis.end()){
                vis.insert({a+1,b});
                q.push({a+1,b});
                s+='r';
            }
            if(b-1>=0 and grid[a][b-1]==1 and vis.find({a,b-1})==vis.end()){
                vis.insert({a,b-1});
                q.push({a,b-1});
                s+='t';
            }
            if(b+1<m and grid[a][b+1]==1 and vis.find({a,b+1})==vis.end()){
                vis.insert({a,b+1});
                q.push({a,b+1});
                s+='b';
            }
        }

        ms.insert(s);
    }

    int countDistinctIslands(vector<vector<int>>& grid) {
        
        int n=grid.size(),m=grid[0].size();

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(vis.find({i,j})==vis.end() and grid[i][j]){
                    vis.insert({i,j});
                    dfs(i,j,grid);
                }
            }
        }

        return ms.size();

    }
};
```
