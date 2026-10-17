
import pandas as pd

roll_number = input("Enter your roll number: ")

last_two = roll_number[-2:]
digit1 = int(last_two[0])
digit2 = int(last_two[1])

categories = ["billing", "account", "general"]

fixed_entries = [
    {
        "question": "what is the annual fee",
        "answer": "The annual fee is Rs 500.",
        "keywords": "fee cost price",
        "category": "billing"
    },
    {
        "question": "how to reset password",
        "answer": "Go to Settings > Reset Password.",
        "keywords": "password reset login",
        "category": "account"
    },
    {
        "question": "what are your working hours",
        "answer": "We are open 9 AM to 5 PM.",
        "keywords": "hours timing open",
        "category": "general"
    },
    {
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": "pay payment upi",
        "category": "billing"
    }
]

personalized1 = {
    "question": "how do i update my registered mobile number",
    "answer": "Go to Account Settings and update your registered mobile number.",
    "keywords": "mobile number update",
    "category": categories[digit1 % 3]
}

personalized2 = {
    "question": "how can i change my email address",
    "answer": "Go to Account Settings and update your email address.",
    "keywords": "email address change",
    "category": categories[digit2 % 3]
}

df = pd.DataFrame(fixed_entries + [personalized1, personalized2])
df.index = range(1,7)

display(df)

def score_query(query, df):
    query_words = set(query.lower().split())
    results = []

    for _, row in df.iterrows():
        text = (row["question"] + " " + row["keywords"]).lower()
        score = len(query_words.intersection(set(text.split())))

        if score > 0:
            results.append({
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "score": score
            })

    return sorted(results, key=lambda x: x["score"], reverse=True)


query = input("Enter your query: ")

for result in score_query(query, df):
    print(result)

def same_category(category_name, df):
    return df[df["category"] == category_name]["question"]


category_name = input("Enter catagory(billing/account/general: )")

print(same_category(category_name, df))

for i in range(1,len(df)+1):
    print(i, df.loc[i, "question"])

choice = int(input("Enter entry number: "))
new_keyword = input("Enter new keyword: ")

df.loc[choice, "keywords"] += " " + new_keyword

filename = roll_number + "_faq_data.csv"

df.to_csv(filename, index=False)

print(df)
print("Saved as:", filename)

print(df.groupby("category").size())

def score_query_with_ties(query, df):
    query_words = query.lower().split()
    results = []

    for _, row in df.iterrows():
        text = (row["question"] + " " + row["keywords"]).lower()
        score = sum(word in text.split() for word in query_words)

        if score > 0:
            results.append({
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "score": score
            })

    if not results:
        return []

    highest_score = max(result["score"] for result in results)

    return [result for result in results
            if result["score"] == highest_score]


query = input("Enter your query: ")

results = score_query_with_ties(query, df)

if results:
    print("\nMatching entries:")
    for result in results:
        print(result)
else:
    print("No matching entries found.")