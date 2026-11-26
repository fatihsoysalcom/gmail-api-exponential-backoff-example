import time
import random

MAX_RETRIES = 5
INITIAL_BACKOFF_SECONDS = 1
MAX_BACKOFF_SECONDS = 60

def simulate_gmail_api_call(attempt):
    """
    Simulates a call to the Gmail API. It randomly fails for the first few attempts
    to demonstrate the need for a robust retry mechanism.
    """
    print(f"Attempt {attempt + 1}: Making a simulated Gmail API call...")
    # Simulate transient errors, like rate limits or temporary service unavailability.
    # For demonstration, it has a high chance to fail for the first few attempts.
    if attempt < 3 and random.random() < 0.7: # 70% chance to fail for first 3 attempts
        print(f"Attempt {attempt + 1}: Simulated API call FAILED (transient error).")
        return False
    else:
        print(f"Attempt {attempt + 1}: Simulated API call SUCCEEDED.")
        return True

def main():
    """
    Demonstrates making a robust API call with exponential backoff and jitter.
    This strategy is crucial for handling transient errors and rate limits,
    as discussed in the context of Google's new Gmail API policies.
    """
    current_backoff = INITIAL_BACKOFF_SECONDS

    print("--- Starting Gmail API Call Simulation with Exponential Backoff ---")
    for attempt in range(MAX_RETRIES):
        if simulate_gmail_api_call(attempt):
            print("\nAPI call successful after retries. Exiting.")
            return
        
        # If the call failed, apply exponential backoff.
        # This is the core concept for handling "timers" or rate limits
        # mentioned in the article about Google's new Gmail API policies.
        
        # Calculate jitter: a random delay to prevent "thundering herd" problem
        # where many clients retry at the exact same time.
        jitter = random.uniform(0, current_backoff * 0.1) # Add up to 10% jitter
        sleep_time = min(current_backoff + jitter, MAX_BACKOFF_SECONDS)
        
        print(f"Retrying in {sleep_time:.2f} seconds...")
        time.sleep(sleep_time)
        
        # Double the backoff time for the next attempt, up to a maximum.
        current_backoff = min(current_backoff * 2, MAX_BACKOFF_SECONDS)

    print("\nAll retry attempts failed. Could not complete the API call.")
    print("--- Simulation Finished ---")

if __name__ == "__main__":
    main()
