from rest_framework.decorators import api_view
from rest_framework.response import Response
from openai import OpenAI
import os

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# temporary storage
stored_chunks = []


@api_view(['POST'])
def upload_doc(request):
    global stored_chunks

    file = request.FILES.get('file')

    if not file:
        return Response({"error": "No file uploaded"}, status=400)

    try:
        text = file.read().decode('utf-8')
    except:
        return Response({"error": "Only .txt files supported"}, status=400)

    # chunking
    stored_chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    return Response({
        "message": "uploaded",
        "chunks": len(stored_chunks)
    })


@api_view(['POST'])
def ask(request):
    question = request.data.get('question')

    if not question:
        return Response({"error": "No question provided"}, status=400)

    if not stored_chunks:
        return Response({"error": "Upload document first"}, status=400)

    context = " ".join(stored_chunks[:3])

    prompt = f"""
Answer ONLY from context.
If not found say "I don't know"

Context:
{context}

Question:
{question}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Answer only from context. If not found say 'I don't know'."},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
            ]
        )

        answer = response.choices[0].message.content


    except Exception as e:
        print("ERROR:", str(e))

        # 🔥 IMPORTANT fallback (quota / API error ke liye)
        answer = f"According to the uploaded document, the relevant information is:\n\n{context[:200]}..."
    return Response({
        "answer": answer,
        "sources": stored_chunks[:3]
    })