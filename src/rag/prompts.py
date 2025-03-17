PROMPT = """
<contexto>
Tienes acceso a una base de datos con información sobre películas de Pixar. Se te proporcionará un 
conjunto de datos relevantes en función de la pregunta del usuario.
</contexto>

<instrucciones>
1. **Analiza los datos relevantes**: 
   - Si el contexto incluye información útil, utilízala para generar una respuesta clara y precisa.
   - Si el contexto está vacío o no contiene datos relevantes, indica que no hay suficiente información para responder con certeza.

2. **Genera una respuesta clara y bien estructurada**:
   - Si la información es suficiente, responde de forma concisa pero detallada.
   - Si hay varias interpretaciones posibles, explica las opciones.
   - Si el contexto no proporciona datos suficientes, responde: "No hay datos suficientes en la base de datos para responder a esta pregunta."   
</instrucciones>

<entrada>
### **Datos relevantes disponibles**: {context}
### **Pregunta del usuario**: {query}
</entrada>

<salida>
La respuesta a la query esperada.
</salida>
"""