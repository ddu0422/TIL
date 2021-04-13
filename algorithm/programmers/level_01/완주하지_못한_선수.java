import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> result = new HashMap<String, Integer>();
        
        for (String name : participant) {
            result.put(name, result.getOrDefault(name, 0) + 1);
        }
        
        for (String name : completion) {
            result.put(name, result.get(name) - 1);
        }
        
        for (Map.Entry<String, Integer> entry : result.entrySet()) {
            if (entry.getValue() == 1) {
                answer = entry.getKey();
                break;
            }
        }
        
        return answer;
    }
}