#!/usr/bin/env bash
# SketchSilicon — Demo Recording Script
# Records a terminal demo as .cast then converts to GIF
# Usage: ./demo/record_demo.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

GREEN='\033[0;32m'; RED='\033[0;31m'; CYAN='\033[0;36m'; NC='\033[0m'

# Check dependencies
if ! command -v asciinema &>/dev/null; then
    echo -e "${RED}✗ asciinema not installed. Run: brew install asciinema${NC}"
    exit 1
fi

# Check WiFi status (Cactus track proof)
# WIFI_STATUS=$(networksetup -getairportpower en0 2>/dev/null | grep -c "Off" || true)
# if [ "$WIFI_STATUS" -eq 0 ]; then
#     echo -e "${RED}⚠️  Turn off WiFi first for Cactus track proof${NC}"
#     echo -e "  Run: networksetup -setairportpower en0 off"
#     echo -e "  Then re-run this script."
#     exit 1
# fi

# Check server is running
if ! curl -sf "http://localhost:8080/health" &>/dev/null; then
    echo -e "${RED}✗ llama.cpp server not running. Start it first:${NC}"
    echo -e "  cd $PROJECT_DIR && ./start_server.sh"
    exit 1
fi

# Set terminal size
printf '\e[8;35;120t'

echo -e "${CYAN}Recording starts in...${NC}"
sleep 1; echo "  3..."
sleep 1; echo "  2..."
sleep 1; echo "  1..."
sleep 1

# Record
asciinema rec "$SCRIPT_DIR/raw_recording.cast" \
    --overwrite \
    --cols 120 --rows 35 \
    -c "bash $SCRIPT_DIR/demo_commands.sh"

echo -e "\n${GREEN}✓ Recording saved: $SCRIPT_DIR/raw_recording.cast${NC}"

# Convert to GIF if agg is available
if command -v agg &>/dev/null; then
    echo -e "${CYAN}Converting to GIF...${NC}"
    agg "$SCRIPT_DIR/raw_recording.cast" "$SCRIPT_DIR/sketchsilicon_demo.gif" \
        --cols 120 --rows 35 --speed 1.5
    echo -e "${GREEN}✓ GIF saved: $SCRIPT_DIR/sketchsilicon_demo.gif${NC}"
elif command -v asciinema-agg &>/dev/null; then
    echo -e "${CYAN}Converting to GIF...${NC}"
    asciinema-agg "$SCRIPT_DIR/raw_recording.cast" "$SCRIPT_DIR/sketchsilicon_demo.gif" \
        --cols 120 --rows 35 --speed 1.5
    echo -e "${GREEN}✓ GIF saved: $SCRIPT_DIR/sketchsilicon_demo.gif${NC}"
else
    echo -e "  ${RED}No GIF converter found. Install: pip3 install asciinema-agg${NC}"
    echo -e "  Then convert manually:"
    echo -e "  agg $SCRIPT_DIR/raw_recording.cast $SCRIPT_DIR/sketchsilicon_demo.gif --speed 1.5"
fi

echo -e "\n${GREEN}Done! Don't forget to re-enable WiFi:${NC}"
echo -e "  networksetup -setairportpower en0 on"
