from llama_cpp import Llama

model = Llama(model_path="models/clave-f16.gguf")

dataset = [
    {"input": "What is the capital of France?", "label": "Paris"},
    {"input": "Who wrote 'Romeo and Juliet'?", "label": "William Shakespeare"},
    {"input": "What is the chemical symbol for water?", "label": "H2O"},
    {"input": "What planet is known as the Red Planet?", "label": "Mars"},
    {"input": "Who painted the Mona Lisa?", "label": "Leonardo da Vinci"},
    {"input": "What is 15 multiplied by 3?", "label": "45"},
    {"input": "Which gas do plants absorb from the atmosphere?", "label": "Carbon dioxide"},
    {"input": "In which continent is Egypt located?", "label": "Africa"},
    {"input": "What is the largest mammal in the world?", "label": "Blue whale"},
    {"input": "Who discovered gravity after observing a falling apple?", "label": "Isaac Newton"},
    {"input": "Which ocean is the largest on Earth?", "label": "Pacific Ocean"},
    {"input": "What is the boiling point of water in Celsius?", "label": "100"},
    {"input": "Which country is known as the Land of the Rising Sun?", "label": "Japan"},
    {"input": "Who was the first president of the United States?", "label": "George Washington"},
    {"input": "What is 12 minus 7?", "label": "5"},
    {"input": "What is the main language spoken in Brazil?", "label": "Portuguese"},
    {"input": "Which organ pumps blood through the human body?", "label": "Heart"},
    {"input": "Who wrote 'Pride and Prejudice'?", "label": "Jane Austen"},
    {"input": "Which planet is closest to the Sun?", "label": "Mercury"},
    {"input": "What is the chemical symbol for gold?", "label": "Au"},
    {"input": "What is 9 divided by 3?", "label": "3"},
    {"input": "Which country has the Great Wall?", "label": "China"},
    {"input": "Who invented the telephone?", "label": "Alexander Graham Bell"},
    {"input": "What is the largest planet in the solar system?", "label": "Jupiter"},
    {"input": "What is the freezing point of water in Celsius?", "label": "0"},
    {"input": "Which element has the atomic number 1?", "label": "Hydrogen"},
    {"input": "Who painted the ceiling of the Sistine Chapel?", "label": "Michelangelo"},
    {"input": "What is 7 multiplied by 6?", "label": "42"},
    {"input": "Which continent is known for kangaroos?", "label": "Australia"},
    {"input": "Who is known as the father of modern physics?", "label": "Albert Einstein"},
    {"input": "What is the largest desert in the world?", "label": "Sahara"},
    {"input": "What is the chemical formula for table salt?", "label": "NaCl"},
    {"input": "Who wrote '1984'?", "label": "George Orwell"},
    {"input": "Which is the smallest prime number?", "label": "2"},
    {"input": "Which gas do humans exhale?", "label": "Carbon dioxide"},
    {"input": "Who discovered penicillin?", "label": "Alexander Fleming"},
    {"input": "Which river is the longest in the world?", "label": "Nile"},
    {"input": "What is 8 plus 15?", "label": "23"},
    {"input": "What is the main ingredient in bread?", "label": "Flour"},
    {"input": "Who was the first person to walk on the Moon?", "label": "Neil Armstrong"},
    {"input": "Which country is famous for the Eiffel Tower?", "label": "France"},
    {"input": "What is the atomic number of oxygen?", "label": "8"},
    {"input": "Who is the author of 'The Odyssey'?", "label": "Homer"},
    {"input": "What is 14 divided by 2?", "label": "7"},
    {"input": "Which continent is home to the Amazon rainforest?", "label": "South America"},
    {"input": "Who painted 'Starry Night'?", "label": "Vincent van Gogh"},
    {"input": "What is the fastest land animal?", "label": "Cheetah"},
    {"input": "Which planet has rings around it?", "label": "Saturn"},
    {"input": "What is the currency of Japan?", "label": "Yen"},
    {"input": "Who formulated the theory of evolution?", "label": "Charles Darwin"},
    {"input": "Which metal is liquid at room temperature?", "label": "Mercury"},
    {"input": "What is 20 minus 9?", "label": "11"},
    {"input": "Which country is known for pyramids?", "label": "Egypt"}
]


preds = []
labels = []

for item in dataset:
    output = model(item["input"], max_tokens=50)
    pred = output['choices'][0]['text'].strip()
    preds.append(pred)
    labels.append(item['label'])
    print(f"Input: {item['input']}")
    print(f"Prediction: {pred} | Label: {item['label']}")
    print("------")

accuracy = sum(p == l for p, l in zip(preds, labels)) / len(labels)
print("Final Accuracy:", accuracy)