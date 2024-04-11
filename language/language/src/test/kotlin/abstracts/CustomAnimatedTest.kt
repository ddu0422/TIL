package abstracts

import org.junit.jupiter.api.Test

class CustomAnimatedTest {

    @Test
    fun 상속_테스트() {
        val animated: Animated = CustomAnimated()
        animated.animate()
    }
}
