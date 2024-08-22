from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

class TextGenerationPipeline:
    def __init__(self, model_name="EleutherAI/gpt-neo-1.3B"):
        """
        Initializes the TextGenerationPipeline class by loading the specified model 
        and tokenizer, and setting up the text generation pipeline.

        Args:
            model_name (str): The name of the model to be used. Default is "EleutherAI/gpt-neo-1.3B".
        """
        try:
            print(f"Cargando el modelo {model_name}...")
            self.model = AutoModelForCausalLM.from_pretrained(model_name)
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            print("Modelo y tokenizer cargados correctamente.")

            print("Configurando el pipeline...")
            self.nlp = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)
            print("Pipeline configurado correctamente.")
        except Exception as e:
            print(f"Error al cargar el modelo o configurar el pipeline: {e}")
            raise

    def generate_prompt(self, context, question):
        """
        Generates a prompt by combining the given context and question.

        Args:
            context (str): The input text over which the question is asked.
            question (str): The question to be asked about the context.

        Returns:
            str: The combined prompt to be used for text generation.
        """
        prompt = f"{context} \n\n Pregunta: {question} \n Respuesta:"
        print(f"Prompt generado: {prompt}")
        return prompt

    def generate_response(self, prompt, max_length=200, do_sample=True):
        """
        Generates a response using the configured pipeline.

        Args:
            prompt (str): The prompt to be processed by the model.
            max_length (int): The maximum length of the generated text. Default is 200.
            do_sample (bool): Whether to use sampling; use greedy decoding otherwise. Default is True.

        Returns:
            str: The generated response text.
        """
        try:
            print("Generando la respuesta...")
            response = self.nlp(prompt, max_length=max_length, do_sample=do_sample)
            print("Respuesta generada.")
            if response:
                return response[0]['generated_text']
            else:
                print("No se generó ninguna respuesta.")
                return None
        except Exception as e:
            print(f"Error al generar la respuesta: {e}")
            raise

    def ask_question(self, context, question):
        """
        Combines the context and question, generates the prompt, and retrieves the response.

        Args:
            context (str): The input text over which the question is asked.
            question (str): The question to be asked about the context.

        Returns:
            str: The final response generated by the model.
        """
        prompt = self.generate_prompt(context, question)
        return self.generate_response(prompt)

if __name__ == "__main__":
    try:
        print("Inicio del proceso...")

        # Define the context and question
        context = "Me llamo juan"
        question = "¿Como me llamo?"

        # Create an instance of TextGenerationPipeline
        tgp = TextGenerationPipeline()

        # Generate the response based on the context and question
        response = tgp.ask_question(context, question)

        # Print the response
        if response:
            print("Respuesta generada:")
            print(response)
        else:
            print("No se generó ninguna respuesta.")

    except Exception as e:
        print(f"Se produjo un error: {e}")
