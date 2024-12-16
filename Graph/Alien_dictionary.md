## Alian Dictionary
* https://neetcode.io/problems/foreign-dictionary
* https://www.geeksforgeeks.org/problems/alien-dictionary/1


```cpp
class Solution {
public:
    string foreignDictionary(vector<string>& words) {
        
        map<char,set<char>>mpp;

        int n=words.size();
        if(n==1){
            return words[0];
        }

        map<char,int>upp;

        for(int i=0;i<n;i++){
            for(char cur:words[i]){
                upp[cur];
            }
        }

        for(int i=0;i<n-1;i++){
            string a=words[i],b=words[i+1];
            int m=min(a.size(),b.size());
            if(a.size()>b.size()){
                int f=1;
                for(int j=0;j<m;j++){
                    if(a[j]!=b[j]){
                        f=0;
                        break;
                    }
                }
                if(f)return "";
            }
            for(int j=0;j<m;j++){
                if(a[j]!=b[j]){
                    if(mpp[a[j]].find(b[j])==mpp[a[j]].end()){
                        mpp[a[j]].insert(b[j]);
                        upp[b[j]]++;
                    }
                    break;
                }
            }
            
        }

        

        vector<char>brr;
        for(auto it:upp){
            if(it.second==0){
                brr.push_back(it.first);
            }
        }

        

        string ans="";
        while(brr.size()){
            char cur=brr.back();
            brr.pop_back();
            ans+=cur;

            for(char temp:mpp[cur]){
                upp[temp]--;
                if(upp[temp]==0){
                    brr.push_back(temp);
                }
            }
        }

        

        if(ans.size()!=upp.size()){
            ans="";
        }
        return ans;
    }
};
```

