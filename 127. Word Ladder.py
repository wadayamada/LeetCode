class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or beginWord==None or len(wordList)==0:
            return 0
        
        L=len(beginWord)
        
        net_dict=defaultdict(list)
        
        for word in wordList:
            for i in range(L):
                net_dict[word[:i]+"*"+word[i+1:]].append(word)
                
                
        queue=collections.deque([(beginWord,1)])
        visited=[beginWord]
        
        while queue:
            current_word,num=queue.popleft()
            
            for i in range(L):
                
                i_word=current_word[:i]+"*"+current_word[i+1:]
                
                for next_word in net_dict[i_word]:
                    
                    if next_word==endWord:
                        return num+1
                    
                    if next_word not in visited:
                        visited.append(next_word)
                        queue.append((next_word,num+1))
                        
        return 0
               
