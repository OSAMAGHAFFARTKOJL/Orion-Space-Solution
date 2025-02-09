from autogen import UserProxyAgent, AssistantAgent

user_proxy = UserProxyAgent(name="User", human_input_mode="ALWAYS")

data_agent = AssistantAgent(name="DataProcessor", system_message="You process telemetry data.")
anomaly_agent = AssistantAgent(name="AnomalyDetector", system_message="You detect anomalies.")
predictive_agent = AssistantAgent(name="PredictiveMaintenance", system_message="You predict failures.")
decision_agent = AssistantAgent(name="DecisionMaker", system_message="You make autonomous decisions.")

def orion_ai_pipeline(telemetry_data):
    response = user_proxy.initiate_chat(
        data_agent, message=f"Process telemetry data: {telemetry_data}"
    )
    response = anomaly_agent.initiate_chat(message="Detect anomalies")
    response = predictive_agent.initiate_chat(message="Predict failures")
    response = decision_agent.initiate_chat(message="Make a decision")

    return response

