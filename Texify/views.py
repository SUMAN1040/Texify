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

    if not djText.strip():
        from django.http import HttpResponse
        return HttpResponse("Please enter some text to analyze.")

    purposes = []
    analyzed = djText

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
        temp = ""
        for char in analyzed:
            if char not in punctuations:
                temp += char
        analyzed = temp
        purposes.append('Removed Punctuation')

    if fullCap == "on":
        analyzed = analyzed.upper()
        purposes.append('Full Capitalization')

    if lineRemover == "on":
        temp = ""
        for char in analyzed:
            if char != "\n" and char != "\r":
                temp += char
        analyzed = temp
        purposes.append('Remove New Lines')

    if extraSpaceRemover == "on":
        temp = ""
        for index, char in enumerate(analyzed):
            if index < len(analyzed)-1 and analyzed[index] == " " and analyzed[index+1] == " ":
                pass
            else:
                temp += char
        analyzed = temp
        purposes.append('Remove Extra Spaces')

    char_count = None
    if charCounts == "on":
        char_count = len(analyzed.replace(" ", ""))
        purposes.append('Character Count')

    if not purposes:
        from django.http import HttpResponse
        return HttpResponse("Please select any operation and try again")

    params = {
        'purpose': ', '.join(purposes),
        'analyzed_text': analyzed,
    }
    if char_count is not None:
        params['char_count'] = char_count


    return render(request, 'analyze.html', params)