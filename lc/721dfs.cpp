// dfs solution
class Solution {
public:
    // main function
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        // build the graph
        unordered_map<string, vector<string>> graph = buildGraph(accounts);

        // initialize the res vector and visited vector
        vector<vector<string>> res;
        unordered_set<string> visited;

        // the main loop
        for (auto & account : accounts) {
            string email = account[1];
            vector<string> tmp;

            dfs(graph, visited, email, tmp);
            
            if (tmp.empty()) continue;

            // sort the tmp vec
            // and push to the res
            sort(tmp.begin(), tmp.end());
            tmp.insert(tmp.begin(), account[0]);
            res.push_back(tmp);
        }

        return res;
    }


    // the graph builder
    unordered_map<string, vector<string>> buildGraph(vector<vector<string>>& accounts) {
        unordered_map<string, vector<string>> graph;

        for (auto & account : accounts) {
            string master = account[1];

            // delete the duplicates
            for (auto & email : unordered_set<string>(account.begin() + 2, account.end())) {
                graph[master].push_back(email);
                graph[email].push_back(master);
            }

        }
        return graph;
    }


    // dfs function
    void dfs(unordered_map<string, vector<string>>& graph, unordered_set<string>& visited, string& email, vector<string>& res) {
        // branch cut if visited
        if (visited.count(email)) return;

        visited.insert(email);
        res.push_back(email);

        for (auto & neighbor : graph[email]) {
            dfs(graph, visited, neighbor, res);
        }
        
    }

};
