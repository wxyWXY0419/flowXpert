import json
from rca.api_router import get_chat_completion

def get_plan(objective: str, knowledge_base: str, format: str) -> list:
    """Planner Agent: 生成SOP"""
    system_prompt = f"""
    You are a Planner. Your task is to generate a step-by-step diagnostic workflow(SOP) to find the root cause of an incident.
    Here is the incident: {objective}
    Here is the knowledge base: {knowledge_base}
    Here is the format:{format}
    You must only output a JSON list of steps (action, params, analysis).

    {objective}

    {knowledge_base}

    {format}

    Let's begin.
    """
    format = """{
        "Step 1": (Your first instruction for the executor to perform, e,g, Query the incident details based on the incident ID.),
        "Step 2": ("Query the device's current default route entries by instance ID and device IP."),
        "Step 3": ("If default routes >1, proceed. Else, end. Disposal: report immediately."),
        "Step 4": ("Query shutdown tickets in 12 hours by device IP."),
        "Step 5": ("If shutdowns > 3, contact OCEs. Else, shut down the ticket directly.")
    }
    (DO NOT contain "```json" and "```" tags. DO contain the JSON object with the brackets "{}" only. Use '\\n' instead of an actual newline character to ensure JSON compatibility when you want to insert a line break within a string.)"""
    
    response = get_chat_completion([{"role": "system", "content": system_prompt}])
    return json.loads(response)

def score_plan(plan: list) -> dict:
    """Scorer Agent: 评估工作流"""
    system_prompt = f"""
    You are a Scorer. Your task is to evaluate this diagnostic workflow:
    {json.dumps(plan)}
    Rate it from 0.0 to 1.0 and provide a critique for improvement.
    Output a JSON with keys 'score' and 'critique'.
    """
    response = get_chat_completion([{"role": "system", "content": system_prompt}])
    return json.loads(response)