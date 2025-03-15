from flask import Flask, request, jsonify
import dialogflow_v2 as dialogflow

app = Flask(__name__)

# Initialize Dialogflow session client
DIALOGFLOW_PROJECT_ID = 'your-dialogflow-project-id'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'current-user-id'

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    query_result = req.get('queryResult')
    user_message = query_result.get('queryText')
    
    # Process the intent and respond accordingly
    if query_result.get('intent').get('displayName') == 'ApplyLeave':
        response_text = "Please provide the dates for your leave application."
    elif query_result.get('intent').get('displayName') == 'CheckLeaveBalance':
        response_text = "You have 10 days of leave remaining."
    else:
        response_text = "I didn't understand that. Can you please repeat?"

    return jsonify({'fulfillmentText': response_text})

if __name__ == '__main__':
    app.run(debug=True)
