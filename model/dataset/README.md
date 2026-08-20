# model/dataset/ — NZ-domain training pairs

**Step 5 (Part B) · Lead: James · Status: scaffolded only**

The ~1000 NZ-domain instruction/response pairs the LoRA fine-tune trains on. Kept strictly
separate from the held-out set in `../eval/` — nothing here may overlap with an eval
question, or the eval stops measuring anything.

If time is short, this is the set that shrinks (see `../eval/README.md`): quality and
domain coverage over raw count.

**Done** when the pairs are assembled, deduplicated against the eval set, and documented
(what NZ domains they cover, where they came from).
