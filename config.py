from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"

# Drug response: one row per (cell line, drug) fitted dose-response curve.
# Prefer GDSC2 over GDSC1 where a drug/cell line pair exists in both — GDSC2 used
# CellTiter-Glo and GDSC1 used Resazurin/Syto60 (older, noisier assay).
GDSC1_PATH = DATA_DIR / "GDSC1_fitted_dose_response_27Oct23.xlsx"
GDSC2_PATH = DATA_DIR / "GDSC2_fitted_dose_response_27Oct23.xlsx"

# Cell line metadata: model_list's `model_id` matches GDSC's `SANGER_MODEL_ID` and 
# the RNA-seq column headers below directly, so no ID lookup is needed to join them. 
MODEL_LIST_PATH = DATA_DIR / "model_list_20260814.csv"

# Gene expression (RNA-seq): rows = genes, columns = cell lines (model_id).
RNASEQ_TPM_PATH = DATA_DIR / "rnaseq_merged_20260323" / "rnaseq_merged_rsem_tpm_20260323.csv"
