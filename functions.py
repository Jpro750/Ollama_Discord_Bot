import ollama

def generate_answer(prompt):
    modelo = "gemma3:1b"
    response = ollama.chat(model=modelo, messages=[{"role": "user", "content": prompt}])
    return   response["message"]["content"]
