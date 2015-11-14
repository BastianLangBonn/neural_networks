package model;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class MLP {

    private final List<Neuron> inputLayer = new LinkedList<Neuron>();
    private final List<Neuron> hiddenLayer = new LinkedList<Neuron>();
    private final List<Neuron> outputLayer = new LinkedList<Neuron>();
    private final Neuron bias = new BiasNeuron();

    public MLP(int numberInputNeurons, int numberHiddenNeurons, int numberOutputNeurons, double initialWeight) {

        createInputLayer(numberInputNeurons);
        createFullyConnectedLayer(inputLayer, hiddenLayer, numberHiddenNeurons, initialWeight);
        createFullyConnectedLayer(hiddenLayer, outputLayer, numberOutputNeurons, initialWeight);

    }

    private void createInputLayer(int numberInput) {
        for (int i = 0; i < numberInput; i++) {
            Neuron inputNeuron = new InputNeuron();
            inputLayer.add(inputNeuron);
        }
    }

    private void createFullyConnectedLayer(List<Neuron> originLayer, List<Neuron> targetLayer, int layerSize,
            double initialWeight) {
        for (int i = 0; i < layerSize; i++) {
            Neuron targetNeuron = new StandardNeuron();
            for (Neuron originNeuron : originLayer) {
                Connection connection = new Connection(originNeuron, targetNeuron, initialWeight);
                originNeuron.addOutgoingConnection(connection);
                targetNeuron.addIncomingConnection(connection);
            }
            Connection connection = new Connection(bias, targetNeuron, initialWeight);
            targetNeuron.addIncomingConnection(connection);
            targetLayer.add(targetNeuron);
        }
    }

    public List<Double> propagate(List<Double> input) {
        for (int i = 0; i < inputLayer.size(); i++) {
            Neuron inputNeuron = inputLayer.get(i);
            inputNeuron.setLastInducedLocalField(input.get(i));
            inputNeuron.activate();
        }

        propagateThroughLayer(hiddenLayer);
        propagateThroughLayer(outputLayer);

        ArrayList<Double> result = new ArrayList<Double>();
        for (Neuron neuron : outputLayer) {
            result.add(neuron.getLastOutput());
        }
        return result;
    }

    private void propagateThroughLayer(List<Neuron> layer) {
        for (Neuron neuron : layer) {
            neuron.computeInducedLocalField();
            neuron.activate();
        }
    }

    public void backpropagate(List<Double> input, List<Double> desiredOutput, double learningRate) {
        List<Double> netOutput = propagate(input);
        // Compute delta for output neurons and change incoming weights
        for (int i = 0; i < outputLayer.size(); i++) {
            double error = desiredOutput.get(i) - netOutput.get(i);
            Neuron neuron = outputLayer.get(i);
            neuron.setLastDelta(error * neuron.derivative());
            changeIncomingWeightsForNeuron(learningRate, neuron);
        }

        // Compute delta for hidden neurons and change their incoming weights
        for (Neuron neuron : hiddenLayer) {
            double summedDelta = 0;
            for (Connection outgoingConnection : neuron.getOutgoingConnections()) {
                summedDelta += outgoingConnection.getWeight() * outgoingConnection.getTargetNeuron().getLastDelta();
            }
            neuron.setLastDelta(neuron.derivative() * summedDelta);
            changeIncomingWeightsForNeuron(learningRate, neuron);
        }
    }

    private void changeIncomingWeightsForNeuron(double learningRate, Neuron neuron) {
        for (Connection incomingConnection : neuron.getIncomingConnections()) {
            double weightChange = neuron.getLastDelta() * learningRate
                    * incomingConnection.getOriginNeuron().getLastOutput();
            incomingConnection.setWeight(incomingConnection.getWeight() + weightChange);
        }
    }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();
        result.append("MLP:\nInput Layer:\n");
        for (Neuron neuron : inputLayer) {
            result.append(neuron.toString() + "\n");
        }
        result.append("\nHidden Layer:\n");
        for (Neuron neuron : hiddenLayer) {
            result.append(neuron.toString() + "\n");
        }
        result.append("\nOutput Layer:\n");
        for (Neuron neuron : outputLayer) {
            result.append(neuron.toString() + "\n");
        }
        return result.toString();
    }
}
