# Health Checker Application using AWS Bedrock
import boto3
from botocore.exceptions import ClientError
import json

def get_health_recommendations(symptoms):
    """
    Get health recommendations based on user symptoms using AWS Bedrock
    """
    # Create a Bedrock Runtime client
    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    
    # Set the model ID (using Claude 3)
    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    
    # Prepare the conversation context
    conversation = [
        {
            "role": "user",
            "content": [{"text": f"I'm experiencing the following symptoms: {symptoms}. Please provide medical advice based on these symptoms. Remember to recommend consulting a healthcare professional for serious conditions."}]
        }
    ]
    
    try:
        # Send the message to the model
        response = client.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={
                "maxTokens": 1024,
                "temperature": 0.7,
                "topP": 0.9
            }
        )
        
        # Extract and format the response
        response_text = response["output"]["message"]["content"][0]["text"]
        return response_text
        
    except (ClientError, Exception) as e:
        return f"Error getting health recommendations: {str(e)}"

def main():
    print("Welcome to Health Checker!")
    print("Please describe your symptoms and we'll provide recommendations.")
    print("(Note: This is not a substitute for professional medical advice)")
    
    symptoms = input("\nPlease describe your symptoms: ")
    recommendations = get_health_recommendations(symptoms)
    
    print("\nRecommendations:")
    print("-" * 50)
    print(recommendations)
    print("\nDisclaimer: These recommendations are for informational purposes only. Always consult a healthcare professional for medical advice.")

if __name__ == "__main__":
    main()
