from transformers import pipeline

try:
    print("Inicio del proceso...")

    print("Cargando el modelo y configurando el pipeline...")
    pipe = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")
    print("Pipeline configurado correctamente.")  

    context = "Me llamo juan"
    question = "¿quien habla?"
    prompt = f"{context} \n\n Pregunta: {question} \n Respuesta:"
    print(f"Prompt generado: {prompt}")

    print("Generando la respuesta...")
    response = pipe(prompt, max_length=50, do_sample=True)
    print("Respuesta generada.")

    if response:
        print("Respuesta generada:")
        print(response[0]['generated_text'])
    else:
        print("No se generó ninguna respuesta.")

except Exception as e:
    print(f"Se produjo un error: {e}")

input("Presiona Enter para finalizar...")
