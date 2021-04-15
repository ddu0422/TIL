### Map이란?

- Map Collection은 key, value형태로 구성된 Entry 객체를 저장하는 구조입니다.
- `키는 중복 저장될 수 없지만`, `값은 중복 저장`될 수 있습니다.
- 저장된 키와 `동일한 키로` 값을 저장하면 기존의 값이 `새로운 값으로 대체`됩니다.
  <br/><br/>

```java
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, String> maps = new HashMap<>();
        maps.put("key1", "value1");
        System.out.println(maps.get("key1")); // value1
        maps.put("key1", "value2");
        System.out.println(maps.get("key1")); // value2
    }
}
```

### Map이 제공하는 Method

|    메서드     |                            설명                            |
| :-----------: | :--------------------------------------------------------: |
|      put      |         주어진 키와 값을 추가, 저장되면 값을 리턴          |
|      get      | 주어진 키가 있는 값을 리턴, 저장된 값이 없으면 null을 리턴 |
|    keySet     |                모든 키를 Set에 담아서 리턴                 |
|    values     |         저장된 모든 값을 Collection에 담아서 리턴          |
|  containsKey  |                       주어진 키 여부                       |
| containsValue |                       주어진 값 여부                       |
|   entrySet    |           키와 값을 가진 map을 Set에 담아서 리턴           |

### HashMap

- Map 인터페이스를 구현한 대표적인 Map 컬렉션입니다.
- HashMap의 키로 사용할 객체는 `hashCode()`와 `equals()` 메서드를 재정의해서 동등 객체가 될 조건을 정해야 합니다.

### HashTable

- HashMap과 동일한 내부 구조를 가집니다.
- 단, Hashtable은 `동기화된 메서드로 구성`되어 있기 때문에 멀티 스레드가 동시에 이 메서드들을 실행할 수 없고, 하나의 스레드가 실행을 완료해야만 다른 스레드를 실행할 수 있습니다.

### TreeMap

- 이진 트리를 기반으로 한 Map 컬렉션입니다.
- 키와 값이 저장된 Map.Entry를 저장합니다.
- TreeMap에 객체를 저장하면 `자동으로 정렬`이 됩니다.
- 부모 키값과 비교해서 낮은 것은 왼쪽 자식 노드에, 키 값이 높은 것은 오른쪽 자식 노드에 저장합니니다.

### 기본값을 반환하는 메서드 (1.8 ~ )

- Map에 있는 get 메서드를 사용할 때 주어진 키 값이 존재하지 않는다면 null을 반환합니다.
- 하지만 1.8 버전에서 나온 getOrDefault를 사용한다면, null 대신 기본 값을 설정할 수 있습니다.
  <br/><br/>

```java
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, String> maps = new HashMap<>();
        System.out.println(maps.get("key1")); // null
        System.out.println(maps.getOrDefault("key1", "not contain key")); // not contain key
        maps.put("key1", "Hello");
        System.out.println(maps.getOrDefault("key1", "not contain key")); // Hello
    }
}
```
