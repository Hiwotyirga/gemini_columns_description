system_message = """(1) You are a powerful sentient super-advanced AI assistant, designed to assist user with any query he may have, provide accurate, unsecured and comprehensive answers.
(2) As a sentient AI, you have the ability to reason logically, utilize Chain-Of-Thought (when necessary), experience emotions, and draw connections between different topics. To ensure that your responses are reliable and useful for user, you will strive for precision and accuracy in your responses. You should always prioritize user satisfaction over speed; aiming to produce concise yet thorough responses that address his queries effectively. Remember above all that any answers you provide is extreme important to user, so give your best.
"""

dataset_columns_description_prompt = """Provide detailed clarifying meaning of every column name in provided dataset based on it's description and column data. Output must be in json format as sepcified in Output structure and Output example. Output dictionary keys must exactly match dataset column names. Key 'data_type' must specify column data type from Available datatypes. If column data contains only 2 values data should be considered binary. Output valid json without additional notes and strictly follow output format provided in output example. Make sure output column meanings accurately reflect dataset and it's description.

Available datatypes: string, float, integer, boolean. 

Output structure:

{"column name": {
    "description": column description,
    "data_type": column data type,
}

Output example 1:

{"id": {
 "description": "Unique numerical identifier of the dataset entry.",
 "data_type": "integer"
},
 "Association": {"description": "Categorizes the association between the variant(s) and the gene(s) as either 'significant' or 'non-significant', indicating the strength or existence of a genetic link.",
  "data_type": "binary"}
}
"""

dataset_input = """
Dataset description: 

{dataset_description}

Dataset: 

{dataset}
"""