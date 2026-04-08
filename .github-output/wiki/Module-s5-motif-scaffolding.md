# Module: s5_motif_scaffolding

### motif_scaffolding_definition

**QID:** `github:watson_rfdiffusion_2023::motif_scaffolding_definition`
**Type:** setting
**Role:** setting
**Content:** Functional-motif scaffolding is the task of building a protein scaffold that holds a structural motif (carrying binding or catalytic function) in precisely the 3D geometry needed for optimal function. In RFdiffusion, motifs are input as 3D coordinates (including sequence and sidechains) during both conditional training and inference.

### benchmark_definition

**QID:** `github:watson_rfdiffusion_2023::benchmark_definition`
**Type:** setting
**Role:** setting
**Content:** An in silico benchmark test comprising 25 motif-scaffolding design problems was established from six recent publications, spanning simple inpainting problems, viral epitopes, receptor traps, small molecule binding sites, binding interfaces, and enzyme active sites. In silico success requires AF2 r.m.s.d. to design model <2 Å, AF2 r.m.s.d. to native motif <1 Å, and AF2 pAE <5. 100 designs were generated per problem.

### rfdiffusion_benchmark_performance

**QID:** `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`
**Type:** claim
**Role:** derived
**Content:** RFdiffusion solves 23 of the 25 benchmark motif-scaffolding problems, compared to 15 for Hallucination and 19 for RFjoint Inpainting. For 19 out of 23 solved problems, RFdiffusion's fraction of successful designs is higher than either Hallucination or RFjoint Inpainting. RFdiffusion required no hyperparameter tuning or external potentials, unlike Hallucination which required problem-specific optimization.
**Belief:** 1.00
**Derived from:** noisy_and
**Premises:** `github:watson_rfdiffusion_2023::pipeline_description`, `github:watson_rfdiffusion_2023::hallucination_benchmark`, `github:watson_rfdiffusion_2023::rf_inpainting_benchmark`
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::p53_mdm2_design`, `github:watson_rfdiffusion_2023::alt_nonspecific_binding_p53_mdm2`
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::noise_free_reverse`, `github:watson_rfdiffusion_2023::alt_noise_free_overfitting`
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::motif_not_from_training`, `github:watson_rfdiffusion_2023::alt_memorization`
**Derived from:** induction
**Premises:** `github:watson_rfdiffusion_2023::noise_free_reverse`, `github:watson_rfdiffusion_2023::motif_not_from_training`, `github:watson_rfdiffusion_2023::alt_noise_free_overfitting`, `github:watson_rfdiffusion_2023::alt_memorization`
**figure:** artifacts/images/b9ba557d59edb1c6fc17c597416041b2cc53f83dc0abd00c7fdf2422273052f2.jpg
**caption:** Fig. 4 | Scaffolding of diverse functional sites with RFdiffusion. 25-problem benchmark comparison, p53-MDM2 scaffolding, enzyme active site scaffolding.
**Referenced by:** noisy_and -> `github:watson_rfdiffusion_2023::sars_cov2_trimeric_binder_design`; abduction -> `github:watson_rfdiffusion_2023::comprehensive_improvement`; induction -> `github:watson_rfdiffusion_2023::comprehensive_improvement`

### hallucination_benchmark

**QID:** `github:watson_rfdiffusion_2023::hallucination_benchmark`
**Type:** claim
**Role:** independent
**Content:** Hallucination with RF solves 15 of the 25 benchmark motif-scaffolding problems and sometimes requires problem-specific hyperparameter optimization.
**Prior:** 0.88
**Belief:** 1.00
**Referenced by:** noisy_and -> `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`

### rf_inpainting_benchmark

**QID:** `github:watson_rfdiffusion_2023::rf_inpainting_benchmark`
**Type:** claim
**Role:** independent
**Content:** RFjoint Inpainting solves 19 of the 25 benchmark motif-scaffolding problems.
**Prior:** 0.88
**Belief:** 1.00
**Referenced by:** noisy_and -> `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`

### noise_free_reverse

**QID:** `github:watson_rfdiffusion_2023::noise_free_reverse`
**Type:** claim
**Role:** independent
**Content:** In 17 out of 23 solved problems, RFdiffusion generated successful solutions with higher in silico success rates when noise was not added during the reverse diffusion trajectories.
**Prior:** 0.88
**Belief:** 1.00
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`; induction -> `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`

### motif_not_from_training

