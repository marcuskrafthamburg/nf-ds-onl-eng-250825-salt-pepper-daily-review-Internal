
# Day 42, 31.10.2025 - Prompt Engineering

## __Basic Overview__

* Structure of prompts and their components
* Few-shot prompting for formatted outputs
* LangChain implementation with templates and chains

---

## __Prompt Structure__

A prompt typically consists of these components (not all are required but usually 2 or more for a _good_ prompt):

| Component | Description |
|---|---|
| **Instruction** | What the model should do |
| **External information/context** | Additional data provided to the model |
| **User input** | The specific query |
| **Output indicator** | Beginning format (e.g., "Answer:") |

**Example:**
```
Answer the question based on the context below. If the
question cannot be answered using the information provided answer
with "I don't know".

Context: [information here]

Question: {query}

Answer:
```

---

## __LLM Knowledge Sources__

* **Parametric knowledge**: Learned during training, stored in model parameters
* **Source knowledge**: Provided at inference time via the prompt

We can use prompts to provide additional context or examples as source knowledge.

---

## __LangChain Basics__

### Setup
```python
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.1, max_tokens=512)
output_parser = StrOutputParser()
```

### Prompt Template
```python
template = """Answer based on context.
Context: {context}
Question: {query}
Answer: """

prompt = PromptTemplate(input_variables=["context", "query"], template=template)
```

### Chain
A chain sequences components using `|`:
```python
chain = prompt | llm | output_parser
answer = chain.invoke({"context": "...", "query": "..."})
```

### Batch Processing
```python
questions = [{"question": "Q1?"}, {"question": "Q2?"}]
answers = chain.batch(questions)

for question, answer in zip(qs, answers):
    print(f"Question: {question['question']}")
    print(f"Answer: {answer.content.strip()}")
```

---

## __Few-Shot Prompting__

Provide examples in the prompt to show desired output format. Provide enough examples but don't overload.

**Without examples:** Generic output

**With examples:**
```python
template = """
Create a structured Markdown FAQ.

Example Input:
Q1: Do you ship internationally?
A1: Yes, we ship worldwide.

Example Output:
## Shipping
- **Do you ship internationally?**  
  Yes, we ship worldwide.

Now, create similar output for:
{input}
"""
```

Result: Model follows the demonstrated format.

---

## __FewShotPromptTemplate__

```python
from langchain_core.prompts import FewShotPromptTemplate

examples = [
    {
        'input': "Q1: Do you ship internationally?\nA1: Yes, worldwide.",
        'output': "## Shipping\n- **Do you ship internationally?**\n  Yes, worldwide."
    }
]

example_template = """Example input:
{input}
Example Output:
{output}"""

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template=example_template
)

few_shot = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Task instructions here",
    suffix="Now create output for:\n{input}",
    input_variables=["input"],
    example_separator="\n"
)

chain = few_shot | llm | output_parser
answer = chain.invoke({"input": "your input"})
```

---

## __Key Takeaways__

* Prompts guide model responses through structure and examples
* Few-shot prompting demonstrates desired output format
* LangChain templates use `{variables}` for dynamic content
* Chains connect: `prompt | llm | output_parser`
* Use `.invoke()` for single queries, `.batch()` for multiple

---

## __Helpful References__

* [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
* [NF GitHub Repo](https://github.com/neuefische/ds-prompt-engineering)
* [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)