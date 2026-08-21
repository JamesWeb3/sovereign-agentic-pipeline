# voice/ — Whisper STT + Piper/Kokoro TTS, local only

**Plan Step:** Step 9 (Part B — pipeline) · **Lead:** Karl
**Status:** scaffolded only. Part B starts week 10; do not implement ahead of that.

## What this will be

A local voice interface: **Whisper** for speech-to-text and **Piper** (or **Kokoro**) for
text-to-speech, both running on-device. This is the sovereignty claim taken to its
end — even the microphone-to-model path never leaves the country. No hosted speech API.

**Done** when a spoken question is transcribed locally, answered by the agent (Step 8), and
spoken back — with nothing leaving the machine.
