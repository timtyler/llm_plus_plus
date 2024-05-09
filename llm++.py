import sys
import google.generativeai as genai

def query_gemini(user_prompt):
  """
  Queries Gemini API with a user prompt, and return the preferred response.
  Args:
    user_prompt: The user's query/prompt.
  Returns:
    A response based on an internal evaluation.
  """

  # Read API token from file
  with open("gemini_api_token.txt", "r") as f:
    api_token = f.read().strip()

  # Configure the model with the API token
  genai.configure(api_key=api_token)
  model = genai.GenerativeModel('gemini-1.5-pro-latest')

  # Construct the prompt
  gemini_prompt = f"""At the bottom of this query is a user prompt, preceeded by the line:
"Here is the original user prompt:". Output the string "Research results". Then output the results of any research which might plausibly help to generate an accurate response to the original user prompt.<BR>
Next, output the string "Chain of thought". Then generate and output a response to the original user prompt with " Let's think step by step." appended to it - while bearing any research in mind.<BR>
Next, output the string "Critical review stage". Next generate and output a critical review of the answer. Check accuracy, logic and include a smoke test to catch any obvious mistakes.<BR>
Finally, output the string "Final answer". Next generate and output a response to the user's query - bearing in mind the chain of thought reasoning and the critical review.
Here is the original user prompt:
{user_prompt}"""

  gemini_response = model.generate_content(gemini_prompt)
  response_text = gemini_response.text
  print(response_text)
  return response_text.split("Final answer")[1].strip()

# Access specific arguments
script_name = sys.argv[0]
prompt_string = sys.argv[1]  # Make sure enough arguments are provided

preferred_response = query_gemini(prompt_string)
#print(preferred_response)
