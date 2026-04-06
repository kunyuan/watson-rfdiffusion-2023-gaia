"""Functional-Motif Scaffolding and Enzyme Active Site Scaffolding — RFdiffusion outperforms prior methods at scaffolding diverse functional sites."""

from gaia.lang import claim, setting, noisy_and, abduction, induction

from .motivation import in_silico_success_definition
from .s2_method import pipeline_description

# --- Settings ---

motif_scaffolding_definition = setting(
    "Functional-motif scaffolding is the task of building a protein scaffold that "
    "holds a structural motif (carrying binding or catalytic function) in precisely "
    "the 3D geometry needed for optimal function. In RFdiffusion, motifs are input "
    "as 3D coordinates (including sequence and sidechains) during both conditional "
    "training and inference.",
    title="Definition of motif scaffolding",
)

benchmark_definition = setting(
    "An in silico benchmark test comprising 25 motif-scaffolding design problems "
    "was established from six recent publications, spanning simple inpainting problems, "
    "viral epitopes, receptor traps, small molecule binding sites, binding interfaces, "
    "and enzyme active sites. In silico success requires AF2 r.m.s.d. to design model "
    "<2 Å, AF2 r.m.s.d. to native motif <1 Å, and AF2 pAE <5. 100 designs were "
    "generated per problem.",
    title="25-problem motif-scaffolding benchmark",
)

# --- Claims ---

rfdiffusion_benchmark_performance = claim(
    "RFdiffusion solves 23 of the 25 benchmark motif-scaffolding problems, compared "
    "to 15 for Hallucination and 19 for RFjoint Inpainting. For 19 out of 23 solved "
    "problems, RFdiffusion's fraction of successful designs is higher than either "
    "Hallucination or RFjoint Inpainting. RFdiffusion required no hyperparameter "
    "tuning or external potentials, unlike Hallucination which required problem-specific "
    "optimization.",
    title="RFdiffusion solves 23/25 benchmark problems",
    background=[benchmark_definition, in_silico_success_definition],
    metadata={
        "figure": "artifacts/images/b9ba557d59edb1c6fc17c597416041b2cc53f83dc0abd00c7fdf2422273052f2.jpg",
        "caption": "Fig. 4 | Scaffolding of diverse functional sites with RFdiffusion. 25-problem benchmark comparison, p53-MDM2 scaffolding, enzyme active site scaffolding.",
    },
)

hallucination_benchmark = claim(
    "Hallucination with RF solves 15 of the 25 benchmark motif-scaffolding problems "
    "and sometimes requires problem-specific hyperparameter optimization.",
    title="Hallucination solves 15/25 benchmark problems",
    background=[benchmark_definition],
)

rf_inpainting_benchmark = claim(
    "RFjoint Inpainting solves 19 of the 25 benchmark motif-scaffolding problems.",
    title="RFjoint Inpainting solves 19/25 benchmark problems",
    background=[benchmark_definition],
)

noise_free_reverse = claim(
    "In 17 out of 23 solved problems, RFdiffusion generated successful solutions "
    "with higher in silico success rates when noise was not added during the reverse "
    "diffusion trajectories.",
    title="Noise-free reverse trajectories often improve success",
)

motif_not_from_training = claim(
    "The ability of RFdiffusion to scaffold functional motifs is not related to "
    "their presence in the RFdiffusion training set.",
    title="Scaffolding success independent of training set membership",
)

# --- p53-MDM2 binder scaffolding ---

p53_mdm2_design = claim(
    "RFdiffusion scaffolded the p53 helix that binds MDM2 in the presence of MDM2, "
    "so extra interactions could be designed. Out of 96 designs, 55 showed detectable "
    "binding at 10 μM. The overall experimental success rate (binding at or above 50% "
    "of maximal response) was high.",
    title="p53-MDM2 binder scaffolding: 55/96 designs show binding",
    metadata={
        "figure": "artifacts/images/b9ba557d59edb1c6fc17c597416041b2cc53f83dc0abd00c7fdf2422273052f2.jpg",
        "caption": "Fig. 4 | Scaffolding of diverse functional sites with RFdiffusion. 25-problem benchmark comparison, p53-MDM2 scaffolding, enzyme active site scaffolding.",
    },
)

p53_mdm2_affinity = claim(
    "The highest affinity p53-MDM2 scaffold binders achieved dissociation constants "
    "of 0.5 nM and 0.7 nM by biolayer interferometry (BLI), three orders of magnitude "
    "higher affinity than the reported 600 nM affinity of the p53 peptide alone.",
    title="p53-MDM2 binder affinity: 0.5-0.7 nM vs 600 nM native",
    metadata={
        "figure": "artifacts/images/b9ba557d59edb1c6fc17c597416041b2cc53f83dc0abd00c7fdf2422273052f2.jpg",
        "caption": "Fig. 4 | Scaffolding of diverse functional sites with RFdiffusion. 25-problem benchmark comparison, p53-MDM2 scaffolding, enzyme active site scaffolding.",
    },
)

# --- Enzyme active site scaffolding ---

enzyme_scaffolding_success = claim(
    "Following fine-tuning on a task mimicking enzyme active site scaffolding, "
    "RFdiffusion was able to scaffold enzyme active sites comprising many sidechain "
    "and backbone functional groups with high accuracy and in silico success rates "
    "across a range of enzyme classes (EC1-5). In silico success for enzyme scaffolding "
    "required this fine-tuning step.",
    title="Enzyme active site scaffolding succeeds after fine-tuning",
    background=[in_silico_success_definition],
    metadata={
        "figure": "artifacts/images/b9ba557d59edb1c6fc17c597416041b2cc53f83dc0abd00c7fdf2422273052f2.jpg",
        "caption": "Fig. 4 | Scaffolding of diverse functional sites with RFdiffusion. 25-problem benchmark comparison, p53-MDM2 scaffolding, enzyme active site scaffolding.",
    },
)

