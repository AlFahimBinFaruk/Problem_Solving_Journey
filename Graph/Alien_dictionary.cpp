### https://neetcode.io/problems/foreign-dictionary
### https://www.geeksforgeeks.org/problems/alien-dictionary/1



* The string is invalid only if there is an cycle or there exixts and sequence like ["wrtkj","wrt"]




class Solution {
public:
	string topo(unordered_map<char,vector<char>>&mpp){
		queue<char>q;
		unordered_map<char,int>ing;
		
    for(auto it:mpp){
			ing[it.first]=0;
		}
    
		for(auto it:mpp){
			for(char c:it.second){
				ing[c]++;
			}
		}

        
		for(auto it:ing){
			if(it.second==0){
				q.push(it.first);
			}
		}

		string ans="";

		while(q.size()){
			char cur=q.front();
			q.pop();
			ans+=cur;

			for(char c:mpp[cur]){
				ing[c]--;
				if(ing[c]==0){
					q.push(c);
				}
			}

		}

		if(ans.size()==mpp.size())return ans;
		return "";
	}

  string foreignDictionary(vector<string>& words) {
        
		unordered_map<char,vector<char>>mpp;
		int n=words.size();
		for(int i=0;i<n;i++){
			for(char c:words[i]){
				mpp[c];
			}
		}

        

		for(int i=0;i<n-1;i++){
			string a=words[i],b=words[i+1];
			int mn=min(a.size(),b.size());

			if(a.substr(0,mn)==b.substr(0,mn) and a.size()>b.size()){
				return "";
			}
			for(int j=0;j<mn;j++){
				if(a[j]!=b[j]){
					mpp[a[j]].push_back(b[j]);
					break;
				}
			}
		}

		return topo(mpp);
    }
};

