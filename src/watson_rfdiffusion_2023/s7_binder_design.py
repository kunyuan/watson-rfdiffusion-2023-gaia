"""De Novo Design of Protein-Binding Proteins — RFdiffusion generates high-affinity binders with two orders of magnitude higher success rates."""

from gaia.lang import claim, setting, noisy_and, abduction

from .motivation import alphafold2_definition, in_silico_success_definition
from .s2_method import pipeline_description

# --- Settings ---

binder_design_approach = setting(
    "For binder design, RFdiffusion was fine-tuned on protein complex structures, "
    "with a feature indicating a subset of residues on the target chain ('interface "
    "hotspot residues') to which the diffused chain binds. An additional model was "
    "fine-tuned to condition binder diffusion on secondary structure and block-adjacency "
    "information for coarse-grained topology control, in addition to interface hotspots.",
    title="RFdiffusion binder design approach",
)

binder_filtering = setting(
    "Designed binders were filtered by AF2 confidence in the interface and monomer "
    "structure, and 95 designs were selected per target for experimental characterization.",
    title="AF2-based binder filtering",
)

# --- Claims ---

previous_binder_design_limitations = claim(
    "The previous Rosetta-based method for de novo binder design from target structure "
    "information alone required testing tens of thousands of designs (many thousands "
    "screened per campaign) with low experimental success rates, and relied on "
    "prespecifying particular protein scaffolds, limiting diversity and shape "
    "complementarity. No deep-learning method had previously demonstrated experimental "
    "general success in designing completely de novo binders.",
    title="Prior binder design methods had low success rates",
)

binder_success_rate = claim(
    "The overall experimental success rate for RFdiffusion binders (binding at or "
    "above 50% of maximal BLI response for positive control at 10 μM) was 19% across "
    "five targets, an increase of roughly two orders of magnitude over the previous "
    "Rosetta-based method on the same targets. Binders were identified for all five "
    "targets with fewer than 100 designs tested per target.",
    title="19% binder success rate — 100× improvement over Rosetta",
    background=[binder_filtering],
)

binder_targets_and_affinities = claim(
    "De novo binders were designed against five targets: Influenza A H1 Haemagglutinin "
    "(HA), Interleukin-7 Receptor-α (IL-7Rα), Programmed Death-Ligand 1 (PD-L1), "
    "Insulin Receptor (InsR), and Tropomyosin Receptor Kinase A (TrkA). Full BLI "
    "titrations showed nanomolar affinities with no further experimental optimization, "
    "including HA and IL-7Rα binders with affinities of ~30 nM.",
    title="Nanomolar binders to five therapeutic targets",
)

two_orders_attribution = claim(
    "The two-orders-of-magnitude improvement in binder design success rate is "
    "attributed approximately one order of magnitude to RFdiffusion itself (better "
    "backbone generation) and the second order of magnitude to filtering with AF2 "
    "(better design selection).",
    title="Success rate improvement attributed to RFdiffusion + AF2 filtering",
    background=[in_silico_success_definition],
)

binder_specificity = claim(
    "Six of the highest affinity IL-7Rα binders were assessed by competition BLI, "
    "and all six competed for binding with a structurally validated positive control "
    "binding to the same site, indicating site-specific binding.",
    title="IL-7Rα binders show site-specific binding",
)

novel_interfaces = claim(
    "Binding interfaces designed by RFdiffusion were often highly distinct from "
    "interfaces to these targets found in the PDB.",
    title="Novel binding interfaces distinct from PDB",
)

# --- Cryo-EM validation of HA_20 ---

ha20_cryoem_structure = claim(
    "The cryo-EM structure of the highest affinity Influenza binder (HA_20, Kd = 28 nM) "
    "in complex with Iowa43 HA was solved at 2.9 Å resolution. 3D heterogeneous "
    "refinement without symmetry revealed full occupancy of all three HA stem epitopes "
    "by HA_20.",
    title="Cryo-EM structure of HA_20-HA complex at 2.9 Å",
)

ha20_matches_design = claim(
    "The cryo-EM 3D structure of the HA_20-HA complex almost perfectly matches the "
    "computational design model with 0.63 Å backbone r.m.s.d. Over the binder alone, "
    "the experimental structure deviates from the RFdiffusion design by only 0.6 Å.",
    title="HA_20 cryo-EM structure matches design at 0.63 Å r.m.s.d.",
)

