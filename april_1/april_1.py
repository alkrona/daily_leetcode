def lengthOfLastWord(s: str) -> int:
    
    modified_word = s.rstrip(" ")
    modified_word_array = modified_word.split()

    return(len(modified_word_array[-1]))
if __name__=="__main__":
    print(lengthOfLastWord(" yolo is my savior     "))
        