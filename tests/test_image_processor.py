"""Tests for the image preprocessor."""

import sys
from pathlib import Path

import cv2
import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from pipeline.image_processor import ImageProcessor


@pytest.fixture
def processor():
    return ImageProcessor(max_dimension=512)


@pytest.fixture
def synthetic_image():
    """Create a synthetic circuit-like image (white bg, black lines)."""
    img = np.ones((800, 600, 3), dtype=np.uint8) * 255
    # Draw some rectangles (components)
    cv2.rectangle(img, (100, 100), (250, 200), (0, 0, 0), 2)
    cv2.rectangle(img, (350, 100), (500, 200), (0, 0, 0), 2)
    # Lines (wires)
    cv2.line(img, (250, 150), (350, 150), (0, 0, 0), 2)
    cv2.line(img, (175, 200), (175, 400), (0, 0, 0), 2)
    # Circle (LED/component)
    cv2.circle(img, (175, 450), 30, (0, 0, 0), 2)
    # Some text
    cv2.putText(img, "R1", (140, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    cv2.putText(img, "MCU", (380, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    return img


def test_preprocess_resizes(processor, synthetic_image):
    """Test that preprocessing resizes large images."""
    result = processor.preprocess(synthetic_image)
    h, w = result.shape[:2]
    assert max(h, w) <= 512


def test_preprocess_returns_grayscale(processor, synthetic_image):
    """Test that preprocessing returns a grayscale image."""
    result = processor.preprocess(synthetic_image)
    assert len(result.shape) == 2  # Grayscale = 2D array


def test_encode_base64(processor, synthetic_image):
    """Test base64 encoding produces valid string."""
    gray = cv2.cvtColor(synthetic_image, cv2.COLOR_BGR2GRAY)
    encoded = processor.encode_base64(gray)
    assert isinstance(encoded, str)
    assert len(encoded) > 100


def test_detect_components(processor, synthetic_image):
    """Test component detection finds regions."""
    gray = cv2.cvtColor(synthetic_image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    result = processor.detect_components(binary)
    assert "component_count" in result
    assert "estimated_complexity" in result
    assert result["estimated_complexity"] in ("simple", "moderate", "complex")


def test_prepare_for_gemma(processor, tmp_path):
    """Test full pipeline with a saved image."""
    img = np.ones((400, 300, 3), dtype=np.uint8) * 255
    cv2.rectangle(img, (50, 50), (150, 150), (0, 0, 0), 2)
    cv2.circle(img, (200, 200), 25, (0, 0, 0), 2)
    path = str(tmp_path / "test.png")
    cv2.imwrite(path, img)

    result = processor.prepare_for_gemma(path)
    assert "base64_image" in result
    assert "complexity" in result
    assert result["width"] > 0
    assert result["height"] > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