ha20_atomic_accuracy = claim(
    "The near-perfect agreement between the cryo-EM structure and the RFdiffusion "
    "design model (0.63 Å r.m.s.d.) demonstrates that RFdiffusion can design "
    "functional proteins with atomic-level accuracy and precisely target functionally "
    "relevant sites on therapeutically important proteins.",
    title="RFdiffusion achieves atomic-level accuracy in binder design",
)

# --- Strategies ---

# Binder success rate from RFdiffusion + AF2 filtering
_strat_binder_success = noisy_and(
    [pipeline_description, previous_binder_design_limitations, two_orders_attribution],
    binder_success_rate,
    reason=(
        "The 19% binder success rate results from @pipeline_description applied to "
        "protein complexes (fine-tuned with interface hotspot conditioning). "
        "@previous_binder_design_limitations establishes the baseline (~0.1-0.2% for "
        "Rosetta). @two_orders_attribution decomposes the improvement: ~10× from "
        "RFdiffusion's better backbone generation and ~10× from AF2 filtering. "
        "Binders were found for all five targets with <100 designs per target."
    ),
    background=[binder_design_approach, binder_filtering],
)

# Nanomolar affinities from the screening
_strat_binder_affinities = noisy_and(
    [binder_success_rate],
    binder_targets_and_affinities,
    reason=(
        "From the binder hits identified by BLI screening (@binder_success_rate), "
        "full BLI titrations revealed nanomolar affinities across all five targets "
        "with no experimental optimization needed (HA ~30 nM, IL-7Rα ~30 nM). "
        "This demonstrates that RFdiffusion generates high-quality interfaces "
        "directly, without requiring affinity maturation."
    ),
)

# Novel interfaces support de novo design claim
_strat_novel_interfaces = noisy_and(
    [novel_interfaces],
    binder_success_rate,
    reason=(
        "@novel_interfaces shows that the designed binding interfaces are often highly "
        "distinct from natural interfaces to these targets in the PDB, confirming that "
        "@binder_success_rate reflects genuinely de novo design rather than recapitulation "
        "of known binding modes."
    ),
)

# Competition BLI confirms specificity
alt_nonspecific_adhesion = claim(
    "The binders could achieve high BLI signals through non-specific adhesion "
    "to the target surface rather than site-specific binding at the designed "
    "interface.",
    title="Alternative: non-specific adhesion",
)

_strat_specificity = abduction(
    observation=binder_specificity,
    hypothesis=binder_success_rate,
    alternative=alt_nonspecific_adhesion,
    reason=(
        "The observation (@binder_specificity) that all six tested IL-7Rα binders "
        "compete with a structurally validated positive control binding to the same "
        "site provides evidence of site-specific binding, supporting that "
        "@binder_success_rate reflects genuine designed interactions rather than "
        "non-specific adhesion."
    ),
)

# Cryo-EM: observation → design accuracy hypothesis
alt_ha20_alternative_conformation = claim(
    "The cryo-EM density could be fit to a different structural model that does "
    "not resemble the RFdiffusion design, indicating the binder adopted an "
    "alternative conformation.",
    title="Alternative: HA_20 adopts alternative conformation",
)

_strat_ha20_matches = abduction(
    observation=ha20_cryoem_structure,
    hypothesis=ha20_matches_design,
    alternative=alt_ha20_alternative_conformation,
    reason=(
        "The observation (@ha20_cryoem_structure) of a 2.9 Å cryo-EM structure showing "
        "full occupancy of all three HA stem epitopes is best explained by "
        "@ha20_matches_design — the design folds as predicted. The 0.63 Å r.m.s.d. "
        "between the cryo-EM structure and design model is well within experimental "
        "error, making an alternative conformation extremely unlikely."
    ),
)

# Design match → atomic accuracy conclusion
_strat_atomic_accuracy = noisy_and(
    [ha20_matches_design, binder_success_rate],
    ha20_atomic_accuracy,
    reason=(
        "@ha20_matches_design provides the strongest structural evidence: 0.63 Å "
        "r.m.s.d. between cryo-EM and design model, and 0.6 Å over the binder alone. "
        "Combined with @binder_success_rate showing this works across multiple targets, "
        "this demonstrates that RFdiffusion achieves atomic-level design accuracy for "
        "functional proteins targeting therapeutically relevant sites."
    ),
)
