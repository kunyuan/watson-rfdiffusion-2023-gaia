# Module: s3_unconditional

### unconditional_generates_diverse_structures

**QID:** `github:watson_rfdiffusion_2023::unconditional_generates_diverse_structures`
**Type:** claim
**Role:** derived
**Content:** Starting from random noise with no conditioning information, RFdiffusion generates elaborate protein structures spanning a wide range of alpha, beta, and mixed alpha-beta topologies, with little overall structural similarity to structures seen during training (as quantified by TM-score to PDB), indicating considerable generalization beyond the PDB. The designs are diverse and the divergence from known structures increases with protein length.
**Belief:** 0.96
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::af2_validates_unconditional_designs`, `github:watson_rfdiffusion_2023::alt_af2_coincidence`
**Derived from:** abduction
**Premises:** `github:watson_rfdiffusion_2023::experimental_validation_monomers`, `github:watson_rfdiffusion_2023::alt_nonspecific_folding`
**metadata:** {'figure': 'artifacts/images/a2edf1159fef613aca489410c9267ab0944878967855ac284ddd740f587eb780.jpg', 'caption': 'Fig. 2 | Outstanding performance of RFdiffusion for monomer generation. Unconditional generation, TM-score novelty, AF2 validation, comparison with Hallucination, ablation studies, experimental CD/thermostability.'}

### af2_validates_unconditional_designs

**QID:** `github:watson_rfdiffusion_2023::af2_validates_unconditional_designs`
**Type:** claim
**Role:** independent
**Content:** AF2 and ESMFold predictions are very close to the RFdiffusion design structure models for unconditional de novo designs with as many as 600 residues. Unconditional samples are closely repredicted by AF2 up to about 400 amino acids.
**Prior:** 0.92
**Belief:** 1.00
**metadata:** {'figure': 'artifacts/images/a2edf1159fef613aca489410c9267ab0944878967855ac284ddd740f587eb780.jpg', 'caption': 'Fig. 2 | Outstanding performance of RFdiffusion for monomer generation. Unconditional generation, TM-score novelty, AF2 validation, comparison with Hallucination, ablation studies, experimental CD/thermostability.'}
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::unconditional_generates_diverse_structures`

### experimental_validation_monomers

**QID:** `github:watson_rfdiffusion_2023::experimental_validation_monomers`
**Type:** claim
**Role:** independent
**Content:** Experimental characterization of six 300-amino-acid designs and three 200-amino-acid designs showed circular dichroism (CD) spectra consistent with the mixed alpha-beta topologies of the designs and extreme thermostability.
**Prior:** 0.92
**Belief:** 1.00
**metadata:** {'figure': 'artifacts/images/a2edf1159fef613aca489410c9267ab0944878967855ac284ddd740f587eb780.jpg', 'caption': 'Fig. 2 | Outstanding performance of RFdiffusion for monomer generation. Unconditional generation, TM-score novelty, AF2 validation, comparison with Hallucination, ablation studies, experimental CD/thermostability.'}
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::unconditional_generates_diverse_structures`; abduction -> `github:watson_rfdiffusion_2023::ideality_and_stability`; induction -> `github:watson_rfdiffusion_2023::ideality_and_stability`

### outperforms_hallucination

**QID:** `github:watson_rfdiffusion_2023::outperforms_hallucination`
**Type:** claim
**Role:** independent
**Content:** RFdiffusion significantly outperforms Hallucination with RF at unconditional monomer generation (two-proportion z-test: n = 400 designs per condition, z = 9.5, P = 1.6 × 10⁻²¹). Although Hallucination successfully generates designs up to 100 amino acids in length, in silico success rates rapidly deteriorate beyond this length.
**Prior:** 0.92
**Belief:** 1.00
**metadata:** {'figure': 'artifacts/images/a2edf1159fef613aca489410c9267ab0944878967855ac284ddd740f587eb780.jpg', 'caption': 'Fig. 2 | Outstanding performance of RFdiffusion for monomer generation. Unconditional generation, TM-score novelty, AF2 validation, comparison with Hallucination, ablation studies, experimental CD/thermostability.'}
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::comprehensive_improvement`; induction -> `github:watson_rfdiffusion_2023::comprehensive_improvement`

### fold_conditioned_generation

**QID:** `github:watson_rfdiffusion_2023::fold_conditioned_generation`
**Type:** claim
**Role:** independent
**Content:** RFdiffusion can be further fine-tuned to condition on secondary structure and/or fold information, enabling rapid and accurate generation of diverse designs with desired topologies. In silico success rates were 42.5% for TIM barrels and 54.1% for NTF2 folds. Experimental characterization of 11 TIM barrel designs indicated that at least 8 were soluble, thermostable, and had CD spectra consistent with the design model.
**Prior:** 0.88
**Belief:** 1.00
**metadata:** {'figure': 'artifacts/images/a2edf1159fef613aca489410c9267ab0944878967855ac284ddd740f587eb780.jpg', 'caption': 'Fig. 2 | Outstanding performance of RFdiffusion for monomer generation. Unconditional generation, TM-score novelty, AF2 validation, comparison with Hallucination, ablation studies, experimental CD/thermostability.'}
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::ideality_and_stability`; induction -> `github:watson_rfdiffusion_2023::ideality_and_stability`

### alt_af2_coincidence

**QID:** `github:watson_rfdiffusion_2023::alt_af2_coincidence`
**Type:** claim
**Role:** independent
**Content:** The close agreement between AF2 predictions and RFdiffusion design models could be an artifact of both methods sharing similar biases from PDB training data, rather than reflecting genuine design quality.
**Prior:** 0.20
**Belief:** 0.23
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::unconditional_generates_diverse_structures`

### alt_nonspecific_folding

**QID:** `github:watson_rfdiffusion_2023::alt_nonspecific_folding`
**Type:** claim
**Role:** independent
**Content:** The observed CD spectra and thermostability could arise from non-specific aggregation or misfolded but stable structures rather than the designed alpha-beta topologies.
**Prior:** 0.20
**Belief:** 0.23
**Referenced by:** abduction -> `github:watson_rfdiffusion_2023::unconditional_generates_diverse_structures`
