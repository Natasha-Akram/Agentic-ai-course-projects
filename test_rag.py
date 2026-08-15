from retriever import get_retriever


def test_retriever():
    retriever = get_retriever()

    questions = [
        "Which laptop is best for programming under PKR 150,000?",
        "What is the return policy?",
        "Is delivery free for an order above PKR 100,000?",
        "Which device is best for reading and study?"
    ]

    for question in questions:
        print("\n" + "=" * 70)
        print("QUESTION:")
        print(question)

        documents = retriever.invoke(question)

        print("\nRETRIEVED INFORMATION:")

        for i, doc in enumerate(documents, start=1):
            print(f"\n--- Document {i} ---")
            print(doc.page_content)


if __name__ == "__main__":
    test_retriever()