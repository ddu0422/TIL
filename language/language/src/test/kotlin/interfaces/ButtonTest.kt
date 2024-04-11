package interfaces

import kotlin.test.Test

class ButtonTest {

    @Test
    fun 두_인터페이스_함수_호출() {
        val button = Button()
        button.showOff()
    }
}
