"""Unconditional Protein Monomer Generation — RFdiffusion generates diverse, novel protein structures from random noise."""

from gaia.lang import claim, setting, noisy_and, abduction

from .motivation import in_silico_success_definition, alphafold2_definition
from .s2_method import (
    pipeline_description,
    self_conditioning_improvement,
    pretraining_benefit,
    mse_loss_design,
    compute_efficiency,
)

# --- Claims ---

unconditional_generates_diverse_structures = claim(
    "Starting from random noise with no conditioning information, RFdiffusion "
    "generates elaborate protein structures spanning a wide range of alpha, beta, "
    "and mixed alpha-beta topologies, with little overall structural similarity to "
    "structures seen during training (as quantified by TM-score to PDB), indicating "
    "considerable generalization beyond the PDB. The designs are diverse and the "
    "divergence from known structures increases with protein length.",
    title="RFdiffusion generates diverse novel structures unconditionally",
    background=[in_silico_success_definition],
)

af2_validates_unconditional_designs = claim(
    "AF2 and ESMFold predictions are very close to the RFdiffusion design structure "
    "models for unconditional de novo designs with as many as 600 residues. Unconditional "
    "samples are closely repredicted by AF2 up to about 400 amino acids.",
    title="AF2 validates unconditional designs up to 600 residues",
    background=[alphafold2_definition],
)

experimental_validation_monomers = claim(
    "Experimental characterization of six 300-amino-acid designs and three 200-amino-acid "
    "designs showed circular dichroism (CD) spectra consistent with the mixed alpha-beta "
    "topologies of the designs and extreme thermostability.",
    title="Experimental validation of unconditional monomer designs",
)

outperforms_hallucination = claim(
    "RFdiffusion significantly outperforms Hallucination with RF at unconditional "
    "monomer generation (two-proportion z-test: n = 400 designs per condition, "
    "z = 9.5, P = 1.6 × 10⁻²¹). Although Hallucination successfully generates "
    "designs up to 100 amino acids in length, in silico success rates rapidly "
    "deteriorate beyond this length.",
    title="RFdiffusion outperforms RF Hallucination",
    background=[in_silico_success_definition],
)

fold_conditioned_generation = claim(
    "RFdiffusion can be further fine-tuned to condition on secondary structure and/or "
    "fold information, enabling rapid and accurate generation of diverse designs with "
    "desired topologies. In silico success rates were 42.5% for TIM barrels and 54.1% "
    "for NTF2 folds. Experimental characterization of 11 TIM barrel designs indicated "
    "that at least 8 were soluble, thermostable, and had CD spectra consistent with "
    "the design model.",
    title="Fold-conditioned generation achieves high success rates",
)

# --- Strategies ---

# AF2 validation is an observation that supports the diversity claim (abduction)
alt_af2_coincidence = claim(
    "The close agreement between AF2 predictions and RFdiffusion design models could "
    "be an artifact of both methods sharing similar biases from PDB training data, "
    "rather than reflecting genuine design quality.",
    title="Alternative: AF2/RFdiffusion shared PDB bias",
)

_strat_af2_validates = abduction(
    observation=af2_validates_unconditional_designs,
    hypothesis=unconditional_generates_diverse_structures,
    alternative=alt_af2_coincidence,
    reason=(
        "The observation (@af2_validates_unconditional_designs) that AF2 and ESMFold — "
        "independently trained structure predictors — closely reproduce RFdiffusion designs "
        "up to 600 residues is best explained by @unconditional_generates_diverse_structures: "
        "the designs encode genuinely realistic protein folds. The shared-bias alternative "
        "is weakened by the use of two independent predictors (AF2 and ESMFold) and the "
        "fact that designs have low TM-scores to PDB structures."
    ),
    background=[alphafold2_definition],
)

# Experimental validation: observation that designs fold as predicted
alt_nonspecific_folding = claim(
    "The observed CD spectra and thermostability could arise from non-specific "
    "aggregation or misfolded but stable structures rather than the designed "
    "alpha-beta topologies.",
    title="Alternative: non-specific folding",
)

_strat_exp_validation = abduction(
    observation=experimental_validation_monomers,
    hypothesis=unconditional_generates_diverse_structures,
    alternative=alt_nonspecific_folding,
    reason=(
        "The experimental observation (@experimental_validation_monomers) that 9 designs "
        "show CD spectra consistent with their designed mixed alpha-beta topologies and "
        "extreme thermostability is best explained by @unconditional_generates_diverse_structures — "
        "that RFdiffusion generates realistic protein structures. The alternative of "
        "non-specific aggregation is unlikely given the specific CD spectral signatures "
        "matching the designed topologies."
    ),
)

# Compute efficiency: direct measurement supports pipeline effectiveness
_strat_compute = noisy_and(
    [pipeline_description],
    compute_efficiency,
    reason=(
        "The @pipeline_description's iterative denoising process generates a 100-residue "
        "protein in ~11 seconds vs 8.5 minutes for Hallucination, because RFdiffusion "
        "predicts the final structure at each timestep allowing larger inference steps "
        "and early trajectory truncation."
    ),
)
