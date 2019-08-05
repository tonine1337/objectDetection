package com.cognizant.Interactive.objectdetection.customview;

import com.cognizant.Interactive.objectdetection.tflite.Classifier;

import java.util.List;

public interface ResultsView {
    public void setResults(final List<Classifier.Recognition> results);
}
