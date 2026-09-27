# X API - Optional Extension

Do not make X a dependency of the MVP.

Use it only after the core historical pipeline works. The main reason is that recent search and full-archive access have different access/pricing constraints, while the M5 core period is 2011-2016.

If you obtain access later, add `X_BEARER_TOKEN` to `.env` and create a current social-sentiment pipeline separated from the historical M5 forecasting experiment.
