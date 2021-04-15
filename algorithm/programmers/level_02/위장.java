package programmers.level2;

import java.util.HashMap;
import java.util.Map;

public class Disguise {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> maps = new HashMap<>();

        for (String[] clothe : clothes) {
            String part = clothe[1];
            // 고르지 않는 경우를 포함
            maps.put(part, maps.getOrDefault(part, 1) + 1);
        }

        for (Integer value : maps.values()) {
            answer *= value;
        }

        return answer - 1;
    }
}
