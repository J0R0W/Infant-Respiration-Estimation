"""Unsupervised prediction methods for physiological signal extraction.

This module provides inference functions for classical computer vision methods
that extract physiological signals without requiring trained models.

Note: This is a minimal stub implementation to prevent import errors.
For full implementations of unsupervised methods (POS, CHROM, ICA, etc.),
please refer to the original rPPG-Toolbox repository.
"""

import numpy as np
import torch
from tqdm import tqdm


def unsupervised_predict(config, data_loader, method_name):
    """
    Run unsupervised prediction using classical computer vision methods.

    Args:
        config: Configuration object
        data_loader: DataLoader for the dataset
        method_name: Name of the method (POS, CHROM, ICA, GREEN, LGI, PBV)

    Note: This is a minimal stub implementation. The actual implementation
    would include signal processing algorithms for extracting physiological
    signals from video frames.

    For the AIR-125 and COHFACE datasets used in this project, we focus on
    the supervised deep learning approach (VIRENet/AIRFlowNet) rather than
    unsupervised methods.
    """
    print(f"\n{'='*70}")
    print(f"Unsupervised Method: {method_name}")
    print(f"{'='*70}")

    print(f"\n⚠ WARNING: This is a stub implementation.")
    print(f"The full {method_name} method is not implemented in this repository.")
    print(f"\nFor complete unsupervised methods, please refer to:")
    print(f"https://github.com/ubicomplab/rPPG-Toolbox")
    print(f"\nThis project focuses on supervised learning with VIRENet/AIRFlowNet.")
    print(f"To use this project, set TOOLBOX_MODE to 'train_and_test' or 'only_test'.")
    print(f"\n{'='*70}\n")

    # Minimal implementation to prevent crashes
    predictions = []
    labels = []

    print(f"Processing {len(data_loader)} batches...")
    for batch_idx, batch in enumerate(tqdm(data_loader, desc=method_name)):
        # In a real implementation, this would:
        # 1. Extract RGB signals from facial regions
        # 2. Apply the specific algorithm (POS, CHROM, etc.)
        # 3. Extract frequency-domain features
        # 4. Compute physiological metrics

        # Placeholder: just extract labels if available
        if isinstance(batch, dict) and 'label' in batch:
            labels.append(batch['label'].cpu().numpy())

    print(f"\n⚠ No predictions generated (stub implementation).")
    print(f"Please use supervised methods (VIRENet) for actual inference.\n")

    return None


def _extract_rgb_signals(frames, roi):
    """
    Extract RGB signals from regions of interest.

    Args:
        frames: Video frames (N, C, H, W)
        roi: Region of interest coordinates

    Returns:
        RGB signals (N, 3) for N frames

    Note: Stub implementation.
    """
    # In a real implementation:
    # - Detect face/region of interest
    # - Extract mean RGB values from ROI
    # - Apply preprocessing (detrending, filtering)
    pass


def _apply_pos_algorithm(rgb_signals):
    """
    Apply Plane-Orthogonal-to-Skin (POS) algorithm.

    Reference:
    Wang, W., et al. "Algorithmic principles of remote PPG."
    IEEE Transactions on Biomedical Engineering, 2017.

    Note: Stub implementation.
    """
    pass


def _apply_chrom_algorithm(rgb_signals):
    """
    Apply CHROM (Chrominance-based) algorithm.

    Reference:
    De Haan, G., & Jeanne, V. "Robust pulse rate from chrominance-based rPPG."
    IEEE Transactions on Biomedical Engineering, 2013.

    Note: Stub implementation.
    """
    pass


def _apply_ica_algorithm(rgb_signals):
    """
    Apply Independent Component Analysis (ICA).

    Reference:
    Poh, M. Z., et al. "Non-contact, automated cardiac pulse measurements
    using video imaging and blind source separation."
    Optics express, 2010.

    Note: Stub implementation.
    """
    pass


def _compute_metrics(predictions, labels, method_name, config):
    """
    Compute evaluation metrics.

    Args:
        predictions: Predicted signals/values
        labels: Ground truth labels
        method_name: Name of the method
        config: Configuration object

    Note: Stub implementation.
    """
    pass
