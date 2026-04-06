"""Symmetric Functional-Motif Scaffolding — SARS-CoV-2 trimeric binders and Ni²⁺-coordinating assemblies."""

from gaia.lang import claim, setting, noisy_and, abduction

from .motivation import alphafold2_definition
from .s4_oligomers import symmetric_high_success
from .s5_motif_scaffolding import rfdiffusion_benchmark_performance

# --- Settings ---

metal_coordination_geometry = setting(
    "Divalent transition metal ions show distinct preferences for specific coordination "
    "geometries (square planar, tetrahedral, octahedral) with ion-specific optimal "
    "sidechain-metal bond lengths. RFdiffusion provides a general route to building "
    "symmetric protein assemblies around such sites, with the symmetry of the assembly "
    "matching the symmetry of the coordination geometry.",
    title="Metal coordination geometry principles",
)

# --- Claims ---

sars_cov2_trimeric_binder_design = claim(
    "RFdiffusion designed C3-symmetric trimers that rigidly hold three copies of "
    "the ACE2 mimic AHB2 binding domain to match the ACE2 binding sites on the "
    "SARS-CoV-2 spike protein trimer. AF2 predictions recapitulated the AHB2 "
    "structure with 0.6 Å r.m.s.d. over the asymmetric unit and 2.9 Å r.m.s.d. "
    "over the C3 assembly. These rigid symmetric fusions reduce entropic cost of "
    "binding while maintaining avidity benefits from multivalency.",
    title="C3-symmetric SARS-CoV-2 trimeric binder design",
    background=[alphafold2_definition],
)

ni_binding_design = claim(
    "C4 protein assemblies were designed with four central histidine imidazoles "
    "arranged in an ideal Ni²⁺-binding site with square-planar coordination geometry. "
    "Diverse designs starting from distinct C4-symmetric histidine sites had good "
    "in silico success with histidine residues in near-ideal geometries for coordinating "
    "metal in the AF2-predicted structures.",
    title="C4 Ni²⁺-binding assembly design with square-planar geometry",
    background=[metal_coordination_geometry, alphafold2_definition],
)

ni_binding_experimental = claim(
    "Of 44 Ni²⁺-binding C4 designs expressed and purified in E. coli, 37 had SEC "
    "chromatograms consistent with the intended oligomeric state. Of 36 tested by "
    "isothermal titration calorimetry (ITC), 18 bound Ni²⁺ with dissociation constants "
    "ranging from low nanomolar to low micromolar. Inflection points in wild-type "
    "isotherms indicated binding with the designed 1:4 stoichiometry (ion:monomer).",
    title="18/36 Ni²⁺-binding designs experimentally confirmed",
)

ni_binding_histidine_dependence = claim(
    "Mutation of the designed histidine residue (H52) to alanine abolished or notably "
    "reduced Ni²⁺ binding in 17 out of 17 cases with successful expression, confirming "
    "that metal binding is mediated by the scaffolded histidine residues.",
    title="H52A mutation abolishes Ni²⁺ binding",
)

ni_binding_nsem = claim(
    "nsEM characterization of four Ni²⁺-binding designs (NiB1.12, NiB1.15, NiB1.17, "
    "NiB1.20) that showed histidine-dependent binding all showed clear fourfold "
    "symmetry in raw micrographs and 2D class averages. A 3D reconstruction of "
    "NiB1.17 was in close agreement with the design model.",
    title="nsEM confirms C4 symmetry of Ni²⁺ binders",
)

ni_binding_endothermic = claim(
    "Although most designed Ni²⁺-binding proteins showed exothermic metal coordination, "
    "a few cases (NiB2.9, NiB2.10, NiB2.15, NiB2.23) showed endothermic binding, "
    "suggesting that Ni²⁺ coordination is entropically driven in these assemblies.",
    title="Some Ni²⁺-binding designs show entropy-driven coordination",
)

# --- Strategies ---

# Trimeric binder combines symmetric design + motif scaffolding
_strat_sars_cov2 = noisy_and(
    [symmetric_high_success, rfdiffusion_benchmark_performance],
    sars_cov2_trimeric_binder_design,
    reason=(
        "The C3-symmetric SARS-CoV-2 trimeric binder design combines two established "
        "capabilities: @symmetric_high_success (RFdiffusion can generate symmetric "
        "oligomers) and @rfdiffusion_benchmark_performance (RFdiffusion can scaffold "
        "functional motifs). The design rigidly holds three AHB2 binding domains in "
        "C3 symmetry matching the spike trimer, and AF2 predictions confirm the "
        "structural accuracy."
    ),
    background=[alphafold2_definition],
)

