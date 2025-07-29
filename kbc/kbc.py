print("Welcome to KBC made by ashutosh!\n")

kbl = [
    {
        "question": "Which of these is a popular Indian festival of lights?",
        "option": ["A. Holi", "B. Diwali", "C. Eid", "D. Christmas"],
        "answer": "B"
    },
    {
        "question": "Who is known as the ‘Father of the Indian Constitution’?",
        "option": ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. B. R. Ambedkar", "D. Sardar Vallabhbhai Patel"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the ‘Red Planet’?",
        "option": ["A. Venus", "B. Mars", "C. Jupiter", "D. Mercury"],
        "answer": "B"
    },
    {
        "question": "Who among the following was the first Indian to receive a Nobel Prize?",
        "option": ["A. C. V. Raman", "B. Mother Teresa", "C. Rabindranath Tagore", "D. Amartya Sen"],
        "answer": "C"
    },
    {
        "question": "Which Mughal emperor is known for building the Buland Darwaza at Fatehpur Sikri?",
        "option": ["A. Shah Jahan", "B. Akbar", "C. Humayun", "D. Aurangzeb"],
        "answer": "B"
    }
]

prize = [5000, 10000, 50000, 200000, 700000]
total = 0

for i, q in enumerate(kbl):
    print(f"\nQuestion {i+1}: {q['question']}")
    for opt in q["option"]:
        print(opt)
    
    a = input("Enter your answer (A, B, C, or D): ").strip().upper()

    if a == q["answer"]:
        print(f"🎉 Correct! You won ₹{prize[i]}")
        total += prize[i]
        print(f"💰 Total amount: ₹{total}")
    else:
        print("❌ Wrong answer!")
        print(f"💔 You lost. Total winnings: ₹{total}")
        break

if( total == '965000' ):
    print("itne pese ho gye ab toh tex bharna hi padega 😅 🤣")
