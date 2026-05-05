from rest_framework.decorators import api_view
from rest_framework.response import Response
from openai import OpenAI

client = OpenAI()

# temporary storage
stored_chunks = []

@api_view(['POST'])
def upload_doc(request):
    global stored_chunks
    file = request.FILES.get('file')

    text = file.read().decode('utf-8')

    # simple chunking
    stored_chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    return Response({"message": "uploaded", "chunks": len(stored_chunks)})


@api_view(['POST'])
def ask(request):
    question = request.data.get('question')

    context = " ".join(stored_chunks[:3])

    prompt = f"""
Answer ONLY from context.
If not found say "I don't know"

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    return Response({
        "answer": answer,
        "sources": stored_chunks[:3]
    })