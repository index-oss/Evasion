def analyze_response(url, html):
    findings = []

    if "sql" in html.lower() and "error" in html.lower():
        findings.append("Possible SQL error leakage")

    if "<script>" in html.lower():
        findings.append("Possible script reflection")

    return findings