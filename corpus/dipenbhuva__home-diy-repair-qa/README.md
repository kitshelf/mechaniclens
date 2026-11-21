---
language:
- en
license: apache-2.0
task_categories:
- question-answering
- text-generation
tags:
- home-repair
- diy
- synthetic
- instruction-tuning
- qa
- how-to
- finetuning
pretty_name: Home DIY Repair Q&A
size_categories:
- 1K<n<10K
dataset_info:
  - config_name: default
    features:
      - name: id
        dtype: string
      - name: category
        dtype: string
      - name: question
        dtype: string
      - name: answer
        dtype: string
      - name: equipment_problem
        dtype: string
      - name: tools_required
        sequence: string
      - name: steps
        sequence: string
      - name: safety_info
        dtype: string
      - name: tips
        sequence: string
    splits:
      - name: train
        num_examples: 4000
      - name: eval
        num_examples: 1000
configs:
  - config_name: default
    data_files:
      - split: train
        path: train.jsonl
      - split: eval
        path: eval.jsonl
---

# Home DIY Repair Q&A

A synthetic dataset of **5,000 Q&A pairs** covering common home DIY repair scenarios. Each example includes a detailed step-by-step answer, required tools, safety warnings, and practical tips.

## Dataset Purpose

This dataset is built for:

- **Instruction fine-tuning** — train language models to give detailed, safe, and actionable home repair guidance
- **Retrieval-Augmented Generation (RAG)** — build a knowledge base for home repair assistants
- **Question answering** — train or evaluate models on structured how-to responses
- **Embedding fine-tuning** — learn representations of repair problems and solutions

## Dataset Structure

Each example is a structured Q&A pair about a home repair problem.

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier (e.g., `qa_00001`) |
| `category` | string | Repair category |
| `question` | string | User's home repair question |
| `answer` | string | Complete natural language answer with safety info, steps, and tips |
| `equipment_problem` | string | Short description of the problem |
| `tools_required` | list[string] | Tools needed for the repair |
| `steps` | list[string] | Step-by-step repair instructions |
| `safety_info` | string | Safety warnings and precautions |
| `tips` | list[string] | Additional practical tips |

### Splits

| Split | Examples |
|-------|----------|
| `train` | 4,000 |
| `eval` | 1,000 |

### Categories

The dataset covers 5 categories, evenly distributed (1,000 each before splitting):

| Category | Description | Train | Eval |
|----------|-------------|-------|------|
| `appliance_repair` | Washing machines, dishwashers, refrigerators, etc. | 785 | 215 |
| `plumbing_repair` | Toilets, faucets, drains, pipes | 804 | 196 |
| `electrical_repair` | Outlets, switches, wiring, fixtures | 794 | 206 |
| `hvac_maintenance` | Thermostats, furnaces, AC units, air quality | 814 | 186 |
| `general_home_repair` | Doors, walls, flooring, windows, etc. | 803 | 197 |

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

dataset = load_dataset("dipenbhuva/home-diy-repair-qa")

train = dataset["train"]
eval_set = dataset["eval"]

print(train[0])
```

### Instruction Fine-tuning

Format examples as instruction-response pairs:

```python
def format_for_finetuning(example):
    return {
        "instruction": example["question"],
        "response": example["answer"],
    }

formatted = dataset["train"].map(format_for_finetuning)
```

### Using Structured Fields

Access individual components for custom formatting:

```python
example = dataset["train"][0]

print("Problem:", example["equipment_problem"])
print("Tools:", example["tools_required"])
print("Safety:", example["safety_info"])
for i, step in enumerate(example["steps"], 1):
    print(f"  {i}. {step}")
print("Tips:", example["tips"])
```

## Example

```json
{
  "id": "qa_00001",
  "category": "appliance_repair",
  "question": "My washing machine is not filling with water. How do I fix this?",
  "answer": "Before you begin, an important safety note: Turn off both water supply valves before disconnecting hoses...",
  "equipment_problem": "Washing machine not filling with water",
  "tools_required": ["adjustable pliers", "toothbrush", "bucket", "towels"],
  "steps": [
    "Check that both the hot and cold water supply faucets behind the machine are fully open",
    "Inspect the inlet hoses for kinks or pinches that could restrict water flow",
    "Turn off the water supply and disconnect the hoses from the back of the machine",
    "Clean the inlet filter screens inside the hose connections with a toothbrush",
    "Reconnect the hoses hand-tight plus a quarter turn with pliers",
    "Turn the supply valves back on and run a fill cycle to verify water enters the machine"
  ],
  "safety_info": "Turn off both water supply valves before disconnecting hoses. Have towels and a bucket ready.",
  "tips": [
    "Clogged inlet screens are the most common cause of fill problems — clean them every year",
    "If the machine fills slowly, the water supply valves may not be fully open"
  ]
}
```

## Generation

This dataset was synthetically generated using OpenAI's API with 5 diverse prompt templates, followed by Pydantic schema validation, quality validation (6 rules), and LLM-as-Judge failure analysis. The pipeline achieved a 100% structural validity rate and 80% quality pass rate, with the primary failure mode being overcomplicated solutions.

## Limitations

- **Synthetic data**: Generated by an LLM, not written by professional repair technicians. Instructions should be verified before use on real repairs.
- **English only**: All text is in English.
- **General guidance**: Answers provide general approaches and may not cover all makes/models or local building codes.
- **Safety**: While safety info is included, always consult a licensed professional for electrical, gas, or structural work.

## Citation

```bibtex
@dataset{home_diy_repair_qa,
  title={Home DIY Repair Q&A},
  author={dipenbhuva},
  year={2025},
  url={https://huggingface.co/datasets/dipenbhuva/home-diy-repair-qa}
}
```
