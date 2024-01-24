from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def ask_openai(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Thanks for everything!"},
            {"role": "user", "content": message}
        ]
    )
    answer = response.choices[0].message.content.strip()
    return answer


def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        message = user_message
        response = ask_openai(message)
        return JsonResponse({'message': user_message, 'response': response})
    
    return render(request, "bot/chatbot_template.html")