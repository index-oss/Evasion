from urllib.parse import urlparse
import ssl, socket

def score_url(url):
    score = 0
    p = urlparse(url)

    if p.scheme != "https":
        score += 2

    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=p.hostname) as s:
            s.settimeout(3)
            s.connect((p.hostname, 443))
    except:
        score += 3

    if score >= 3:
        return "Risky"
    elif score == 2:
        return "Suspicious"
    else:
        return "Safe"
