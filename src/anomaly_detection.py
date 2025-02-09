import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd

def build_autoencoder(input_dim):
    model = keras.Sequential([
        keras.layers.Dense(32, activation='relu', input_shape=(input_dim,)),
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(input_dim, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def train_anomaly_model():
    df = pd.read_csv("data/telemetry.csv").drop(columns=["timestamp"])
    model = build_autoencoder(df.shape[1])
    model.fit(df.values, df.values, epochs=10, batch_size=32, validation_split=0.1)
    model.save("models/anomaly_detector.h5")

train_anomaly_model()

