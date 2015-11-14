package model;

import java.util.LinkedList;
import java.util.List;

public abstract class Neuron {

    private double lastInducedLocalField;
    private double lastDelta;
    private double lastOutput;
    private final List<Connection> outgoingConnections;
    private final List<Connection> incomingConnections;

    public Neuron() {
        outgoingConnections = new LinkedList<Connection>();
        incomingConnections = new LinkedList<Connection>();
    }

    public void addOutgoingConnection(Connection connection) {
        outgoingConnections.add(connection);
    }

    public void addIncomingConnection(Connection connection) {
        incomingConnections.add(connection);
    }

    public List<Connection> getIncomingConnections() {
        return incomingConnections;
    }

    public List<Connection> getOutgoingConnections() {
        return outgoingConnections;
    }

    public double getLastDelta() {
        return lastDelta;
    }

    public double getLastOutput() {
        return lastOutput;
    }

    public double getLastInducedLocalField() {
        return lastInducedLocalField;
    }

    public abstract double activate();

    public double computeInducedLocalField() {
        double result = 0;
        for (Connection connection : incomingConnections) {
            result += connection.getWeight() * connection.getOriginNeuron().getLastOutput();
        }
        setLastInducedLocalField(result);
        return result;
    }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();
        result.append(String.format("Number of incomming connections: %d. ", getIncomingConnections().size()));
        result.append("weights:[");
        for (Connection connection : incomingConnections) {
            result.append(connection.getWeight() + " ");
        }
        result.append("]");
        result.append(String.format("Number of outgoing connections: %d. ", getOutgoingConnections().size()));
        return result.toString();
    }

    public void setLastOutput(double lastOutput) {
        this.lastOutput = lastOutput;
    }

    public void setLastDelta(double lastDelta) {
        this.lastDelta = lastDelta;
    }

    public void setLastInducedLocalField(double lastInducedLocalField) {
        this.lastInducedLocalField = lastInducedLocalField;
    }

    public abstract double derivative();
}