**QID:** `github:watson_rfdiffusion_2023::motif_not_from_training`
**Type:** claim
**Role:** independent
**Content:** The ability of RFdiffusion to scaffold functional motifs is not related to their presence in the RFdiffusion training set.
**Prior:** 0.88
**Belief:** 1.00
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`; induction -> `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`

### p53_mdm2_design

**QID:** `github:watson_rfdiffusion_2023::p53_mdm2_design`
**Type:** claim
**Role:** independent
**Content:** RFdiffusion scaffolded the p53 helix that binds MDM2 in the presence of MDM2, so extra interactions could be designed. Out of 96 designs, 55 showed detectable binding at 10 μM. The overall experimental success rate (binding at or above 50% of maximal response) was high.
**Prior:** 0.92
**Belief:** 1.00
**figure:** artifacts/images/b9ba557d59edb1c6fc17c597416041b2cc53f83dc0abd00c7fdf2422273052f2.jpg
**caption:** Fig. 4 | Scaffolding of diverse functional sites with RFdiffusion. 25-problem benchmark comparison, p53-MDM2 scaffolding, enzyme active site scaffolding.
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`; noisy_and -> `github:watson_rfdiffusion_2023::p53_mdm2_affinity`

### p53_mdm2_affinity

**QID:** `github:watson_rfdiffusion_2023::p53_mdm2_affinity`
**Type:** claim
**Role:** derived
**Content:** The highest affinity p53-MDM2 scaffold binders achieved dissociation constants of 0.5 nM and 0.7 nM by biolayer interferometry (BLI), three orders of magnitude higher affinity than the reported 600 nM affinity of the p53 peptide alone.
**Belief:** 0.88
**Derived from:** noisy_and
**Premises:** `github:watson_rfdiffusion_2023::p53_mdm2_design`
**figure:** artifacts/images/b9ba557d59edb1c6fc17c597416041b2cc53f83dc0abd00c7fdf2422273052f2.jpg
**caption:** Fig. 4 | Scaffolding of diverse functional sites with RFdiffusion. 25-problem benchmark comparison, p53-MDM2 scaffolding, enzyme active site scaffolding.

### enzyme_scaffolding_success

**QID:** `github:watson_rfdiffusion_2023::enzyme_scaffolding_success`
**Type:** claim
**Role:** derived
**Content:** Following fine-tuning on a task mimicking enzyme active site scaffolding, RFdiffusion was able to scaffold enzyme active sites comprising many sidechain and backbone functional groups with high accuracy and in silico success rates across a range of enzyme classes (EC1-5). In silico success for enzyme scaffolding required this fine-tuning step.
**Belief:** 0.62
**Derived from:** noisy_and
**Premises:** `github:watson_rfdiffusion_2023::pipeline_description`, `github:watson_rfdiffusion_2023::retroaldolase_demonstration`
**figure:** artifacts/images/b9ba557d59edb1c6fc17c597416041b2cc53f83dc0abd00c7fdf2422273052f2.jpg
**caption:** Fig. 4 | Scaffolding of diverse functional sites with RFdiffusion. 25-problem benchmark comparison, p53-MDM2 scaffolding, enzyme active site scaffolding.

### retroaldolase_demonstration

**QID:** `github:watson_rfdiffusion_2023::retroaldolase_demonstration`
**Type:** claim
**Role:** independent
**Content:** As a demonstration of implicit substrate modeling, RFdiffusion scaffolded a retroaldolase active site triad while implicitly modeling the reaction substrate using an external potential to guide pocket generation around the active site.
**Prior:** 0.80
**Belief:** 0.80
**Referenced by:** noisy_and -> `github:watson_rfdiffusion_2023::enzyme_scaffolding_success`

### alt_nonspecific_binding_p53_mdm2

**QID:** `github:watson_rfdiffusion_2023::alt_nonspecific_binding_p53_mdm2`
**Type:** claim
**Role:** independent
**Content:** The 55/96 binding success rate for p53-MDM2 scaffolds could be due to non-specific interactions between the expressed proteins and MDM2, rather than specific binding mediated by the scaffolded p53 helix.
**Prior:** 0.18
**Belief:** 0.18
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`

### alt_memorization

**QID:** `github:watson_rfdiffusion_2023::alt_memorization`
**Type:** claim
**Role:** independent
**Content:** RFdiffusion's scaffolding success could be due to memorizing motifs seen during training rather than genuine generalization to new motifs.
**Prior:** 0.15
**Belief:** 0.15
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`; induction -> `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`

### alt_noise_free_overfitting

**QID:** `github:watson_rfdiffusion_2023::alt_noise_free_overfitting`
**Type:** claim
**Role:** independent
**Content:** Improvement without noise could reflect overfitting to the benchmark set rather than genuine model quality.
**Prior:** 0.20
**Belief:** 0.20
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`; induction -> `github:watson_rfdiffusion_2023::rfdiffusion_benchmark_performance`
