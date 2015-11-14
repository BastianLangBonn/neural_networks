import java.util.Arrays;
import java.util.List;

import model.MLP;

/**
 * 
 * @author bastian
 * 
 */
public class Main {
    public static void main(String[] args) {
        MLP mlp = new MLP(2, 2, 1, 0.0);
        System.out.println(mlp);
        List<Double> input = Arrays.asList(0.0, 0.0);
        System.out.println(mlp.propagate(input));

        for (int i = 0; i < 10000; i++) {
            mlp.backpropagate(Arrays.asList(0.0, 0.0), Arrays.asList(0.0), 1.0);
            mlp.backpropagate(Arrays.asList(1.0, 0.0), Arrays.asList(1.0), 1.0);
            mlp.backpropagate(Arrays.asList(0.0, 1.0), Arrays.asList(1.0), 1.0);
            mlp.backpropagate(Arrays.asList(1.0, 1.0), Arrays.asList(0.0), 1.0);
        }

        System.out.println(mlp);
        System.out.println(mlp.propagate(Arrays.asList(0.0, 0.0)));
        System.out.println(mlp.propagate(Arrays.asList(1.0, 0.0)));
        System.out.println(mlp.propagate(Arrays.asList(0.0, 1.0)));
        System.out.println(mlp.propagate(Arrays.asList(1.0, 1.0)));
    }
}