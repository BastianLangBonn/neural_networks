package model;

public class BiasNeuron extends Neuron {

    public BiasNeuron() {
        setLastInducedLocalField(1);
        setLastOutput(1);
    }

    @Override
    public double activate() {
        setLastOutput(1);
        return 1;
    }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();
        result.append("Bias Neuron: ");
        result.append(super.toString());
        return result.toString();
    }

    @Override
    public double derivative() {
        System.out.println("Derivative for bias should never be needed");
        return 0;
    }

}