retroaldolase_demonstration = claim(
    "As a demonstration of implicit substrate modeling, RFdiffusion scaffolded a "
    "retroaldolase active site triad while implicitly modeling the reaction substrate "
    "using an external potential to guide pocket generation around the active site.",
    title="Retroaldolase active site scaffolding with implicit substrate",
)

# --- Strategies ---

# Benchmark comparison: RFdiffusion vs Hallucination vs Inpainting
_strat_benchmark = noisy_and(
    [pipeline_description, hallucination_benchmark, rf_inpainting_benchmark],
    rfdiffusion_benchmark_performance,
    reason=(
        "RFdiffusion's superior benchmark performance (23/25 vs 15/25 for Hallucination "
        "and 19/25 for RFjoint Inpainting) is attributed to @pipeline_description — the "
        "iterative diffusion approach conditioned on motif coordinates. The comparison "
        "against @hallucination_benchmark and @rf_inpainting_benchmark on the same 25 "
        "problems with the same success metric provides a controlled evaluation. "
        "RFdiffusion required no problem-specific tuning, unlike Hallucination."
    ),
    background=[benchmark_definition, motif_scaffolding_definition, in_silico_success_definition],
)

# p53-MDM2: experimental binding validates scaffolding
alt_nonspecific_binding_p53_mdm2 = claim(
    "The 55/96 binding success rate for p53-MDM2 scaffolds could be due to "
    "non-specific interactions between the expressed proteins and MDM2, rather "
    "than specific binding mediated by the scaffolded p53 helix.",
    title="Alternative: non-specific binding in p53-MDM2 screens",
)

_strat_p53_binding = abduction(
    observation=p53_mdm2_design,
    hypothesis=rfdiffusion_benchmark_performance,
    alternative=alt_nonspecific_binding_p53_mdm2,
    reason=(
        "The experimental observation (@p53_mdm2_design) that 55 out of 96 scaffolded "
        "designs show detectable binding to MDM2 at 10 μM provides experimental evidence "
        "supporting @rfdiffusion_benchmark_performance — that RFdiffusion effectively "
        "scaffolds functional motifs. Non-specific binding is unlikely given the high "
        "hit rate and the sub-nanomolar affinities achieved."
    ),
)

_strat_p53_affinity = noisy_and(
    [p53_mdm2_design],
    p53_mdm2_affinity,
    reason=(
        "From the 55 binders identified in @p53_mdm2_design, BLI titrations of the "
        "top candidates revealed 0.5 nM and 0.7 nM affinities. The three-order-of-magnitude "
        "improvement over the native p53 peptide (600 nM) demonstrates that RFdiffusion "
        "not only scaffolds the motif but enables design of additional stabilizing "
        "interactions with the target (average 31% increased buried surface area)."
    ),
)

# Scaffolding success is independent of training set → abduction
alt_memorization = claim(
    "RFdiffusion's scaffolding success could be due to memorizing motifs seen during "
    "training rather than genuine generalization to new motifs.",
    title="Alternative: training set memorization",
)

_strat_generalization = abduction(
    observation=motif_not_from_training,
    hypothesis=rfdiffusion_benchmark_performance,
    alternative=alt_memorization,
    reason=(
        "The observation (@motif_not_from_training, Supplementary Fig. 7) that scaffolding "
        "success is uncorrelated with training set membership is best explained by "
        "@rfdiffusion_benchmark_performance reflecting genuine generalization. The "
        "alternative — that success comes from memorizing training motifs — is directly "
        "contradicted by the lack of correlation."
    ),
)

# Multiple benchmark-supporting observations → induction into benchmark performance
alt_noise_free_overfitting = claim(
    "Improvement without noise could reflect overfitting to the benchmark set rather "
    "than genuine model quality.",
    title="Alternative: noise-free improvement is overfitting",
)
alt_training_correlation_artifact = claim(
    "The lack of correlation between success and training set membership could be a "
    "sampling artifact rather than genuine generalization.",
    title="Alternative: training correlation is sampling artifact",
)

_strat_benchmark_support = induction(
    [noise_free_reverse, motif_not_from_training],
    rfdiffusion_benchmark_performance,
    alt_exps=[alt_noise_free_overfitting, alt_training_correlation_artifact],
    reason=(
        "Two independent technical findings support @rfdiffusion_benchmark_performance: "
        "@noise_free_reverse (17/23 problems improve without noise) reveals that the model's "
        "deterministic predictions are already high-quality; @motif_not_from_training confirms "
        "generalization beyond the training set. Both point to a robust scaffolding capability."
    ),
)

# Enzyme scaffolding requires fine-tuning, with retroaldolase as demonstration
_strat_enzyme = noisy_and(
    [pipeline_description, retroaldolase_demonstration],
    enzyme_scaffolding_success,
    reason=(
        "Enzyme active site scaffolding extends @pipeline_description to scaffolding "
        "minimal descriptions comprising a few amino acid sidechains, requiring additional "
        "fine-tuning. @retroaldolase_demonstration provides a concrete example: scaffolding "
        "a retroaldolase active site triad while implicitly modeling the substrate via "
        "an external potential."
    ),
    background=[motif_scaffolding_definition, in_silico_success_definition],
)
