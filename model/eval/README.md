# model/eval/ — the protected held-out eval

**Step 5 (Part B) · Lead: James · Status: scaffolded only**

## ⚠ This directory is protected

The 100-question held-out set is **never used for training and never tuned against.**

If Step 5 slips, **cut the dataset size, never the eval set.** A small dataset with a
rigorous eval is a result; a big one with a rushed eval measures nothing.

Treat any change under this directory as requiring explicit sign-off. The eval set's
whole value is that no part of the pipeline has ever seen it — one leak and the number it
produces is worthless.

**Done** when a fixed, documented 100-question set lives here, sealed off from the
training data in `../dataset/`, with a scoring script that reports results honestly.
