package clazz

class Client(val name: String, val age: Int) {

    override fun equals(other: Any?): Boolean {
        return if (other == null || other !is Client) {
            false
        } else {
            name == other.name && age == other.age
        }
    }

    override fun hashCode(): Int {
        return name.hashCode() * 31 + age
    }
}
