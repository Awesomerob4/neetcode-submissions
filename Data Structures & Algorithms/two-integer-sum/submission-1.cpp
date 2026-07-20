class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> solutions;
        //solutions.push_back(int);
        for(int i=0; i<= nums.size()-1; i++){
            for(int j = 1; j<=nums.size()-1; j++){
                if(((nums[i] + nums[j]) == target) && (i!= j)){
                    solutions.push_back(i);
                    solutions.push_back(j);
                    return solutions;
                }
            }
        }
    }
};
