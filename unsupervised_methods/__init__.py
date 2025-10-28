"""Unsupervised methods for physiological signal extraction.

This module contains classical computer vision methods for extracting
physiological signals (heart rate, respiration rate) from videos without
requiring training data.

Methods include:
- POS (Plane-Orthogonal-to-Skin)
- CHROM (Chrominance-based)
- ICA (Independent Component Analysis)
- GREEN (Green channel)
- LGI (Local Group Invariance)
- PBV (Pulse Blood Volume)

Note: This is a minimal implementation. For full functionality, refer to the
original rPPG-Toolbox repository: https://github.com/ubicomplab/rPPG-Toolbox
"""

from unsupervised_methods.unsupervised_predictor import unsupervised_predict

__all__ = ['unsupervised_predict']
