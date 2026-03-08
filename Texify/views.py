from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")

def removePunch(request):

    djText = request.POST.get('Info', '')

    removepunc = request.POST.get('remove', 'off')
    fullCap = request.POST.get('fullCaps', 'off')
    lineRemover = request.POST.get('lineRemover', 'off')
    extraSpaceRemover = request.POST.get('spaceRemover', 'off')
    charCounts = request.POST.get('charCount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        for char in djText:
            if char not in punctuations:
                analyzed += char

        djText = analyzed
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}

    if fullCap == "on":
        analyzed = djText.upper()
        djText = analyzed
        params = {'purpose': 'Full Capitalization', 'analyzed_text': analyzed}

    if lineRemover == "on":
        analyzed = ""
        for char in djText:
            if char != "\n" and char != "\r":
                analyzed += char

        djText = analyzed
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}

    if extraSpaceRemover == "on":
        analyzed = ""
        for index, char in enumerate(djText):
            if index < len(djText)-1 and djText[index] == " " and djText[index+1] == " ":
                pass
            else:
                analyzed += char

        djText = analyzed
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}

    if charCounts == "on":
        count = len(djText.replace(" ", ""))
        params = {
            'purpose': 'Character Count',
            'analyzed_text': djText,
            'char_count': count
        }

    if(removepunc != "on" and fullCap != "on" and lineRemover != "on" and extraSpaceRemover != "on" and charCounts != "on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)