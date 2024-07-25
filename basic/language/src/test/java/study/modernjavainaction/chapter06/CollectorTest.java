package study.modernjavainaction.chapter06;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import study.modernjavainaction.Car;

import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class CollectorTest {

    private List<Car> cars;

    @BeforeEach
    void setUp() {
        cars = List.of(
            new Car("car1", 1),
            new Car("car2", 1),
            new Car("car3", 3)
        );
    }

    @Test
    void groupingByExample() {
        // 자동차 위치 별로 자동차 이름 출력
        Map<Integer, List<String>> collect = cars.parallelStream()
            .collect(
                Collectors.groupingBy(
                    Car::getPosition,
                    Collectors.mapping(Car::getName, Collectors.toList()))
            );

        assertEquals(collect.get(1).size(), 2);
        assertEquals(collect.get(3).size(), 1);
    }

    @Test
    void maxByExample() {
        // Book Example
        Car bookCar = cars.parallelStream()
            .collect(Collectors.maxBy(Comparator.comparingInt(Car::getPosition)))
            .orElseThrow();

        assertEquals(3, bookCar.getPosition());

        // Refactoring
        Car exampleCar = cars.parallelStream()
            .max(Comparator.comparingInt(Car::getPosition))
            .orElseThrow();
        assertEquals(3, exampleCar.getPosition());
    }
}

