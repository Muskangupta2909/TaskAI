from rest_framework.decorators import api_view
from rest_framework.response import Response
from openai import OpenAI
import os

# SAFE way (env se key lega)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("API KEY:", os.getenv("OPENAI_API_KEY"))

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
        return Response({"error": "File must be .txt"}, status=400)

    stored_chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    return Response({
        "message": "uploaded",
        "chunks": len(stored_chunks)
    })


@api_view(['POST'])
def ask(request):
    question = request.data.get('question')

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
            messages=[{"role": "user", "content": prompt}]
        )

        answer = response.choices[0].message.content

    except Exception as e:
        return Response({"error": str(e)}, status=500)

    return Response({
        "answer": answer,
        "sources": stored_chunks[:3]
    })