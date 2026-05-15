"""Tests for the Architect agent."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.architect import ArchitectAgent


class TestCodeExtraction:
    """Test code extraction from various response formats."""

    def test_extract_c_code_block(self):
        text = 'Here is the code:\n```c\n#include <stdint.h>\nint main(void) { return 0; }\n```\nDone.'
        code = ArchitectAgent.extract_code_from_response(text)
        assert "#include <stdint.h>" in code
        assert "int main" in code

    def test_extract_plain_code_block(self):
        text = 'Code:\n```\n#include <stdint.h>\nvolatile uint32_t *ptr = (volatile uint32_t *)0x40021000;\nint main(void) { return 0; }\n```'
        code = ArchitectAgent.extract_code_from_response(text)
        assert "#include" in code

    def test_extract_no_code_block_but_has_code(self):
        text = '#include <stdint.h>\n#define RCC 0x40021000\nint main(void) {\n  return 0;\n}'
        code = ArchitectAgent.extract_code_from_response(text)
        assert "int main" in code

    def test_extract_no_code_raises(self):
        with pytest.raises(ValueError):
            ArchitectAgent.extract_code_from_response("No code here, just text.")

    def test_extract_longest_block(self):
        text = (
            '```c\nshort\n```\n\nFull code:\n```c\n'
            '#include <stdint.h>\n'
            'void SystemInit(void) {}\n'
            'int main(void) { while(1); return 0; }\n'
            '```'
        )
        code = ArchitectAgent.extract_code_from_response(text)
        assert "SystemInit" in code  # Should pick the longer block


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
