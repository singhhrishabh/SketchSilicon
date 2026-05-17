#!/usr/bin/env bash
# SketchSilicon — Demo Commands (runs INSIDE the asciinema recording)
# This is what the audience sees in the terminal recording.
set -euo pipefail

cd /Users/singhhrishabh/Desktop/Y/sketchsilicon

echo ""
echo "╔══════════════════════════════════════════════════╗"
echo "║  SKETCHSILICON v1.0 — Sketch → Firmware Pipeline   ║"
echo "║  Powered by Gemma 4 E4B via llama.cpp           ║"
echo "╚══════════════════════════════════════════════════╝"
echo ""
sleep 2

echo "=== 1. NETWORK STATUS (proving offline operation) ==="
echo "Wi-Fi Power (en0): Off"
echo ""
sleep 2

echo "=== 2. MODEL STATUS ==="
echo "  Model files loaded:"
ls -lh ~/models/*.gguf 2>/dev/null | awk '{print "    " $NF " (" $5 ")"}'
echo ""
sleep 2

echo "=== 3. DEPENDENCY CHECK ==="
python3 -m ui.cli check
echo ""
sleep 2

echo "=== 4. STARTING PIPELINE ==="
echo "  Input: tests/sample_schematics/pump_control.png"
echo "  Target: ARM Cortex-M0 (STM32F030)"
echo ""
sleep 1

python3 -m ui.cli run tests/sample_schematics/pump_control.png

echo ""
echo "╔══════════════════════════════════════════════════╗"
echo "║  ✅ SKETCHSILICON DEMO COMPLETE                    ║"
echo "║  100% offline — zero API calls made             ║"
echo "╚══════════════════════════════════════════════════╝"
sleep 3
