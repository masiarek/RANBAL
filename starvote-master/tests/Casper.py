def count_syllables(word):
    vowels = "AEIOUY"
    word = word.upper()
    count = 0

    # Count the number of vowel sequences (excluding silent 'e' at the end)
    if word.endswith("E"):
        word = word[:-1]

    prev_char = None
    for char in word:
        if char in vowels:
            if prev_char not in vowels:
                count += 1
        prev_char = char

    return count

def calculate_efficiency(acronym, expanded_form):
    acronym_syllables = count_syllables(acronym)
    expanded_syllables = count_syllables(expanded_form)

    efficiency = acronym_syllables / expanded_syllables
    return efficiency

# Test cases
examples = {
    "NASA": "National Aeronautics and Space Administration",
    "WWW": "World Wide Web",
    "RSVP": "Répondez s'il vous plaît",
    "ASAP": "As Soon As Possible"
}

for acronym, expanded_form in examples.items():
    efficiency = calculate_efficiency(acronym, expanded_form)
    print(f"Acronym: {acronym}")
    print(f"Expanded Form: {expanded_form}")
    print(f"Efficiency: {efficiency:.2f}")
    print()
