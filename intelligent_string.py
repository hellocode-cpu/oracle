def get_special_substring(s, k, char_value):
    char_val = {}
    # Creating a dictionary where each character 'a' to 'z' has a corresponding value from char_value
    for i in range(len(char_value)):
        char_val[chr(ord('a') + i)] = int(char_value[i])
    
    i, start, j = 0, 0, 0
    count = 0
    max_len = float('-inf')
    indices = []

    # Iterating through the string 's'
    for i in range(len(s)):
        if char_val[s[i]]:  # If the character is 'special' (char_val[s[i]] == 1)
            max_len = max(max_len, i - start + 1)
        else:  # If the character is 'non-special' (char_val[s[i]] == 0)
            indices.append(i)
            count += 1

            if count <= k:  # If the number of non-special characters is within limit
                max_len = max(max_len, i - start + 1)
            else:  # More than k non-special characters, update start position
                start = indices[j] + 1
                j += 1
                count -= 1
                max_len = max(max_len, i - start + 1)
    
    return max_len


# Example usage
s = "giraffe"
k = 2
char_value = "10101111111111111111111111"

print(get_special_substring(s, k, char_value))


"""#include <iostream>
    #include<vector>
    #include<unordered_map>
    #include<climits>
    using namespace std;
     
    int getSpecialSubString(string s, int k, string charValue) {
    	std::vector<int> list;
    	unordered_map<char,int> charVal;
     
    	for(int i = 0; i < charValue.length(); ++i) {
    		charVal['a'+i] = charValue[i] - '0';
    	}
    	int i =0, start = 0, j = 0;
    	int count = 0;
    	int len = INT_MIN;
    	for(; i < s.length(); ++i) {
    		if(charVal[s[i]]) {
    			len = max(len, i-start+1);
    			continue;
    		}else{
    			list.push_back(i);
    			count++;
    			if(count <=k){
    				len = max(len, i-start+1);
    			}else{
    				start = list[j]+1;
    				j++;
    				count --;
    				len = max(len, i-start+1);
    			}
    		}
    	}
    	return len;
    }
     
    int main() {
    	//You can also take the input from the user 
    	string s = "giraffe";
    	int k = 2;
     
    	cout << getSpecialSubString(s,k,"10101111111111111111111111");
    	return 0;
    }"""
