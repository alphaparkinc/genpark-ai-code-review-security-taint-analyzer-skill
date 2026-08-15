from client import AiCodeReviewSecurityTaintAnalyzerClient

def main():
    client = AiCodeReviewSecurityTaintAnalyzerClient()
    diff = "+ const token = process.env.API_KEY;
+ await fetch(endpoint, { headers: { Authorization: token } });"
    res = client.review_diff(diff)
    print(f"Approval Verdict: {res['approval_verdict']}")
    print(f"Issues Found: {res['critical_issues_found']}")
    print("Suggestions:", res["suggested_fixes"])

if __name__ == "__main__":
    main()