# Ni²⁺ binding design combines symmetric design + metal geometry
_strat_ni_design = noisy_and(
    [symmetric_high_success],
    ni_binding_design,
    reason=(
        "The Ni²⁺-binding C4 assembly design extends @symmetric_high_success to "
        "coordinate metal ions. The C4 protein symmetry is matched to the square-planar "
        "coordination geometry of Ni²⁺, with four histidine imidazoles positioned at "
        "the symmetry center. AF2 predictions show near-ideal histidine geometries."
    ),
    background=[metal_coordination_geometry, alphafold2_definition],
)

# Endothermic binding diversity → abduction supporting designed coordination
alt_uniform_nonspecific_mechanism = claim(
    "The diversity of binding thermodynamics (exothermic and endothermic) could arise "
    "from varying degrees of non-specific surface interactions rather than designed "
    "coordination at distinct engineered sites.",
    title="Alternative: non-specific mechanism producing diverse thermodynamics",
)

_strat_ni_endothermic = abduction(
    observation=ni_binding_endothermic,
    hypothesis=ni_binding_design,
    alternative=alt_uniform_nonspecific_mechanism,
    reason=(
        "The observation (@ni_binding_endothermic) that some Ni²⁺-binding designs show "
        "endothermic ITC signals while most are exothermic is best explained by "
        "@ni_binding_design — genuine designed coordination at distinct engineered sites "
        "with different scaffold environments leading to different thermodynamic signatures. "
        "A uniform non-specific mechanism would be unlikely to produce this thermodynamic "
        "diversity across designs."
    ),
)

# Experimental validation of Ni²⁺ binding
alt_nonspecific_metal_chelation = claim(
    "The ITC binding signals could arise from non-specific metal chelation by "
    "surface-exposed histidine or other residues rather than the designed "
    "square-planar binding site.",
    title="Alternative: non-specific metal chelation",
)

_strat_ni_experimental = abduction(
    observation=ni_binding_experimental,
    hypothesis=ni_binding_design,
    alternative=alt_nonspecific_metal_chelation,
    reason=(
        "The observation (@ni_binding_experimental) that 18/36 designs bind Ni²⁺ with "
        "the designed 1:4 stoichiometry supports @ni_binding_design. The correct "
        "stoichiometry is strong evidence for the designed binding mechanism, as "
        "non-specific chelation would not show this precise ratio."
    ),
)

# H52A mutation confirms designed binding site
alt_indirect_structural_disruption_h52a = claim(
    "Ni²⁺ binding could be mediated by other residues, with H52A mutation "
    "indirectly disrupting binding through structural perturbation rather than "
    "direct loss of the coordinating residue.",
    title="Alternative: indirect structural disruption by H52A",
)

_strat_ni_histidine = abduction(
    observation=ni_binding_histidine_dependence,
    hypothesis=ni_binding_design,
    alternative=alt_indirect_structural_disruption_h52a,
    reason=(
        "The observation (@ni_binding_histidine_dependence) that H52A mutation abolished "
        "or notably reduced Ni²⁺ binding in 17/17 cases provides direct evidence that "
        "the designed histidine residue mediates metal coordination, as predicted by "
        "@ni_binding_design. While indirect structural disruption is possible for one "
        "design, the consistency across 17 designs makes this alternative unlikely."
    ),
)

# nsEM confirms C4 symmetry
alt_alternative_c4_arrangement = claim(
    "The fourfold symmetry in nsEM could arise from a different C4-symmetric "
    "arrangement that does not involve the designed metal-binding site.",
    title="Alternative: alternative C4 arrangement without designed site",
)

_strat_ni_nsem = abduction(
    observation=ni_binding_nsem,
    hypothesis=ni_binding_design,
    alternative=alt_alternative_c4_arrangement,
    reason=(
        "The nsEM observation (@ni_binding_nsem) of clear fourfold symmetry in "
        "micrographs and 2D class averages, with NiB1.17's 3D reconstruction matching "
        "the design model, confirms that @ni_binding_design's intended C4 architecture "
        "is realized. Combined with histidine-dependent binding, the alternative of "
        "a different C4 arrangement is not supported."
    ),
)
