# FieldForge — Submission Checklist

## Kaggle Writeup
- [ ] Writeup submitted on Kaggle (not draft)
- [ ] Writeup ≤1,500 words (currently ~1,450)
- [ ] Track selected: Global Resilience + Cactus + llama.cpp
- [ ] Sections: Problem, Solution, Architecture, Technical Evidence, Impact, Prize Tracks
- [ ] Real metrics cited (instruction count, binary size, stack depth)
- [ ] llama.cpp usage documented
- [ ] Offline operation documented

## Video
- [ ] YouTube video uploaded (≤3 min, public, no login required)
- [ ] Video linked in Kaggle submission Attachments → Project Links
- [ ] Opening creates emotional urgency within 20 seconds
- [ ] WiFi-off shown on screen (hold for 3 seconds)
- [ ] llama.cpp server loading visible (~5 seconds screen time)
- [ ] Critic bug-catch shown (timestamp ~1:00)
- [ ] Bug table with line numbers visible
- [ ] Fix applied and recompile shown
- [ ] Resource score shown (timestamp ~2:00)
- [ ] Final panel held for 5 seconds
- [ ] Closing story matches opening

## GitHub Repository
- [ ] Repository is public
- [ ] README.md with setup instructions
- [ ] All source code committed
- [ ] Sample schematics included (LED blink + pump control)
- [ ] Apache 2.0 LICENSE file added
- [ ] GitHub repo linked in Kaggle submission Attachments → Project Links

## Kaggle Submission Assets
- [ ] Cover image uploaded to Media Gallery
- [ ] WiFi-off screenshot in Media Gallery
- [ ] llama.cpp server screenshot in Media Gallery
- [ ] Critic bug-catch terminal screenshot in Media Gallery

## Live Demo
- [ ] Live demo URL linked (or alternative: Wokwi project link)
- [ ] Demo works with the sample schematics

## Technical Requirements
- [ ] Gemma 4 model used (E4B via llama.cpp)
- [ ] llama.cpp is the serving framework
- [ ] Multimodal capability demonstrated (image → code)
- [ ] Function calling demonstrated (compile_firmware tool)
- [ ] Offline operation proven (WiFi disabled during demo)
- [ ] Real compilation (arm-none-eabi-gcc)
- [ ] Real metrics (arm-none-eabi-size output)

## Pre-Submission
- [ ] `python -m pytest tests/ -v` — all tests pass
- [ ] `python -m ui.cli check` — all dependencies green
- [ ] `python -m ui.cli demo` — full pipeline runs successfully
- [ ] Demo video recorded and reviewed
- [ ] Writeup proofread (no filler phrases, no jargon without explanation)
- [ ] All code publicly accessible before deadline

## Deadline
- [ ] **May 18, 2026 11:59 PM UTC** — submit BEFORE this time
