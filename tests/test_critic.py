"""Tests for the Critic agent."""

import sys
import json
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.critic import CriticAgent, CriticReport, BugReport


class TestResponseParsing:
    """Test Critic response parsing from various formats."""

    def test_parse_clean_json(self):
        agent = CriticAgent.__new__(CriticAgent)
        raw = json.dumps({
            "verdict": "fail",
            "issues": [
                {
                    "line": 34,
                    "category": "A1",
                    "severity": "critical",
                    "description": "Uninitialized pointer dereference",
                    "fix": "Initialize pointer to NULL"
                }
            ],
            "fixed_code": "#include <stdint.h>\nint main(void) { return 0; }",
            "summary": "Found 1 critical issue.",
            "confidence": 0.92
        })
        report = agent.parse_response(raw)
        assert report.verdict == "fail"
        assert len(report.issues) == 1
        assert report.issues[0].severity == "critical"
        assert report.confidence == 0.92

    def test_parse_json_in_text(self):
        agent = CriticAgent.__new__(CriticAgent)
        raw = 'Here is my review:\n' + json.dumps({
            "verdict": "pass",
            "issues": [],
            "fixed_code": "",
            "summary": "Code looks good.",
            "confidence": 0.85
        }) + '\nEnd of review.'
        report = agent.parse_response(raw)
        assert report.verdict == "pass"
        assert len(report.issues) == 0

    def test_parse_json_in_code_block(self):
        agent = CriticAgent.__new__(CriticAgent)
        raw = '```json\n' + json.dumps({
            "verdict": "fail",
            "issues": [{"line": 10, "category": "B3", "severity": "high",
                        "description": "Missing clock enable", "fix": "Add RCC enable"}],
            "fixed_code": "fixed",
            "summary": "1 issue",
            "confidence": 0.8
        }) + '\n```'
        report = agent.parse_response(raw)
        assert report.verdict == "fail"
        assert report.issues[0].category == "B3"

    def test_format_report(self):
        agent = CriticAgent.__new__(CriticAgent)
        report = CriticReport(
            verdict="fail",
            issues=[BugReport(line=34, category="A1", severity="critical",
                              description="Uninitialized pointer", fix="Init to NULL")],
            summary="Found issues.",
            confidence=0.9,
        )
        text = agent.format_report(report)
        assert "FAIL" in text


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
