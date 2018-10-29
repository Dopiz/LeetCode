def uniqueMorseRepresentations(self, words):
    """
    :type words: List[str]
    :rtype: int
    """
    morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                "...","-","..-","...-",".--","-..-","-.--","--.."]

    if len(words) == 0:
        return 0
    
    tran_list = []
    for word in words:
        tran_word = ""
        for c in word:
            tran_word += morse_code[ord(c) - ord('a')]
        tran_list.append(tran_word)

    tran_list = set(list(tran_list))

    return len(tran_list)