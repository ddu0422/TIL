package interfaces

interface User {
    val nickname: String
}

class PrivateUser(override val nickname: String) : User
class SubscribingUser(private val email: String) : User {
    override val nickname: String
        get() = email.substringBefore('@')
}
class FacebookUser(accountId: Int) : User {
    override val nickname = getFacebookName(accountId)

    private fun getFacebookName(accountId: Int): String {
        return "Test Nickname"
    }
}
