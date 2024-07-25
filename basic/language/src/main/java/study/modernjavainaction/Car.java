package study.modernjavainaction;

public class Car {

    private final String name;
    private final int position;

    public Car(String name, int position) {
        this.name = name;
        this.position = position;
    }

    public String getName() {
        return name;
    }

    public int getPosition() {
        return position;
    }

    @Override
    public String toString() {
        return "Car{" + "name='" + name + '\'' + ", position=" + position + '}';
    }
}

