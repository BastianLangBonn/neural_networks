package model;

public class InputNeuron extends Neuron {

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();
        result.append("Input Neuron: ");
        result.append(super.toString());
        return result.toString();
    }

    @Override
    public double activate() {
        setLastOutput(getLastInducedLocalField());
        return getLastOutput();
    }

    @Override
    public double derivative() {
        System.out.println("Derivative of input neuron should never be needed.");
        return 0;
    }
}
