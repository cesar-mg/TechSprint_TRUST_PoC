from transformers import pipeline

try:
    print("Inicio del proceso...")

    print("Cargando el modelo y configurando el pipeline...")
    pipe = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")
    print("Pipeline configurado correctamente.")  

    context = "Se adjudica el contrato a la persona RAMON CONCEPCION PLACENCIA, con el Registro Nacional de Contribuyentes (RNC) Numero. 049-0030912-3 habilitado para contratar con el Estado mediante el Registro de Proveedor Núm."
    question = "¿Como se llama la persona se le adjudica el contrato? No me interesa el Registro Nacional de Contribuyentes"
    prompt = f"{context} \n\n Pregunta: {question} \n Respuesta:"
    print(f"Prompt generado: {prompt}")

    print("Generando la respuesta...")
    response = pipe(prompt, max_length=150, do_sample=True)
    print("Respuesta generada.")

    if response:
        print("Respuesta generada:")
        print(response[0]['generated_text'])
    else:
        print("No se generó ninguna respuesta.")

except Exception as e:
    print(f"Se produjo un error: {e}")

input("Presiona Enter para finalizar...")
