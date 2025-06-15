import os
import func
import simpliflow.smartagents as sim


from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Print OpenAI API Key from the environment variables
# print(os.environ['OPENAI_API_KEY'])
# Print Claude API Key from the environment variables
# print(os.environ['ANTHROPIC_API_KEY'])
# print Cohere API Key from the environment variables
# print(os.environ['COHERE_API_KEY'])
# print DeepSeek API Key from claude-3-5-sonnetthe environment variables
# print(os.environ['DEEPSEEK_API_KEY'])
# print Gemini API Key from the environment variables
# print(os.environ['GEMINI_API_KEY'])


# STEP 1: REQUIRED PARAMETERS
vendor = "OpenAI"  # "OpenAI", "Anthropic" "Cohere", "DeepSeek","Google".  If assigned None, default is "OpenAI".
modelname = "gpt-4o" # Choose relevant models that go along with the vendors i.e. "gpt-4o", "gpt-3.5-turbo" ,"claude-3-5-sonnet-20241022", "claude-3-opus","claude-3-5-sonnet", "command-r-plus", "deepseek-chat", "deepseek-reasoner", "gemini-1.5-flash", "gemini-2.0-flash-exp", "gemini-2.0-flash-thinking-exp-01-21" # This is the modelname. If assigned None, default is "gpt-4o".

# STEP 2: OPTIONAL PARAMETERS  (If set to None, their default values will be used)
creativity = 0.7  # This is the temperature. If assigned None, default is 0.7
diversity = 0.85  # This is the top_p. If assigned None, default is 0.95
maxtokens = 1000  # This is the max token limit. If assigned None, default is 2000.  Other available values: 2000, 10000

# STEP 3: SOME MORE CONFIGURATION (agentsfile and dynamic_input)
# Agents file should be in the same directory. Provide its name. agentsfile cannot be None. After the agentsfile successfully runs, the output of the run will be stored as an appropriate named in interactions.json file in the Interactions directory.
agentsfile = os.path.join("Workflows", "ready (1).json")  

# Dynamic Input is the input that would be available and required to start executing the flow. It would typically be the result from the previous processing stages of the application/program.
# If you have dynamic input, assign it here. dynamic_input can be any object including custom objects, strings, numbers, lists, dictionaries, etc.
# But it should always be converted to string before passing it to the call_agents function.

# Example of a custom object
class Fruit:
    def __init__(self, name, color, size, price, linktobuy):    
        self.name = name
        self.color = color
        self.size = size
        self.price = price
        self.linktobuy = linktobuy

    def __repr__(self):
        return f"Fruit({self.name}, {self.color}, {self.size}, {self.price}, {self.linktobuy})"

    def __str__(self):
        return f"Fruit Description Fruit A {self.color}, {self.size}, {self.name}. Price: {self.price}. Link to buy: {self.linktobuy}"
        
    
apple = Fruit("apple", "red", "large", "$3.00/lb", "https://usapple.org/")

dynamic_input = apple
# Always convert dynamic input to string
dynamic_input = str(dynamic_input)  # or repr(dynamic_input)  for your custom objects/classes.

# If you do not have dynamic input, then assign None to dynamic_input.
dynamic_input = None

# STEP 4: RUN THE FLOW!
a, b = sim.call_agents(agentsfile, dynamic_input, vendor, modelname, creativity, diversity, maxtokens)

# STEP 5: OUTPUTS AVAILABLE!
# Print only the Last/Final Output of the flow.
print(a)
# Print all Intermediate and Final outputs of the flow.  These are also stored in the interactions.json file.
print(b)
