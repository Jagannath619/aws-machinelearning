import boto3
from botocore.exceptions import ClientError
import json
from typing import Dict, List, Optional

class TravelAgent:
    def __init__(self):
        self.client = boto3.client("bedrock-runtime", region_name="us-east-1")
        self.model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
        
    def generate_response(self, prompt: str, context: str = "") -> str:
        """Generic method to get response from Bedrock"""
        try:
            messages = [{"role": "user", "content": [{"text": f"{context}\n\n{prompt}"}]}]
            
            response = self.client.converse(
                modelId=self.model_id,
                messages=messages,
                inferenceConfig={
                    "maxTokens": 1024,
                    "temperature": 0.7,
                    "topP": 0.9
                }
            )
            return response["output"]["message"]["content"][0]["text"]
        except (ClientError, Exception) as e:
            return f"Error: {str(e)}"

class DestinationExpert(TravelAgent):
    def get_recommendations(self, preferences: Dict) -> str:
        prompt = f"""Based on these travel preferences:
        - Budget: {preferences.get('budget', 'Not specified')}
        - Travel Dates: {preferences.get('dates', 'Flexible')}
        - Group: {preferences.get('group', 'Not specified')}
        - Interests: {', '.join(preferences.get('interests', []))}
        
        Please suggest 3-5 destinations with pros and cons for each."""
        
        system_prompt = """You are a world-traveled destination expert. Provide personalized 
        destination recommendations based on the user's preferences. For each destination, 
        include 1-2 sentences about why it matches their interests, budget considerations, 
        and any seasonal factors."""
        
        return self.generate_response(prompt, system_prompt)

class ItineraryArchitect(TravelAgent):
    def create_itinerary(self, destination: str, preferences: Dict) -> str:
        prompt = f"""Create a detailed {preferences.get('duration', 3)}-day itinerary for {destination}.
        Traveler preferences:
        - Interests: {', '.join(preferences.get('interests', []))}
        - Budget: {preferences.get('budget', 'Moderate')}
        - Travel Style: {preferences.get('travel_style', 'Balanced')}
        
        Include activities, dining, and travel times."""
        
        system_prompt = """You are a professional travel planner. Create a detailed, realistic 
        itinerary that matches the traveler's pace and interests. Include time buffers, 
        travel times between locations, and a good mix of activities and rest."""
        
        return self.generate_response(prompt, system_prompt)

class LocalGuide(TravelAgent):
    def get_local_insights(self, location: str, activity: str) -> str:
        prompt = f"""Provide local insights for {activity} in {location}.
        Include:
        1. Local tips and etiquette
        2. Best times to visit
        3. Hidden gems nearby
        4. Basic local phrases
        5. Any safety considerations"""
        
        system_prompt = """You are a knowledgeable local guide. Provide authentic, 
        practical advice that only locals would know. Be specific and include 
        recent information."""
        
        return self.generate_response(prompt, system_prompt)

class TripGenie:
    def __init__(self):
        self.dest_expert = DestinationExpert()
        self.itinerary_arch = ItineraryArchitect()
        self.local_guide = LocalGuide()
        self.current_plan = {}
    
    def start_planning(self):
        print("\n🌍 Welcome to TripGenie - Your AI Travel Planning Assistant! 🌟")
        print("I'll help you plan your perfect trip with three expert AI assistants!")
        
        # Get travel preferences
        preferences = self.get_travel_preferences()
        
        # Step 1: Get destination recommendations
        print("\n🔍 Analyzing your preferences...")
        print("\n📌 Your Personalized Destination Recommendations:")
        destinations = self.dest_expert.get_recommendations(preferences)
        print(destinations)
        
        # Step 2: Select destination and create itinerary
        destination = input("\n✈️  Which destination would you like to explore? ")
        print(f"\n📅 Creating your {destination} itinerary...")
        
        itinerary = self.itinerary_arch.create_itinerary(destination, preferences)
        print("\n✨ Your Custom Itinerary:")
        print(itinerary)
        
        # Step 3: Get local insights
        print("\n💡 Would you like local insights for any specific activity? (or type 'done')")
        while True:
            activity = input("\n🏷️  Activity: ").strip()
            if activity.lower() == 'done':
                break
            if activity:
                print("\n🧭 Fetching local insights...")
                insights = self.local_guide.get_local_insights(destination, activity)
                print(f"\n{insights}")
        
        print("\n🎉 Your trip is all planned! Safe travels! 🧳✈️")
    
    def get_travel_preferences(self) -> dict:
        print("\nLet's start with some basic information:")
        preferences = {
            'budget': input("💰 What's your travel budget (e.g., $2000, Mid-range)? "),
            'dates': input("📅 When are you planning to travel? "),
            'duration': input("⏳ How many days will your trip be? "),
            'group': input("👥 Who's traveling with you (e.g., solo, couple, family with kids)? "),
            'interests': input("🌟 What are your main interests (e.g., beaches, history, food)? ").split(','),
            'travel_style': input("🚶‍♂️ What's your travel style (Relaxed/Moderate/Fast-paced)? ")
        }
        return preferences

def main():
    planner = TripGenie()
    planner.start_planning()

if __name__ == "__main__":
    main()
