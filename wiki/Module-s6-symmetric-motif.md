# Module: s6_symmetric_motif

### metal_coordination_geometry

**QID:** `github:watson_rfdiffusion_2023::metal_coordination_geometry`
**Type:** setting
**Role:** setting
**Content:** Divalent transition metal ions show distinct preferences for specific coordination geometries (square planar, tetrahedral, octahedral) with ion-specific optimal sidechain-metal bond lengths. RFdiffusion provides a general route to building symmetric protein assemblies around such sites, with the symmetry of the assembly matching the symmetry of the coordination geometry.

### sars_cov2_trimeric_binder_design

**QID:** `github:watson_rfdiffusion_2023::sars_cov2_trimeric_binder_design`
**Type:** claim
**Role:** derived
**Content:** RFdiffusion designed C3-symmetric trimers that rigidly hold three copies of the ACE2 mimic AHB2 binding domain to match the ACE2 binding sites on the SARS-CoV-2 spike protein trimer. AF2 predictions recapitulated the AHB2 structure with 0.6 Å r.m.s.d. over the asymmetric unit and 2.9 Å r.m.s.d. over the C3 assembly. These rigid symmetric fusions reduce entropic cost of binding while maintaining avidity benefits from multivalency.
**Belief:** 0.88
**Derived from:** noisy_and
**Premises:** `github:watson_rfdiffusion_2023::symmetric_high_success`, `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`
**metadata:** {'figure': 'artifacts/images/2f0036d9fb1bf924ca04b19874c78b2c9f147639a86d9b96af264f915aba96df.jpg', 'caption': 'Fig. 5 | Symmetric motif scaffolding with RFdiffusion. C3-symmetric SARS-CoV-2 trimeric binders, C4 Ni²⁺-binding assemblies with ITC and nsEM validation.'}

### ni_binding_design

**QID:** `github:watson_rfdiffusion_2023::ni_binding_design`
**Type:** claim
**Role:** derived
**Content:** C4 protein assemblies were designed with four central histidine imidazoles arranged in an ideal Ni²⁺-binding site with square-planar coordination geometry. Diverse designs starting from distinct C4-symmetric histidine sites had good in silico success with histidine residues in near-ideal geometries for coordinating metal in the AF2-predicted structures.
**Belief:** 1.00
**Derived from:** noisy_and
**Premises:** `github:watson_rfdiffusion_2023::symmetric_high_success`
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::ni_binding_endothermic`, `github:watson_rfdiffusion_2023::alt_uniform_nonspecific_mechanism`
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::ni_binding_experimental`, `github:watson_rfdiffusion_2023::alt_nonspecific_metal_chelation`
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::ni_binding_histidine_dependence`, `github:watson_rfdiffusion_2023::alt_indirect_structural_disruption_h52a`
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::ni_binding_nsem`, `github:watson_rfdiffusion_2023::alt_alternative_c4_arrangement`
**metadata:** {'figure': 'artifacts/images/2f0036d9fb1bf924ca04b19874c78b2c9f147639a86d9b96af264f915aba96df.jpg', 'caption': 'Fig. 5 | Symmetric motif scaffolding with RFdiffusion. C3-symmetric SARS-CoV-2 trimeric binders, C4 Ni²⁺-binding assemblies with ITC and nsEM validation.'}

### ni_binding_experimental

