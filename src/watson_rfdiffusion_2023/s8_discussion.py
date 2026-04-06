"""Discussion — Comprehensive improvement over prior methods and future extensions."""

from gaia.lang import claim, noisy_and

from .motivation import rfdiffusion_broad_success
from .s3_unconditional import (
    outperforms_hallucination,
    experimental_validation_monomers,
    fold_conditioned_generation,
)
from .s4_oligomers import symmetric_high_success
from .s5_motif_scaffolding import rfdiffusion_benchmark_performance, p53_mdm2_affinity
from .s6_symmetric_motif import ni_binding_experimental
from .s7_binder_design import ha20_atomic_accuracy, binder_success_rate

# --- Claims ---

comprehensive_improvement = claim(
    "RFdiffusion is a comprehensive improvement over current protein design methods: "
    "(1) it generates diverse unconditional designs up to 600 residues far exceeding "
    "previous methods; (2) it enables higher-order architectures with any desired "
    "symmetry, unlike Hallucination methods limited to cyclic symmetries; "
    "(3) it outperforms all previous methods on motif scaffolding benchmarks; "
    "(4) it raises binder design success rates by two orders of magnitude.",
    title="RFdiffusion is comprehensive improvement over prior methods",
)

ideality_and_stability = claim(
    "Despite substantially increased complexity, the ideality and stability of "
    "RFdiffusion designs is akin to that of de novo protein designs generated using "
    "previous methods such as Rosetta. Half of tested unconditional designs express "
    "in a soluble way and have CD spectra consistent with design models and high "
    "thermostability.",
    title="RFdiffusion designs retain Rosetta-level ideality and stability",
)

generality_claim = claim(
    "In a manner analogous to networks that produce images from user-specified inputs, "
    "RFdiffusion enables the design of diverse functional proteins from simple molecular "
    "specifications (e.g., high-affinity binders to a user-specified target protein, "
    "diverse protein assemblies from user-specified symmetries), with minimal specialist "
    "knowledge required.",
    title="RFdiffusion enables protein design from minimal specifications",
)

future_nucleic_acids = claim(
    "RoseTTAFold has been extended to nucleic acids and protein-nucleic acid complexes "
    "(RoseTTAFoldNA), which should enable RFdiffusion to design nucleic acid binding "
    "proteins and perhaps folded RNA structures.",
    title="Future extension to nucleic acids via RoseTTAFoldNA",
)

future_ligands = claim(
    "Extension of RF to incorporate ligands should enable extension of RFdiffusion to "
    "explicitly model ligand atoms and allow the design of protein-ligand interactions.",
    title="Future extension to explicit ligand modeling",
)

# --- Strategies ---

# Comprehensive improvement: 3 key results (outperforms is now leaf, not 4-premise)
_strat_comprehensive = noisy_and(
    [outperforms_hallucination, rfdiffusion_benchmark_performance, binder_success_rate],
    comprehensive_improvement,
    reason=(
        "Three independent lines of evidence establish comprehensive improvement: "
        "(1) @outperforms_hallucination — significantly better unconditional generation "
        "(z = 9.5, P = 1.6 × 10⁻²¹). "
        "(2) @rfdiffusion_benchmark_performance — 23/25 scaffolding problems solved. "
        "(3) @binder_success_rate — 19% binder success, ~100× over Rosetta. "
        "Symmetric oligomer success (separately validated) further supports this."
    ),
)

# Ideality claim from experimental data
_strat_ideality = noisy_and(
    [experimental_validation_monomers, fold_conditioned_generation],
    ideality_and_stability,
    reason=(
        "@experimental_validation_monomers shows 9 designs with correct CD spectra "
        "and extreme thermostability. @fold_conditioned_generation shows 8/11 TIM "
        "barrel designs soluble and thermostable. Together these confirm Rosetta-level "
        "ideality despite increased structural complexity."
    ),
)

# Broad success directly from comprehensive improvement + atomic-level validation
_strat_broad_success = noisy_and(
    [comprehensive_improvement, ha20_atomic_accuracy],
    rfdiffusion_broad_success,
    reason=(
        "@comprehensive_improvement establishes performance superiority across all "
        "application areas. @ha20_atomic_accuracy provides atomic-level structural "
        "proof (0.63 Å cryo-EM). Together these establish outstanding performance "
        "across all tested design tasks."
    ),
)

# Generality from broad success
_strat_generality = noisy_and(
    [rfdiffusion_broad_success],
    generality_claim,
    reason=(
        "@rfdiffusion_broad_success covers unconditional design, symmetric oligomers, "
        "motif scaffolding, enzyme sites, and binder design — all from simple molecular "
        "specifications. The analogy to image generation follows: users specify what "
        "they want and RFdiffusion generates diverse solutions."
    ),
)
