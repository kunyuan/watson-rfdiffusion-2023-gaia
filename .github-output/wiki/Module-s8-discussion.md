# Module: s8_discussion

### comprehensive_improvement

**QID:** `github:watson_rfdiffusion_2023::comprehensive_improvement`
**Type:** claim
**Role:** derived
**Content:** RFdiffusion is a comprehensive improvement over current protein design methods: (1) it generates diverse unconditional designs up to 600 residues far exceeding previous methods; (2) it enables higher-order architectures with any desired symmetry, unlike Hallucination methods limited to cyclic symmetries; (3) it outperforms all previous methods on motif scaffolding benchmarks; (4) it raises binder design success rates by two orders of magnitude.
**Belief:** 0.99
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::outperforms_hallucination`, `github:watson_rfdiffusion_2023::alt_outperforms_other_explanation`
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`, `github:watson_rfdiffusion_2023::alt_benchmark_other_explanation`
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::binder_success_rate`, `github:watson_rfdiffusion_2023::alt_binder_other_explanation`
**Derived from:** induction
**Premises:** `github:watson_rfdiffusion_2023::outperforms_hallucination`, `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`, `github:watson_rfdiffusion_2023::binder_success_rate`, `github:watson_rfdiffusion_2023::alt_outperforms_other_explanation`, `github:watson_rfdiffusion_2023::alt_benchmark_other_explanation`, `github:watson_rfdiffusion_2023::alt_binder_other_explanation`
**Referenced by:** noisy_and -> `github:watson_rfdiffusion_2023::rfdiffusion_broad_success`

### ideality_and_stability

**QID:** `github:watson_rfdiffusion_2023::ideality_and_stability`
**Type:** claim
**Role:** derived
**Content:** Despite substantially increased complexity, the ideality and stability of RFdiffusion designs is akin to that of de novo protein designs generated using previous methods such as Rosetta. Half of tested unconditional designs express in a soluble way and have CD spectra consistent with design models and high thermostability.
**Belief:** 0.93
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::experimental_validation_monomers`, `github:watson_rfdiffusion_2023::alt_ideality_exp_artifact`
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::fold_conditioned_generation`, `github:watson_rfdiffusion_2023::alt_ideality_fold_artifact`
**Derived from:** induction
**Premises:** `github:watson_rfdiffusion_2023::experimental_validation_monomers`, `github:watson_rfdiffusion_2023::fold_conditioned_generation`, `github:watson_rfdiffusion_2023::alt_ideality_exp_artifact`, `github:watson_rfdiffusion_2023::alt_ideality_fold_artifact`

### generality_claim

**QID:** `github:watson_rfdiffusion_2023::generality_claim`
**Type:** claim
**Role:** derived
**Content:** In a manner analogous to networks that produce images from user-specified inputs, RFdiffusion enables the design of diverse functional proteins from simple molecular specifications (e.g., high-affinity binders to a user-specified target protein, diverse protein assemblies from user-specified symmetries), with minimal specialist knowledge required.
**Belief:** 0.61
**Derived from:** noisy_and
**Premises:** `github:watson_rfdiffusion_2023::rfdiffusion_broad_success`

### future_nucleic_acids

**QID:** `github:watson_rfdiffusion_2023::future_nucleic_acids`
**Type:** claim
**Role:** orphaned
**Content:** RoseTTAFold has been extended to nucleic acids and protein-nucleic acid complexes (RoseTTAFoldNA), which should enable RFdiffusion to design nucleic acid binding proteins and perhaps folded RNA structures.
**Prior:** 0.70
**Belief:** 0.70

### future_ligands

**QID:** `github:watson_rfdiffusion_2023::future_ligands`
**Type:** claim
**Role:** orphaned
**Content:** Extension of RF to incorporate ligands should enable extension of RFdiffusion to explicitly model ligand atoms and allow the design of protein-ligand interactions.
**Prior:** 0.65
**Belief:** 0.65

### alt_outperforms_other_explanation

**QID:** `github:watson_rfdiffusion_2023::alt_outperforms_other_explanation`
**Type:** claim
**Role:** independent
**Content:** RFdiffusion's statistical superiority over Hallucination (z=9.5) could be an artifact of the specific benchmark setup or in silico metric rather than genuine method superiority.
**Prior:** 0.15
**Belief:** 0.16
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::comprehensive_improvement`; induction -> `github:watson_rfdiffusion_2023::comprehensive_improvement`

### alt_benchmark_other_explanation

**QID:** `github:watson_rfdiffusion_2023::alt_benchmark_other_explanation`
**Type:** claim
**Role:** independent
**Content:** Solving 23/25 motif scaffolding problems could reflect an easy benchmark rather than genuine method capability.
**Prior:** 0.20
**Belief:** 0.21
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::comprehensive_improvement`; induction -> `github:watson_rfdiffusion_2023::comprehensive_improvement`

### alt_binder_other_explanation

**QID:** `github:watson_rfdiffusion_2023::alt_binder_other_explanation`
**Type:** claim
**Role:** independent
**Content:** The 19% binder success rate could be inflated by the AF2 filtering step rather than reflecting RFdiffusion's backbone generation quality.
**Prior:** 0.25
**Belief:** 0.26
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::comprehensive_improvement`; induction -> `github:watson_rfdiffusion_2023::comprehensive_improvement`

### alt_ideality_exp_artifact

**QID:** `github:watson_rfdiffusion_2023::alt_ideality_exp_artifact`
**Type:** claim
**Role:** independent
**Content:** The CD spectra and thermostability of unconditional designs could reflect non-specific stable folds rather than the designed topologies.
**Prior:** 0.25
**Belief:** 0.30
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::ideality_and_stability`; induction -> `github:watson_rfdiffusion_2023::ideality_and_stability`

### alt_ideality_fold_artifact

**QID:** `github:watson_rfdiffusion_2023::alt_ideality_fold_artifact`
**Type:** claim
**Role:** independent
**Content:** The TIM barrel experimental success (8/11) could be due to the inherent stability of the TIM barrel fold rather than RFdiffusion design quality.
**Prior:** 0.30
**Belief:** 0.35
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::ideality_and_stability`; induction -> `github:watson_rfdiffusion_2023::ideality_and_stability`
