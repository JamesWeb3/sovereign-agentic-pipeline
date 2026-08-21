# model/ — Mistral open weights + LoRA

**Plan Step:** Step 5 (Part B — pipeline) · **Lead:** James
**Status:** scaffolded only. Part B starts week 10 (w/c 20 Oct); James leads it. Do not
implement ahead of that — this directory exists so the structure and the protected eval
rule are on the record now.

## What this will be

A LoRA fine-tune of a Mistral open-weights base on ~1000 NZ-domain instruction pairs,
served locally. No hosted inference — the sovereignty constraint applies here most of all.

## Layout

- `dataset/` — the ~1000 NZ-domain training pairs (Step 5).
- `eval/` — the **protected** 100-question held-out set. ⚠ See `eval/README.md`.
- `train_lora.py` — the training entry point (stub until Part B).

## Definition of done (Step 5, when Part B reaches it)

- A reproducible LoRA fine-tune producing a locally-servable adapter.
- Training and eval sets kept strictly separate (see the warning in `eval/`).
- Results — including a loss to a hosted baseline, if that is what happens — recorded
  honestly per `docs/methodology.md`.
