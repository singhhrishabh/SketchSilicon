# Reproducing the SketchSilicon Pipeline

This document provides exact, step-by-step instructions for judges, educators, or makers to independently reproduce the SketchSilicon pipeline on their own hardware.

## Prerequisites
- macOS (Apple Silicon/Intel) or Linux
- Python 3.9+
- Homebrew (macOS) or APT (Linux)

---

## 1. Environment Setup

Clone the repository and run the setup script. This script automatically installs `arm-none-eabi-gcc` for compiling ARM Cortex-M0 firmware, `llama.cpp` for local inference, and Python dependencies.

```bash
git clone https://github.com/singhhrishabh/SketchSilicon.git
cd SketchSilicon
./setup.sh
```

## 2. Model Downloads

SketchSilicon relies on the quantized **Gemma 4 E4B Instruct** model and its vision adapter.

If the `./setup.sh` script did not download them automatically, you can download them manually using the `huggingface-cli`:

```bash
# Ensure the models directory exists
mkdir -p ~/models

# Download the main language model (Q4_K_M quantization)
huggingface-cli download unsloth/gemma-4-E4B-it-GGUF gemma-4-E4B-it-Q4_K_M.gguf --local-dir ~/models

# Download the multimodal vision adapter (mmproj)
huggingface-cli download unsloth/gemma-4-E4B-it-GGUF mmproj-BF16.gguf --local-dir ~/models
```

## 3. Start the Offline AI Server

Start the `llama.cpp` server. This exposes a local, OpenAI-compatible API endpoint that the Architect and Critic agents use to generate and review code.

```bash
# Make sure you are in the SketchSilicon directory
./start_server.sh
```

You should see an output indicating the server is running on `http://127.0.0.1:8080`.
At this point, **you can completely disable your internet connection (Wi-Fi off).**

## 4. Run the Pipeline

With the server running, you can invoke the CLI to process a schematic image into a compiled binary. We've provided a test schematic for you to run:

```bash
# Run the pipeline on the sample LED blink schematic
python3 -m ui.cli run tests/sample_schematics/led_blink.png
```

If you want to skip the QEMU simulation step, use the `--no-simulate` flag:

```bash
python3 -m ui.cli run --no-simulate tests/sample_schematics/led_blink.png
```

## 5. Verify the Output

Once the pipeline finishes, the final output will be exactly one production-ready C file containing the generated firmware, correctly formatted to the image name. 

```bash
# Check the generated firmware
cat output/led_blinkfirmware.c
```

If you didn't use the `--no-simulate` flag, the terminal will also output a detailed performance report including the execution runtime inside the `qemu-system-arm` emulator.
