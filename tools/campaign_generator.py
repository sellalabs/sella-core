import random
import os
from datetime import datetime

hooks = {
    "luxury": [
        "Luxury is silence made visible.",
        "Minimalism is the new luxury.",
        "Quiet systems, powerful impact."
    ],
    "bold": [
        "The future doesn't ask permission.",
        "Break the narrative. Build something new.",
        "Bold ideas create new categories."
    ],
    "minimal": [
        "Less, but intentional.",
        "Clarity over complexity.",
        "Design reduced to essence."
    ]
}

styles = {
    "luxury": "cinematic minimalism and premium editorial aesthetics",
    "bold": "high-impact futuristic visual storytelling",
    "minimal": "clean, reduced, essential communication design"
}


def generate_variants(brand, audience, objective, tone):
    results = []

    for i in range(3):
        hook = random.choice(hooks[tone])
        style = styles[tone]

        results.append(f"""
# Campaign Variant {i+1}

Brand: {brand}
Audience: {audience}
Objective: {objective}

Hook: {hook}

Direction: {style}

Narrative:
{brand} focuses on {objective} targeting {audience}.
""")

    return results


def save_to_file(content):
    os.makedirs("examples", exist_ok=True)

    filename = f"examples/output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print("\nFILE SALVATO:")
    print(filename)


def main():
    print("\n--- SELLA CORE ENGINE ---\n")

    brand = input("Brand Name: ")
    audience = input("Target Audience: ")
    objective = input("Campaign Objective: ")
    tone = input("Tone (luxury/bold/minimal): ").strip().lower()

    if tone not in hooks:
        tone = "luxury"

    variants = generate_variants(brand, audience, objective, tone)

    final_output = "\n\n".join(variants)

    save_to_file(final_output)


if __name__ == "__main__":
    main()