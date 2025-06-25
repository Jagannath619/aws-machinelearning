# Career Coach Application using AWS Bedrock
import boto3
from botocore.exceptions import ClientError

def get_career_advice(user_query, context=None):
    """
    Get career advice using AWS Bedrock
    """
    # Create a Bedrock Runtime client
    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    
    # Set the model ID
    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    
    # Prepare the conversation with context if provided
    messages = []
    if context:
        messages.append({"role": "assistant", "content": [{"text": context}]})
    
    messages.append({
        "role": "user",
        "content": [{"text": f"""I need career coaching help with: {user_query}
        Please provide professional advice. If relevant, consider these areas:
        1. Career path suggestions
        2. Resume and cover letter tips
        3. Interview preparation
        4. Skills development
        5. Industry insights
        
        Be specific and actionable in your response."""}]
    })
    
    try:
        response = client.converse(
            modelId=model_id,
            messages=messages,
            inferenceConfig={
                "maxTokens": 1024,
                "temperature": 0.7,
                "topP": 0.9
            }
        )
        
        return response["output"]["message"]["content"][0]["text"]
        
    except (ClientError, Exception) as e:
        return f"Error getting career advice: {str(e)}"

def main():
    print("\n🤖 Welcome to Career Coach! 🤖")
    print("I can help you with:")
    print("1. Career path exploration")
    print("2. Resume and cover letter writing")
    print("3. Interview preparation")
    print("4. Skills development")
    print("5. Job search strategies\n")
    
    context = None
    while True:
        print("\nWhat would you like help with? (or type 'exit' to quit)")
        user_input = input("> ").strip()
        
        if user_input.lower() == 'exit':
            print("\nThank you for using Career Coach! Good luck with your career journey! 🚀")
            break
            
        if not user_input:
            continue
            
        print("\n🔍 Analyzing your request...\n")
        response = get_career_advice(user_input, context)
        print(response)
        
        # Update context for follow-up questions
        context = f"Previous conversation: {user_input} - {response[:500]}"
        print("\n" + "="*80)
        print("💡 You can ask follow-up questions or type 'exit' to quit")

if __name__ == "__main__":
    main()
