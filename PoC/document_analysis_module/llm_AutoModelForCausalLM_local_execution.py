from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

try:
    print("Inicio del proceso...")


    model_name = "EleutherAI/gpt-neo-1.3B"
    print(f"Cargando el modelo {model_name}...")
    model = AutoModelForCausalLM.from_pretrained(model_name)
    print("Carga exitosa")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    print("Modelo y tokenizer cargados correctamente.") 

    print("Configurando el pipeline...")
    nlp = pipeline("text-generation", model=model, tokenizer=tokenizer)
    print("Pipeline configurado correctamente.")  #
   
   
    context = "Me llamo juan"
    question = "¿Como me llamo?"
    prompt = f"{context} \n\n Pregunta: {question} \n Respuesta:"
    print(f"Prompt generado: {prompt}")


    print("Generando la respuesta...")
    response = nlp(prompt, max_length=200, do_sample=True)
    print("Respuesta generada.")

    if response:
        print("Respuesta generada:")
        print(response[0]['generated_text'])
    else:
        print("No se generó ninguna respuesta.")

except Exception as e:
    print(f"Se produjo un error: {e}")
