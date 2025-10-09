import os
import func
import simpliflow.smartagents as sim


from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env


# STEP 1: REQUIRED PARAMETERS
model = "gemini/gemini-2.5-pro"  # Choose the model you want to use in litellm style. Simpliflow supports 100+ models/providers through litellm. See here for a full list of providers: https://docs.litellm.ai/docs/providers/
# examples of models: "gpt-5-nano", "gemini/gemini-2.5-flash" , "gemini/gemini-2.5-pro","claude-sonnet-4-5", "command-r-plus", "huggingface/together/deepseek-ai/DeepSeek-R1","huggingface/meta-llama/Llama-3.3-70B-Instruct" , "huggingface/Qwen/Qwen3-VL-235B-A22B-Thinking", "command-nightly", "nvidia_nim/meta/llama3-70b-instruct", "groq/compound-mini"


# STEP 2: OPTIONAL PARAMETERS  
# If set to None, then their default values will be used for your chosen model.
# Remember all models may not support creativity, diversity, and max_tokens parameters. 
# If you set parameters that are not supported by your chosen model, simpliflow will simply drop those parameters.

creativity = temperature = 1.0
diversity = top_p = None 
max_tokens = 100000
# Many more parameters are supported. See here for a full list of supported parameters: https://docs.litellm.ai/docs/completion/input


# STEP 3: SOME MORE CONFIGURATION (agentsfile and dynamic_input)
# Agents file should be in the same directory. Provide its name. agentsfile cannot be None. After the agentsfile successfully runs, the output of the run will be stored as an appropriate named in interactions.json file in the Interactions directory.
agentsfile = os.path.join("Workflows", "Realtime-Action-Beeper.json")

# Dynamic Input is the input that would be available and required to start executing the flow. It would typically be the result from the previous processing stages of the application/program.
# If you have dynamic input that needs to be available to the first agent, then assign it here. 
# dynamic_input can be any object including custom objects, strings, numbers, lists, dictionaries, etc. But it should always be converted to string before passing it to the call_agents function.
# If you do not have any dynamic input, then set it to None.


# Here is an example of a custom object
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

dynamic_input = None

# STEP 4: RUN THE FLOW!
a, b = sim.call_agents(agentsfile, dynamic_input, model, creativity, diversity, max_tokens)

# STEP 5: OUTPUTS AVAILABLE!
# Print only the Last/Final Output of the flow.
print(a)
# Print all Intermediate and Final outputs of the flow.  These are also stored in the interactions.json file.
print(b)
