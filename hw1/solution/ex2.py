def extract_title(html_string):
    starttag = '<title>'
    endtag = '</title>'
    start = html_string.find(starttag) + len(starttag)
    end = html_string.find(endtag, start)
    if start > 6 and end != -1:
        return html_string[start:end]
    return ""  # Return an empty string if no title tag is found