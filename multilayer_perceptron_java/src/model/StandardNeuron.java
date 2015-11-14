package model;

public class StandardNeuron extends Neuron {

    @Override
    public double activate() {
        double activation = computeActivation();
        setLastOutput(activation);
        return activation;
    }

    private double computeActivation() {
        double activation = 1.0 / (1 + Math.exp(getLastInducedLocalField() * (-1)));
        return activation;
    }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();
        result.append("Standard Neuron: ");
        result.append(super.toString());
        return result.toString();
    }

    @Override
    public double derivative() {
        return computeActivation() * (1 - computeActivation());
    }

}
