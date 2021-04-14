import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);
        Map<String, String> maps = new HashMap<>();

        for (String phoneNumber : phone_book) {
            maps.put(phoneNumber, phoneNumber);
        }

        for (String phoneNumber : phone_book) {
            for (int i = 1; i < phoneNumber.length(); i++) {
                if (maps.get(phoneNumber.substring(0, i)) != null) {
                    answer = false;
                    break;
                }
            }
        }

        return answer;
    }
}