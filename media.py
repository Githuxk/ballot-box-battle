def generate_headline(state, problem, choice_key, choice):
    """Return a list of headline lines showing how different outlets frame
    the same government decision (the 'Mask' mechanic from the design bible)."""
    lines = [
        f'GOVERNMENT: "Decisive action taken on {problem["title"].lower()}"',
        f'OPPOSITION: "Government response to {problem["title"].lower()} falls short"',
    ]
    if state["media_pressure"] > 50 or state["public_anger"] > 50:
        lines.append(f'INDEPENDENT: "What will \'{choice["label"]}\' actually achieve?"')
    if state["public_anger"] > 65:
        lines.append("SOCIAL MEDIA: #WHATSTHEPLAN is trending nationally.")
    return lines