**QID:** `github:watson_rfdiffusion_2023::ni_binding_experimental`
**Type:** claim
**Role:** independent
**Content:** Of 44 Ni²⁺-binding C4 designs expressed and purified in E. coli, 37 had SEC chromatograms consistent with the intended oligomeric state. Of 36 tested by isothermal titration calorimetry (ITC), 18 bound Ni²⁺ with dissociation constants ranging from low nanomolar to low micromolar. Inflection points in wild-type isotherms indicated binding with the designed 1:4 stoichiometry (ion:monomer).
**Prior:** 0.92
**Belief:** 1.00
**metadata:** {'figure': 'artifacts/images/2f0036d9fb1bf924ca04b19874c78b2c9f147639a86d9b96af264f915aba96df.jpg', 'caption': 'Fig. 5 | Symmetric motif scaffolding with RFdiffusion. C3-symmetric SARS-CoV-2 trimeric binders, C4 Ni²⁺-binding assemblies with ITC and nsEM validation.'}
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::ni_binding_design`

### ni_binding_histidine_dependence

**QID:** `github:watson_rfdiffusion_2023::ni_binding_histidine_dependence`
**Type:** claim
**Role:** independent
**Content:** Mutation of the designed histidine residue (H52) to alanine abolished or notably reduced Ni²⁺ binding in 17 out of 17 cases with successful expression, confirming that metal binding is mediated by the scaffolded histidine residues.
**Prior:** 0.92
**Belief:** 1.00
**metadata:** {'figure': 'artifacts/images/2f0036d9fb1bf924ca04b19874c78b2c9f147639a86d9b96af264f915aba96df.jpg', 'caption': 'Fig. 5 | Symmetric motif scaffolding with RFdiffusion. C3-symmetric SARS-CoV-2 trimeric binders, C4 Ni²⁺-binding assemblies with ITC and nsEM validation.'}
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::ni_binding_design`

### ni_binding_nsem

**QID:** `github:watson_rfdiffusion_2023::ni_binding_nsem`
**Type:** claim
**Role:** independent
**Content:** nsEM characterization of four Ni²⁺-binding designs (NiB1.12, NiB1.15, NiB1.17, NiB1.20) that showed histidine-dependent binding all showed clear fourfold symmetry in raw micrographs and 2D class averages. A 3D reconstruction of NiB1.17 was in close agreement with the design model.
**Prior:** 0.88
**Belief:** 1.00
**metadata:** {'figure': 'artifacts/images/2f0036d9fb1bf924ca04b19874c78b2c9f147639a86d9b96af264f915aba96df.jpg', 'caption': 'Fig. 5 | Symmetric motif scaffolding with RFdiffusion. C3-symmetric SARS-CoV-2 trimeric binders, C4 Ni²⁺-binding assemblies with ITC and nsEM validation.'}
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::ni_binding_design`

### ni_binding_endothermic

**QID:** `github:watson_rfdiffusion_2023::ni_binding_endothermic`
**Type:** claim
**Role:** independent
**Content:** Although most designed Ni²⁺-binding proteins showed exothermic metal coordination, a few cases (NiB2.9, NiB2.10, NiB2.15, NiB2.23) showed endothermic binding, suggesting that Ni²⁺ coordination is entropically driven in these assemblies.
**Prior:** 0.88
**Belief:** 1.00
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::ni_binding_design`

### alt_uniform_nonspecific_mechanism

**QID:** `github:watson_rfdiffusion_2023::alt_uniform_nonspecific_mechanism`
**Type:** claim
**Role:** independent
**Content:** The diversity of binding thermodynamics (exothermic and endothermic) could arise from varying degrees of non-specific surface interactions rather than designed coordination at distinct engineered sites.
**Prior:** 0.20
**Belief:** 0.20
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::ni_binding_design`

### alt_nonspecific_metal_chelation

**QID:** `github:watson_rfdiffusion_2023::alt_nonspecific_metal_chelation`
**Type:** claim
**Role:** independent
**Content:** The ITC binding signals could arise from non-specific metal chelation by surface-exposed histidine or other residues rather than the designed square-planar binding site.
**Prior:** 0.22
**Belief:** 0.22
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::ni_binding_design`

### alt_indirect_structural_disruption_h52a

**QID:** `github:watson_rfdiffusion_2023::alt_indirect_structural_disruption_h52a`
**Type:** claim
**Role:** independent
**Content:** Ni²⁺ binding could be mediated by other residues, with H52A mutation indirectly disrupting binding through structural perturbation rather than direct loss of the coordinating residue.
**Prior:** 0.12
**Belief:** 0.12
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::ni_binding_design`

### alt_alternative_c4_arrangement

**QID:** `github:watson_rfdiffusion_2023::alt_alternative_c4_arrangement`
**Type:** claim
**Role:** independent
**Content:** The fourfold symmetry in nsEM could arise from a different C4-symmetric arrangement that does not involve the designed metal-binding site.
**Prior:** 0.12
**Belief:** 0.12
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::ni_binding_design`
