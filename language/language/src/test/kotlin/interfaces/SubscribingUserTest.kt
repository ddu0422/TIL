package interfaces

import org.junit.jupiter.api.Test

private const val EMAIL = "test@kotlinlang.org"

class SubscribingUserTest {

    @Test
    fun 닉네임_출력_테스트() {
        val privateUser: User = PrivateUser(EMAIL)
        println(privateUser.nickname)

        val subscribingUser: User = SubscribingUser(EMAIL)
        println(subscribingUser.nickname)
    }
}
