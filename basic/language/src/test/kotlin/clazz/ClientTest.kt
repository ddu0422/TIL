package clazz

import org.junit.jupiter.api.Test
import kotlin.test.assertTrue

class ClientTest {

    @Test
    fun equals_확인() {
        assertTrue { Client(name = "이두호", age = 30) == Client(name = "이두호", age = 30) }
    }

    @Test
    fun hashCode_확인() {
        val set = hashSetOf(Client(name = "이두호", age = 30))
        set.add(Client(name = "이두호", age = 30))

        assertTrue { set.contains(Client(name = "이두호", age = 30)) }
        assertTrue { set.size == 1 }
    }
}
