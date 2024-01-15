import os

from django.shortcuts import render
import openai
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings

# need OPEN-AI API KEY below
openai.api_key = settings.OPENAI_KEY


def call_openai_api(sys_content, user_content):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": sys_content},
                {"role": "user",
                 "content": user_content}
            ]
        )
    except:
        return "エラーが発生しました。"
    return completion.choices[0].message.content.strip()


def get_lang_string(val):
    # van to int
    val = int(val)
    if val == 1:
        return "日本語"
    elif val == 2:
        return "English"
    elif val == 3:
        return "简体中文"
    elif val == 4:
        return "繁體中文"


# Create your views here.
def index(request):
    # if you want to pass data to the template, you can do it like this
    # context = {'key': 'value'}
    # return render(request, 'index.html', context)
    return render(request, 'index.html')


def reply(request):
    return render(request, './pages/reply.html')

def privacy_policy(request):
    return render(request, './pages/privacy_policy.html')


@require_http_methods(["POST"])
def generate_email(request):
    try:
        # receive JSON data from Django
        data = json.loads(request.body)
        lang_string = get_lang_string(data['lang'])

        # system_content
        sys_content = f"Please create the body of the {lang_string} business email based on the following details..."
        user_content = "宛名:" + data['recipient'] + "\n" + "署名:" + data['signature'] + "\n" + "要件:" + data['text']

        # use call_openai_api function to call OpenAI API
        response = call_openai_api(sys_content, user_content)

        # return the result as JSON
        return JsonResponse({"result": response})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@require_http_methods(["POST"])
def add_emoji(request):
    try:
        # receive JSON data from Django
        data = json.loads(request.body)
        lang_string = get_lang_string(data['lang'])

        # Prepare the content to send to the OpenAI API
        sys_content = f"Add emojis to the following contents. Please use {lang_string}."
        user_content = "\n:" + data['text']

        # Call the OpenAI API with your prepared content
        # Here you would implement the chatgpt function or another way to call OpenAI API
        response = call_openai_api(sys_content, user_content)

        # Return the result as JSON
        return JsonResponse({"result": response})

    except json.JSONDecodeError:
        # You should return an HTTP 400 error if there's a problem with the JSON
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except KeyError:
        # If certain keys are not found in the JSON, return an error
        return JsonResponse({"error": "Missing data in request"}, status=400)

@require_http_methods(["POST"])
def more_polite(request):
    try:
        # receive JSON data from Django
        data = json.loads(request.body)
        lang_string = get_lang_string(data['lang'])

        # Prepare the content to send to the OpenAI API
        sys_content = f"Please make the following content more polite. Please use {lang_string}."
        user_content = data['text']

        # Call the OpenAI API with your prepared content
        # Here you would implement the chatgpt function or another way to call OpenAI API
        response = call_openai_api(sys_content, user_content)

        # Return the result as JSON
        return JsonResponse({"result": response})

    except json.JSONDecodeError:
        # You should return an HTTP 400 error if there's a problem with the JSON
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except KeyError:
        # If certain keys are not found in the JSON, return an error
        return JsonResponse({"error": "Missing data in request"}, status=400)

@require_http_methods(["POST"])
def generate_reply(request):
    try:
        # receive JSON data from Django
        data = json.loads(request.body)
        lang_string = "日本語"

        # system_content
        sys_content = f"メールを受信しました、返信要件に基づいて、メールの返信文を作成してください。メールは日本語で作成してください。"
        user_content = "受信したメール:" + data['receivedMail'] + "\n" + "返信要件:" + data['text']

        # use call_openai_api function to call OpenAI API
        response = call_openai_api(sys_content, user_content)

        # return the result as JSON
        return JsonResponse({"result": response})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)