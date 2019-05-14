# Brainstorming:
# Given that these are anagrams as input, storing the strings themselves
# won't really make much of impact since each will be mapped or inserted to the set
# 1. Convert input string into ordinal integer sum
# 2. Create list of size equal to number of inputs (len(strs), because the max
# number of anagrams is 0, meaning we have all unique strings)
# 3. Map the integer sum hash to the index position in A
# Note: Need to append the strings themselves into the string, so helper method
# has to return it
class Solution:
    def groupAnagrams(self, strs):
        word_index_map = {}
        anagram_index = 0
        out_list = []
        for word in strs:
            # Get converted hash value for string
            tuple_str = tuple(sorted(word))
            # Check if hash value is already inserted into mapping, if not
            # then add it and increase the anagram index by 1
            if tuple_str not in word_index_map:
                word_index_map[tuple_str] = anagram_index
                print(word_index_map[tuple_str])
                anagram_index += 1

            if len(out_list) > word_index_map[tuple_str]:
                out_list[word_index_map[tuple_str]].append(word)
            else:
                sub_list = [word]
                print(sub_list[0])
                out_list.append(sub_list)
                print(len(out_list))
        return out_list
