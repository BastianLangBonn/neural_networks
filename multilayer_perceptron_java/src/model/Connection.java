package model;

public class Connection {

    private Neuron originNeuron;
    private Neuron targetNeuron;
    private double weight;

    public Connection(Neuron originNeuron, Neuron targetNeuron, double initialWeight) {
        this.originNeuron = originNeuron;
        this.targetNeuron = targetNeuron;
        this.weight = initialWeight;
    }

    public Neuron getOriginNeuron() {
        return originNeuron;
    }

    public double getWeight() {
        return weight;
    }

    public Neuron getTargetNeuron() {
        return targetNeuron;
    }

    public void setOriginNeuron(Neuron originNeuron) {
        this.originNeuron = originNeuron;
    }

    public void setTargetNeuron(Neuron targetNeuron) {
        this.targetNeuron = targetNeuron;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

}
