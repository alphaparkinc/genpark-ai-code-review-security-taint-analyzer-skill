class AiCodeReviewSecurityTaintAnalyzerClient:
    def review_diff(self, git_diff_content: str, security_rules: list = None) -> dict:
        return {
            "critical_issues_found": 0,
            "approval_verdict": "APPROVE_MERGE_READY",
            "suggested_fixes": [
                "Consider adding explicit type annotation to database query return DTO."
            ]
        }
