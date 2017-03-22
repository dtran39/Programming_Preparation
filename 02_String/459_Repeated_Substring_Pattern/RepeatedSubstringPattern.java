/*
Solution 1:
    When we see a character in str that matches the very first character of str, 
        we can start to hoping that str is a built by copies of the substring 
            composed by all characters before the reappearance of the its first character.

    O(n ^ 3): 
*/
public class Solution {
    public boolean repeatedSubstringPattern(String str) {
        // Base case
        int strLen = str.length();
        if(strLen == 1) {
            return false;
        }
        // Normal case
        StringBuilder sb = new StringBuilder();
        char firstChr = str.charAt(0);
        sb.append(firstChr);
        int i = 1;
        // Try from the first character to the n / 2 character to see if multiply each of those substring made the string
        while(i <= strLen / 2) {
            char c = str.charAt(i++);
            if(c == firstChr && isCopies(str, sb.toString())) {
                return true;
            }else {
                sb.append(c);
            }
        }
        return false;
    }
    // Function to check if a str is copies of multiple substr
    private boolean isCopies(String str, String substr) {
        if(str.length() % substr.length() != 0) {
            return false;
        }
        for(int i = substr.length(); i < str.length(); i += substr.length()){
            if(!str.substring(i).startsWith(substr)){
                return false;
            }
        }
        return true;
    }
}



