from fastapi import FastAPI

app = FastAPI()

# Create a POST endpoint to receive the webhook payload


@app.post("/webhook")
async def receive_webhook(payload: dict):

    # Check if the payload indicates an error (e.g., 'level' is 'ERROR')
    if payload.get('level') == 'ERROR':
        # Create a formatted string to display the alert details
        alert_details = f"Hey Error Alert! \n Details:\n" \
                        f"  Error Timestamp: {payload.get('timestamp')}\n" \
                        f"  Thread: {payload.get('thread')}\n" \
                        f"  Error Message: {payload.get('message')}\n" \
                        f"  Error Class: {payload.get('class')}"

        # Print the formatted alert details
        print(alert_details)

        # Return a response
        return {"message": "Received an error payload. Alert triggered."}
    else:
        # Return a response if the payload is not an error
        return {"message": "Payload received, not an error."}
